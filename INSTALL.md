# Installation
## 📙 We support two independent environments. You just need to install corresponding environment.
## For MMPose
🌵🌵🌵 This environment helps you to train and test our DWPose. You can ignore the following installation for ControlNet.

🌵 You can refer [MMPose Installation](https://mmpose.readthedocs.io/en/latest/installation.html) or
```
# Set MMPose environment
pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

## For ControlNet
🌵🌵🌵 This environment helps you to apply DWPose to ControlNet. You can ignore the above installation for mmpose.

🌵 First, make sure to run ControlNet successfully.
```
# Set ControlNet environment
conda env create -f environment.yaml
conda activate control-v11
```
🌵 Second, install tools to apply DWPose to ControlNet. If it's hard to install mmcv, you can refer branch [onnx](https://github.com/IDEA-Research/DWPose/tree/onnx), which just needs onnxruntime.
```
# Set ControlNet environment
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.1"
mim install "mmdet>=3.1.0"
mim install "mmpose>=1.1.0"
```