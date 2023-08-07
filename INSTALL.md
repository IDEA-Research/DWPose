# Installation
## For MMPose
🌵 You can refer [MMPose Installation](https://mmpose.readthedocs.io/en/latest/installation.html) or
```
# Set environment
pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

## For ControlNet
🌵 First, make sure to run ControlNet successfully.
```
# Set environment
conda env create -f environment.yaml
conda activate control-v11
```
🌵 Second, install tools to apply DWPose to ControlNet
```
# Set environment
pip install onnxruntime
```