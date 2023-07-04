import numpy as np

file_dir = '/home/zjy/3DV-Action/3DV_pointdata/NTU_voxelsize35_split5'
test=np.load('/home/zjy/3DV-Action/3DV_pointdata/NTU_voxelsize35_split5/S001C001P001R001A001.npy')
print(test.shape)

test1=np.load('/home/zjy/3DV-Action/NTU_3seg_depthpoint/Seg1/NTU_v1/S001C001P001R001A001_v1.npy')
print(test1.shape)

