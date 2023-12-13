# Vision Transformer for NeRF-Based View Synthesis from a Single Input Image
This code is adapted from ```git clone https://github.com/ken2576/vision-nerf.git``` and necessary changes are made for this to work.
Changes are Made:
1. train.py
2. extract_camera.py is custom function written for our use case
3. Changes are made in gen_real
4. Notebooks are used for visualization and as per requirements
### Visualizations are in Notebooks
### Install required packages

Make sure you have up-to-date NVIDIA drivers supporting CUDA 11.1 (10.2 could work but need to change `cudatoolkit` package accordingly)

Run

```
conda env create -f environment.yml
conda activate visionnerf
```
## Download 
Download weights, experiment and train_eiffel from ```https://drive.google.com/drive/folders/1mkgUmntorocDBC3EY4TOS5fciKvvva7j?usp=sharing```

## Usage



1. Install requirements ```conda env create -f environment.yml```.

2. Setup configurations in ```configs```.

3. (Optional) Run training script with ```python train.py --config [config_path]```.

4. Pretrained weights are in   ```weights/nmr_500000.pth``` and trained in ```/weights/image/model_500500.pth``
5. ```train_eiffel/``` contains the view used for training eiffel and for testing everything is inside  ```experiment/```
6. Run inference script 
```
python gen_real.py --config [path to config file] 

```


## Acknowledgement

This code is based on[VisionNERF](https://github.com/ken2576/vision-nerf), [DPT](https://github.com/isl-org/DPT), [IBRNet](https://github.com/googleinterns/IBRNet) and [PixelNeRF](https://github.com/sxyu/pixel-nerf).


