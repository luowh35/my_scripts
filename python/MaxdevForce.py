import numpy as np
import matplotlib.pyplot as plt

# 读取文本文件
filename = "Max_Devi_F"
data = np.loadtxt(filename)

# 获取数据列数
num_columns = data.shape[1]

# 绘制图像
fig, ax = plt.subplots(figsize=(8,4))

# 颜色循环
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

# 循环绘制每一列的拟合曲线
for i in range(num_columns):
    # 计算频次
    counts, bins = np.histogram(data[:, i], bins='auto', density=True)
    
    # 拟合曲线
    mu, sigma = np.mean(data[:, i]), np.std(data[:, i])
    best_fit_line = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2))
    
    # 绘制拟合曲线
    ax.plot(bins, best_fit_line, color=color_cycle[i % len(color_cycle)], label='Column {}'.format(i+1))

# 设置图例和坐标轴标签
ax.legend(loc='upper right', fontsize=12)
ax.set_xlabel('Max deviation of force (eV/$\AA$)', fontsize=16)
ax.set_ylabel('Probability Density', fontsize=16)

# 设置图形边界和标签位置
plt.tight_layout() #自动调整图形的边界，使得所有元素都能够正常显示在图像中。

# 显示图像
#plt.show()
plt.savefig('Max_Devi_F.png', dpi=300)
