# Copyright (c) OpenMMLab. All rights reserved.
import numpy as np
from . import util
import cv2
import mmcv
import torch
import matplotlib.pyplot as plt
from mmpose.apis import inference_topdown
from mmpose.apis import init_model as init_pose_estimator
from mmpose.evaluation.functional import nms
from mmpose.utils import adapt_mmdet_pipeline
from mmpose.structures import merge_data_samples

from mmdet.apis import inference_detector, init_detector


class Wholebody:
    def __init__(self):
        device = 'cuda:0'
        det_config = 'annotator/dwpose/yolox_config/yolox_l_8xb8-300e_coco.py'
        det_ckpt = 'https://download.openmmlab.com/mmdetection/v2.0/yolox/yolox_l_8x8_300e_coco/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth'
        pose_config = 'annotator/dwpose/dwpose_config/dwpose-l_384x288.py'
        pose_ckpt = 'annotator/ckpts/dw-ll_ucoco_384.pth'
        
        # build detector
        self.detector = init_detector(det_config, det_ckpt, device=device)
        self.detector.cfg = adapt_mmdet_pipeline(self.detector.cfg)

        # build pose estimator
        self.pose_estimator = init_pose_estimator(
            pose_config,
            pose_ckpt,
            device=device)

    def __call__(self, oriImg):
        # predict bbox
        det_result = inference_detector(self.detector, oriImg)
        pred_instance = det_result.pred_instances.cpu().numpy()
        bboxes = np.concatenate(
            (pred_instance.bboxes, pred_instance.scores[:, None]), axis=1)
        bboxes = bboxes[np.logical_and(pred_instance.labels == 0,
                                    pred_instance.scores > 0.3)]
        # # max value
        # if len(bboxes) > 0:
        #     bboxes = bboxes[0].reshape(1,-1)
        bboxes = bboxes[nms(bboxes, 0.3), :4]

        # predict keypoints
        if len(bboxes) == 0:
            pose_results = inference_topdown(self.pose_estimator, oriImg)
        else:
            pose_results = inference_topdown(self.pose_estimator, oriImg, bboxes)
        preds = merge_data_samples(pose_results)
        preds = preds.pred_instances

        # preds = pose_results[0].pred_instances
        keypoints = preds.get('transformed_keypoints',
                                        preds.keypoints)
        if 'keypoint_scores' in preds:
            scores = preds.keypoint_scores
        else:
            scores = np.ones(keypoints.shape[:-1])

        if 'keypoints_visible' in preds:
            visible = preds.keypoints_visible
        else:
            visible = np.ones(keypoints.shape[:-1])
        keypoints_info = np.concatenate(
            (keypoints, scores[..., None], visible[..., None]),
            axis=-1)
        # compute neck joint
        neck = np.mean(keypoints_info[:, [5, 6]], axis=1)
        # neck score when visualizing pred
        neck[:, 2:4] = np.logical_and(
            keypoints_info[:, 5, 2:4] > 0.3,
            keypoints_info[:, 6, 2:4] > 0.3).astype(int)
        new_keypoints_info = np.insert(
            keypoints_info, 17, neck, axis=1)
        mmpose_idx = [
            17, 6, 8, 10, 7, 9, 12, 14, 16, 13, 15, 2, 1, 4, 3
        ]
        openpose_idx = [
            1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17
        ]
        new_keypoints_info[:, openpose_idx] = \
            new_keypoints_info[:, mmpose_idx]
        keypoints_info = new_keypoints_info

        keypoints, scores, visible = keypoints_info[
            ..., :2], keypoints_info[..., 2], keypoints_info[..., 3]
        
        return keypoints, scores
