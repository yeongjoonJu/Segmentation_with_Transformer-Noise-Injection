# "Adapting Transformer in Image Segmentation tasks"

1st project for Applications and Practice in Neural Networks

This repository is based on official code of mmsegmentation & SegFormer

https://github.com/open-mmlab/mmsegmentation

https://github.com/NVlabs/SegFormer


## Installation

For install and data preparation, please refer to the guidelines as follows

```
pip install torchvision==0.8.2
pip install timm==0.3.2
pip install mmcv-full==1.2.7 -f https://download.openmmlab.com/mmcv/dist/{cuda version}/{torch version}/index.html
# example, https://download.openmmlab.com/mmcv/dist/cu101/torch1.7.0/index.html
pip install opencv-python==4.5.1.48
git clone https://github.com/deepkong/NN_project1_kong.git
cd NN_project1_kong && pip install -e .
```

Donwload [dataset] https://drive.google.com/file/d/1TTFloQwNdg95h-IJceUtVs1WQl_Bu1Ev/view?usp=sharing \
Need to prepare the data root as below
```
NN_project1_kong
├── mmseg
├── tools
├── local_configs
├── data
│   ├── semantic_drone_dataset
│   │   ├── images
│   │   ├── labels
│   │   ├── split
│   │   │   ├── train.txt
│   │   │   ├── val.txt
│   │   │   ├── test.txt
```


## Training
Donwload [pretrained weights] https://drive.google.com/file/d/1VuhtdeQSGl2gxndg_-98HPFJ1qEl3KiH/view?usp=sharing
```
# Single-gpu training
python tools/train.py local_configs/segformer_drone/segformer.b2.512x512.drone.20k.py

# Multi-gpu training
./tools/dist_train.sh local_configs/segformer_drone/segformer.b2.512x512.drone.20k.py <GPU_NUM>
```


## Evaluation
Donwload [weights] https://drive.google.com/file/d/15X00UIMRd3cmFC7sgKiHu5DCRQhM5zik/view?usp=sharing
```
# Single-gpu testing
python tools/test.py local_configs/segformer_drone/segformer.b2.512x512.drone.20k.py /path/to/checkpoint_file --show-dir /path/to/save_file

# Multi-gpu testing
./tools/dist_test.sh local_configs/segformer_drone/segformer.b2.512x512.drone.20k.py /path/to/checkpoint_file <GPU_NUM> --show-dir /path/to/save_file
```
