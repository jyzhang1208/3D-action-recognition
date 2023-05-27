# -*- coding: utf-8 -*-
import os
import imageio
import numpy as np


# from mayavi import mlab
os.environ['QT_API']='pyqt5'
file_dir = '/home/zjy/3DV-Action/data/Drink/S001C001P001R001A001'
fx = 365.481
fy = 365.481
cx = 257.346
cy = 210.347

voxel_size = 50

def depth_to_pointcloud(depth_im):
	rows,cols = depth_im.shape
	xx,yy = np.meshgrid(range(0,cols), range(0,rows))

	valid = depth_im > 0
	xx = xx[valid]
	yy = yy[valid]
	depth_im = depth_im[valid]

	X = (xx - cx) * depth_im / fx
	Y = (yy - cy) * depth_im / fy
	Z = depth_im
	points3d = np.array([X.flatten(), Y.flatten(), Z.flatten()])
	return points3d

imgNames = os.listdir(file_dir)
imgNames.sort()
n_frame = len(imgNames)

each_frame_points_num = np.zeros(n_frame,dtype = np.int32)
all_frame_points_list = []
i = 0
for png in imgNames[0:n_frame]:
    print(png)
