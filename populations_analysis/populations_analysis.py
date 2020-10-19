import numpy as np
import matplotlib.pyplot as plt
#设置中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 导入数据  ['data', 'feature_names']
data = np.load('populations.npz', allow_pickle=True)
# print(data.files)
name = data['feature_names']
# 切片
values = data['data'][-3:-23:-1]
print(values[-3:-23:-1])
print(name)
# 创建图
p = plt.figure(figsize=(20, 10))
ax1 = p.add_subplot(1, 2, 1)
plt.xlabel(name[0])
plt.ylabel(name[1])
plt.xticks(range(20), values[:, 0])
# 总人口
plt.plot(range(20), values[:, 1], color='r', linestyle='--')
# 城镇人口
plt.plot(range(20), values[:, 4], color='b', linestyle='-')
# 农村人口
plt.plot(range(20), values[:, 5], color='g', linestyle='-.')
# 男性人口
plt.plot(range(20), values[:, 2], color='k', linestyle=':')
# 女性人口
plt.plot(range(20), values[:, 3], color='y', linestyle='-')
plt.legend(['年末总人口（万人）', '城镇人口（万人）', '农村人口（万人）', '男性人口（万人）', '女性人口（万人）'])
plt.savefig('1996~2015年末人口分布特征折线图.png', dpi=400, bbox_inches='tight')
ax1 = p.add_subplot(1, 2, 2)
plt.scatter(range(20), values[:, 1], marker='8', color='red')
plt.scatter(range(20), values[:, 4], marker='o', color='black')
plt.scatter(range(20), values[:, 5], marker='D', color='green')
plt.scatter(range(20), values[:, 2], marker='h', color='blue')
plt.scatter(range(20), values[:, 3], marker='.', color='yellow')
plt.xticks(range(20), values[:, 0])
plt.xlabel(name[0])
plt.ylabel(name[1])
plt.title('1996~2015年末人口分布特征散点图')
plt.legend(['年末总人口（万人）', '城镇人口（万人）', '农村人口（万人）', '男性人口（万人）', '女性人口（万人）'])
plt.savefig('1996~2015年末人口分布特征散点图.png', dpi=400, bbox_inches='tight')
plt.show()

