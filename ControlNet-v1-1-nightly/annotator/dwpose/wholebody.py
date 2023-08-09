import cv2
import numpy as np

from .cv_ox_det import inference_detector
from .cv_ox_pose import inference_pose

class Wholebody:
    def __init__(self):
        device = 'cpu'
        backend = cv2.dnn.DNN_BACKEND_OPENCV if device == 'cpu' else cv2.dnn.DNN_BACKEND_CUDA
        # You need to manually build OpenCV through cmake to work with your GPU.
        providers = cv2.dnn.DNN_TARGET_CPU if device == 'cpu' else cv2.dnn.DNN_TARGET_CUDA

        onnx_det = 'annotator/ckpts/yolox_l.onnx'
        onnx_pose = 'annotator/ckpts/dw-ll_ucoco_384.onnx'

        self.session_det = cv2.dnn.readNetFromONNX(onnx_det)
        self.session_det.setPreferableBackend(backend)
        self.session_det.setPreferableTarget(providers)

        self.session_pose = cv2.dnn.readNetFromONNX(onnx_pose)
        self.session_pose.setPreferableBackend(backend)
        self.session_pose.setPreferableTarget(providers)
    
    def __call__(self, oriImg):
        det_result = inference_detector(self.session_det, oriImg)
        keypoints, scores = inference_pose(self.session_pose, det_result, oriImg)

        keypoints_info = np.concatenate(
            (keypoints, scores[..., None]), axis=-1)
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

        keypoints, scores = keypoints_info[
            ..., :2], keypoints_info[..., 2]
        
        return keypoints, scores


