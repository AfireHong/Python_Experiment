import numpy as np
import matplotlib.pyplot as plt
#设置中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 导入数据  ['data', 'feature_names']
data = np.load('populations.npz', allow_pickle=True)
# print(data.files)
name = data['feature_names']
# 将数据切片
values = data['data'][-3:-23:-1]
print(name)
print(values)
# 创建箱线图画布
p = plt.figure(figsize=(20,20))
# 第一幅子图 性别
ax1 = p.add_subplot(2, 2, 1)
sex_populations = (list(values[:, 2]), list(values[:, 3]))
labels = name[2:4]
plt.title('1996年-2015年人口性别箱线图')
plt.boxplot(sex_populations, notch=True, labels=labels, meanline=True)
# 第二幅子图 城乡
ax2 = p.add_subplot(2, 2, 2)
city_populations = (list(values[:, 4]), list(values[:, 5]))
labels = name[4:6]
plt.title('1996年-2015年城乡人口箱线图')
plt.boxplot(city_populations, notch=True, labels=labels, meanline=True)
# 第三幅子图 总人口
ax3 = p.add_subplot(2, 2, 3)
total_populations = (list(values[:, 1]))
labels = name[1:2]
plt.title('1996年-2015年总人口箱线图')
plt.boxplot(total_populations, notch=True, labels=labels, meanline=True)
plt.savefig('1996-2015人口箱线图.png', dpi=400, bbox_inches='tight')

# 创建直方图画布
p = plt.figure(figsize=(30,20))
ax4 = p.add_subplot(2, 1, 1)
plt.xlabel(name[0])
plt.ylabel('人口数量')
plt.xticks(np.arange(20) + 0.1, values[:, 0])
# 男性人口
plt.bar(np.arange(20), values[:, 2], width=0.2, color='g')
# 女性人口
plt.bar(np.arange(20)+0.2, values[:, 3], width=0.2, color='c')
plt.legend(name[2:4], loc='upper left')
plt.title('1996年-2015年人口性别直方图')

ax5 = p.add_subplot(2, 1, 2)
plt.xlabel(name[0])
plt.ylabel('人口数量')
plt.xticks(np.arange(20) + 0.1, values[:, 0])
# 城镇人口
plt.bar(np.arange(20), values[:, 4], width=0.2, color='g')
# 农村人口
plt.bar(np.arange(20)+0.2, values[:, 5], width=0.2, color='c')
plt.legend(name[4:6], loc='upper left')
plt.title('1996年-2015年城乡人口直方图')
plt.savefig('1996-2015人口直方图.png', dpi=400, bbox_inches='tight')

# 创建饼状图画布
ex = [0.01, 0.01]
p = plt.figure(figsize=(20, 20))
ax6 = p.add_subplot(2, 2, 1)
plt.pie(values[0, 2:4], labels=name[2:4], explode=ex, colors=['pink', 'crimson'], autopct='%1.1f%%')
plt.title('1996年男女人口饼状图')

ax7 = p.add_subplot(2, 2, 2)
plt.pie(values[0, 4:6], labels=name[2:4], explode=ex, colors=['pink', 'crimson'], autopct='%1.1f%%')
plt.title('1996年城乡人口饼状图')

ax8 = p.add_subplot(2, 2, 3)
plt.pie(values[-1, 2:4], labels=name[2:4], explode=ex, colors=['pink', 'crimson'], autopct='%1.1f%%')
plt.title('2015年男女人口饼状图')

ax9 = p.add_subplot(2, 2, 4)
plt.pie(values[-1, 4:6], labels=name[2:4], explode=ex, colors=['pink', 'crimson'], autopct='%1.1f%%')
plt.title('2015年城乡人口饼状图')
plt.savefig('1996-2015人口饼状图.png', dpi=400, bbox_inches='tight')