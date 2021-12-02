import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset



@DATASETS.register_module()
class DroneDataset(CustomDataset):
    """ Drone dataset """

    CLASSES = ('unlabeled', 'paved-area', 'dirt', 'grass', 'gravel',
               'water', 'rocks', 'pool', 'vegetation', 'roof',
               'wall', 'window', 'door', 'fence', 'fence-pole',
               'person', 'dog', 'car', 'bicycle', 'tree',
               'bald-tree', 'ar-marker', 'obstacle', 'conflicting')

    PALETTE = [[0, 0, 0], [128, 64, 128], [130, 76, 0], [0, 102, 0], [112, 103, 87],
               [28, 42, 168], [48, 41, 30], [0, 50, 89], [107, 142, 35], [70, 70, 70],
               [102, 102, 156], [254, 228, 12], [254, 148, 12], [190, 153, 153], [153, 153, 153],
               [255, 22, 96], [102, 51, 0], [9, 143, 150], [119, 11, 32], [51, 51, 0],
               [190, 250, 190], [112, 150, 146], [2, 135, 115], [255, 0, 0]]


    def __init__(self, split, **kwargs):       
        super(DroneDataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', split=split, **kwargs)
        assert osp.exists(self.img_dir) and self.split is not None
