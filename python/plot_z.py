import matplotlib.pyplot as plt

# 示例数据
categories = ['0','20','40','60','80']
values = [252,216,236,306,228]

# 创建柱状图
plt.bar(categories, values, color='blue')

# 添加标题和标签
plt.title('nvt Evaporation flux comparison')
plt.xlabel('')
plt.ylabel('Evaporation rate(mol/m^2s)')

# 显示图形
plt.show()
plt.savefig('bar_chart.png')
