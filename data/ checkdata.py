import numpy as np


file_path = '/home/maqingchuan/3Dpose/data/data_2d_humaneva15_gt.npz'

# 加载 npz 文件
data = np.load(file_path)

# 查看文件中包含的所有数组名称
array_names = data.files
print("Array names in the file:", array_names)

# 访问每个数组并打印其内容
for array_name in array_names:
    array_data = data[array_name]
   # print(f"{array_name}:")
    #print(array_data)

# 关闭文件
data.close()