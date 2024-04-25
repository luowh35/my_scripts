import matplotlib.pyplot as plt

x1 = []
y1 = []
x2 = []
y2 = []

with open('lcurve.out') as f:
    for line in f:
        if not line.startswith('#'): # 忽略注释行
            data = line.split()
            x1.append(float(data[0]))
            y1.append(float(data[2]))
            y2.append(float(data[3]))
            x2.append(float(data[0]))

plt.plot(x1, y1, color='red', label='RMSE for energy(Units: meV/atom)') # 第一条折线，红色实线
plt.plot(x2, y2, color='blue', linestyle='-', label='RMSE for forces(Units: eV/$\AA$)') # 第二条折线，蓝色破折线'--'
plt.xlabel('Steps')
plt.ylabel('RMSE for train')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0)) # 设置横轴为科学计数法
plt.legend() # 显示图例
# 显示图形
# plt.show()

#保存图片，可以选择PDF格式
plt.savefig('learn-rate.png', dpi=300)

