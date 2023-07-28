
<div align="center">
<p align="center"> <img src="resources/logo.png" width="100px"> </p>
<h2>Effective Whole-body Pose Estimation with Two-stages Distillation </h2> 

<a href='https://arxiv.org/abs/xxxx.xxxx'><img src='https://img.shields.io/badge/ArXiv-xxxx.xxxx-red'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


[Zhendong Yang](https://scholar.google.com/citations?user=M9qKrogAAAAJ&hl=en&oi=sra), [Ailing Zeng](https://ailingzeng.site/), [Chun Yuan](https://scholar.google.com/citations?user=fYdxi2sAAAAJ&hl=en&oi=sra), [Yu Li](http://yu-li.github.io/)


<img src="resources/lalaland.gif" style="height:260px" />   <img src="resources/iron.gif" style="height:260px" />  
<p>&emsp; &emsp; &emsp;  DWPose   &emsp; &emsp; &emsp;   &emsp;&emsp; &emsp;   &emsp;  &emsp; &emsp;   &emsp; &emsp; &emsp;   &emsp;&emsp; &emsp;   &emsp; DWPose + ControlNet (<i>prompt: Ironman</i>) </p>

</div>

#  💃🏻  DWPose 💃🏻

This repository is the official implementation of the [Effective Whole-body Pose Estimation with Two-stages Distillation](). Our code is based on [MMPose](https://github.com/open-mmlab/mmpose/tree/main) and [ControlNet](https://github.com/lllyasviel/ControlNet-v1-1-nightly).

<img src="resources/architecture.jpg" width="650px"/>


⚔️ We release a series of models named DWPose with different sizes, from tiny to large, for human whole-body pose estimation. Besides, we also replace Openpose with DWPose for ControlNet, obtaining better Generated Images. 

## 🐟 Installation
See [installation instructions](INSTALL.md).

## 🚀 Results and Models
### 😎 DWPose on COCO. We release a series of DWPose models.

<img src="resources/compare.jpg" width="350px"/>

Results on COCO-WholeBody v1.0 val with detector having human AP of 56.4 on COCO val2017 dataset

| Arch                                    | Input Size | FLOPS (G)| Body AP | Body AR | Foot AP | Foot AR | Face AP | Face AR | Hand AP | Hand AR | Whole AP | Whole AR |                   ckpt                   |                   ckpt                   |
| :-------------------------------------- | :--------: | :--------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :------: | :------: | :--------------------------------------: | :-------------------------------------: |
| [DWPose-t](mmpose/configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-t_8xb64-270e_coco-ubody-wholebody-256x192.py) |  256x192   |0.5|  0.585  |  0.670  |  0.465  |  0.636  |  0.735  |  0.807  |  0.357  |  0.490  |  0.485   |  0.584   | [baidu drive](https://pan.baidu.com/s/1X2sVxv4JOZ5WFvOBiwjrNA?pwd=nmvw) | [google drive](https://drive.google.com/file/d/1Csbg56QvB0TtFamJ6pPWNil7h6WziDwl/view?usp=sharing) |
| [DWPose-s](mmpose/configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-s_8xb64-270e_coco-ubody-wholebody-256x192.py) |  256x192   |0.9|  0.633  |  0.713  |  0.533  |  0.690  |  0.776  |  0.841  |  0.427  |  0.549  |  0.538   |  0.632   | [baidu drive](https://pan.baidu.com/s/1k2JxCtJL9dIGU-h31UBQOA?pwd=hcf2) | [google drive](https://drive.google.com/file/d/10TuEeLhArxfd4e6bnE7YgmBI9RFvu9DL/view?usp=sharing) |
| [DWPose-m](mmpose/configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-m_8xb64-270e_coco-ubody-wholebody-256x192.py) |  256x192   |2.2|  0.685  |  0.761  |  0.636  |  0.772  |  0.828  |  0.881  |  0.527  |  0.634  |  0.606   |  0.695   | [baidu drive](https://pan.baidu.com/s/183ovcYHV6I5TQ9Wu1eS-eg?pwd=rcry) | [google drive](https://drive.google.com/file/d/13ZWnGDteGBmjALtErYS8AHhMBBNAN9en/view?usp=sharing) |
| [DWPose-l](mmpose/configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-l_8xb64-270e_coco-ubody-wholebody-256x192.py) |  256x192   |4.5|  0.704  |  0.777  |  0.662  |  0.790  |  0.843  |  0.894  |  0.566  |  0.665  |  0.631   |  0.717   | [baidu drive](https://pan.baidu.com/s/1bWEeiFL5UGoDj9Nkazb98w?pwd=u7ek) | [google drive](https://drive.google.com/file/d/1PHKN3p873dgCSh_YRsYqTZVj-kIbclRS/view?usp=sharing) |
| [DWPose-l](mmpose/configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-l_8xb32-270e_coco-ubody-wholebody-384x288.py) |  384x288   |10.1|  0.722  |  0.789  |  0.704  |  0.817  |  0.887  |  0.921  |  0.621  |  0.710  |  0.665   |  0.743   | [baidu drive](https://pan.baidu.com/s/168T2XGXQDli8j03e_dOJdg?pwd=ajcq) | [google drive](https://drive.google.com/file/d/1Oy9O18cYk8Dk776DbxpCPWmJtJCl-OCm/view?usp=sharing) |

### 🦈 DWPose for ControlNet.
First, you need to download our SOTA model [DWPose-l_384x288](https://drive.google.com/file/d/1Oy9O18cYk8Dk776DbxpCPWmJtJCl-OCm/view?usp=sharing) and put it into ControlNet-v1-1-nightly/annotator/ckpts. Then you can use DWPose to generate the images you like.
```
cd ControlNet-v1-1-nightly
python gradio_dw_open_pose.py
```

#### Non-cherry-picked test with random seed 12345 ("spider man"):
<img src="resources/jay_pose.jpg" width="600px"/>

#### Comparison with OpenPose
<img src="resources/generation.jpg" width="600px"/>

## 🚢 Datasets
Prepare [COCO](https://cocodataset.org/#download) in mmpose/data/coco and [UBody](https://github.com/IDEA-Research/OSX) in mmpose/data/UBody.

UBody needs to be tarnsferred into images. Don't forget.
```
cd mmpose
python video2image.py
```
If you want to evaluate the models on UBody
```
# add category into UBody's annotation
cd mmpose
python add_cat.py
```
## ⭐Train a model
### Train DWPose with the first stage distillation
```
cd mmpose
bash tools/dist_train.sh configs/distiller/ubody/s1_dis/rtmpose_x_dis_l__coco-ubody-256x192.py 8
```
### Train DWPose with the second stage distillation
```
cd mmpose
bash tools/dist_train.sh configs/distiller/ubody/s2_dis/dwpose_l-ll__coco-ubody-256x192.py 8
```
### Tansfer the distillation models into regular models
```
cd mmpose
# if first stage distillation
python pth_transfer.py $dis_ckpt $new_pose_ckpt
# if second stage distillation
python pth_transfer.py $dis_ckpt $new_pose_ckpt --two_dis
```
## ⭐Test a model
```
# test on UBody
bash tools/dist_test.sh configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-l_8xb64-270e_ubody-wholebody-256x192.py $pose_ckpt 8

# test on COCO
bash tools/dist_test.sh configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-l_8xb64-270e_coco-ubody-wholebody-256x192.py $pose_ckpt 8

```

## 🥳 Citation
```
@article{yang2022vitkd,
  title={Effective Whole-body Pose Estimation with Two-stages Distillation},
  author={Yang, Zhendong and Zeng, Ailing and Yuan, Chun and Li, Yu},
  journal={arXiv preprint arXiv:2209.02432},
  year={2023}
}
```

## 🥂 Acknowledgement
Our code is based on [MMPose](https://github.com/open-mmlab/mmpose/tree/main) and [ControlNet](https://github.com/lllyasviel/ControlNet-v1-1-nightly).
