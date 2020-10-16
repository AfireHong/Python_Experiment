import numpy as np
import matplotlib.pyplot as plt
#设置中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 导入数据  ['data', 'feature_names']
data = np.load('populations.npz', allow_pickle=True)
# print(data.files)
name = data['feature_names']
values = data['data'][-3:-23:-1]
print(name)
p = plt.figure(figsize=(12,30))
# 第一幅子图 性别
ax1 = p.add_subplot(3,1,1)
sex_populations = (list(values[:, 2]), list(values[:, 3]))
labels = name[2:4]
plt.boxplot(sex_populations,labels=labels)
# 第二幅子图 城市与农村
ax2 = p.add_subplot(3,1,2)
city_populations = (list(values[:, 4]), list(values[:, 5]))
labels = name[4:6]
plt.boxplot(city_populations,labels=labels)
#第三幅子图 总人口
ax3 = p.add_subplot(3,1,3)
total_populations = (list(values[:, 1]))
labels = name[1:2]
plt.boxplot(total_populations,labels=labels)
plt.show()

