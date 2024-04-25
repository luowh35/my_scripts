import matplotlib.pyplot as plt
import math

x1, x2, x3, xt = [], [], [], []
y4, y5, y6, yt = [], [], [], []
with open('DP_DFT_000.f.out', 'r') as f:
    for line in f:
        if line.startswith('#'):  # 跳过以#开头的注释语句
            continue
        data = line.split()
        x1.append(float(data[0]))
        x2.append(float(data[1]))
        x3.append(float(data[2]))
        xt.append(float(data[0]) + float(data[1]) + float(data[2]))

        y4.append(float(data[3]))
        y5.append(float(data[4]))
        y6.append(float(data[5]))
        yt.append(float(data[3]) + float(data[4]) + float(data[5]))
		
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
fig.subplots_adjust(hspace=0.3, wspace=0.3) #可以使将子图之间的水平和垂直间距设置为0.5（以子图高度和宽度的百分比表示）

# 绘制子图a
axs[0, 0].scatter(x1, x1, c='red', marker='o', label='DFT_${f_x}$', s=10)
axs[0, 0].scatter(x1, y4, c='blue', marker='^', label='DP_${f_x}$', s=10)
axs[0, 0].plot([-(math.floor(max(x1) + 1)), math.floor(max(x1) + 1)], [-(math.floor(max(x1) + 1)), math.floor(max(x1) + 1)], c='green', linestyle='solid', label='DFT=DP')
axs[0, 0].set_xlim(-(math.floor(max(x1) + 1)), math.floor(max(x1) + 1))
axs[0, 0].set_ylim(-(math.floor(max(x1) + 1)), math.floor(max(x1) + 1))
axs[0, 0].legend(loc='upper left')
n = len(y4)
sum_squares = sum([(y4[i] - x1[i]) ** 2 for i in range(n)])
rmse = math.sqrt(sum_squares / n)
axs[0, 0].text(0.75, 0.17, f'Test points = {n}', ha='right', va='top', transform=axs[0, 0].transAxes)
axs[0, 0].text(0.75, 0.1, f'RMSE = {rmse:.4f} eV/$\AA$', ha='right', va='top', transform=axs[0, 0].transAxes)
axs[0, 0].set_xlabel('DFT_${f_x}$ (eV/$\AA$)')
axs[0, 0].set_ylabel('DP_${f_x}$ (eV/$\AA$)')

# 绘制子图b
axs[0, 1].scatter(x2, x2, c='red', marker='o', label='DFT_${f_y}$', s=10)
axs[0, 1].scatter(x2, y5, c='blue', marker='^', label='DP_${f_y}$', s=10)
axs[0, 1].plot([-(math.floor(max(x2)+1)), math.floor(max(x2)+1)], [-(math.floor(max(x2)+1)), math.floor(max(x2)+1)], c='green', linestyle='solid', label='DFT=DP')
axs[0, 1].set_xlim(-(math.floor(max(x2)+1)), math.floor(max(x2)+1))
axs[0, 1].set_ylim(-(math.floor(max(x2)+1)), math.floor(max(x2)+1))
axs[0, 1].legend(loc='upper left')
n = len(y5)
sum_squares = sum([(y5[i] - x2[i]) ** 2 for i in range(n)])
rmse = math.sqrt(sum_squares / n)
axs[0, 1].text(0.75, 0.17, f'Test points = {n}', ha='right', va='top', transform=axs[0, 1].transAxes)
axs[0, 1].text(0.75, 0.1, f'RMSE = {rmse:.4f} eV/$\AA$', ha='right', va='top', transform=axs[0, 1].transAxes)
axs[0, 1].set_xlabel('DFT_${f_y}$ (eV/$\AA$)')
axs[0, 1].set_ylabel('DP_${f_y}$ (eV/$\AA$)')
#绘制子图c
axs[1, 0].scatter(x3, x3, c='red', marker='o', label='DFT_${f_z}$', s=10)
axs[1, 0].scatter(x3, y6, c='blue', marker='^', label='DP_${f_z}$', s=10)
axs[1, 0].plot([-(math.floor(max(x3)+1)), math.floor(max(x3)+1)], [-(math.floor(max(x3)+1)), math.floor(max(x3)+1)], c='green', linestyle='solid', label='DFT=DP')
axs[1, 0].set_xlim(-(math.floor(max(x3)+1)), math.floor(max(x3)+1))
axs[1, 0].set_ylim(-(math.floor(max(x3)+1)), math.floor(max(x3)+1))
axs[1, 0].legend(loc='upper left')
n = len(y6)
sum_squares = sum([(y6[i] - x3[i]) ** 2 for i in range(n)])
rmse = math.sqrt(sum_squares / n)
axs[1, 0].text(0.75, 0.17, f'Test points = {n}', ha='right', va='top', transform=axs[1, 0].transAxes)
axs[1, 0].text(0.75, 0.1, f'RMSE = {rmse:.4f} eV/$\AA$', ha='right', va='top', transform=axs[1, 0].transAxes)
axs[1, 0].set_xlabel('DFT_${f_z}$ (eV/$\AA$)')
axs[1, 0].set_ylabel('DP_${f_z}$ (eV/$\AA$)')
# 绘制子图d
axs[1, 1].scatter(xt, xt, c='red', marker='o', label='DFT_$f$', s=10)
axs[1, 1].scatter(xt, yt, c='blue', marker='^', label='DP_$f$', s=10)
axs[1, 1].set_xlim(-(math.floor(max(xt)+1)), math.floor(max(x1)+1))
axs[1, 1].set_ylim(-(math.floor(max(yt)+1)), math.floor(max(yt)+1))
axs[1, 1].plot([-(math.floor(max(xt)+1)), math.floor(max(xt)+1)], [-(math.floor(max(xt)+1)), math.floor(max(xt)+1)], c='green', linestyle='solid', label='DFT=DP')
axs[1, 1].set_xlim(-(math.floor(max(xt)+1)), math.floor(max(xt)+1))
axs[1, 1].set_ylim(-(math.floor(max(xt)+1)), math.floor(max(xt)+1))
axs[1, 1].legend(loc='upper left')
n = len(yt)
sum_squares = sum([(yt[i] - xt[i]) ** 2 for i in range(n)])
rmse = math.sqrt(sum_squares / n)
axs[1, 1].text(0.75, 0.17, f'Test points = {n}', ha='right', va='top', transform=axs[1, 1].transAxes)
axs[1, 1].text(0.75, 0.1, f'RMSE = {rmse:.4f} eV/$\AA$', ha='right', va='top', transform=axs[1, 1].transAxes)
axs[1, 1].set_xlabel('DFT_${f}$ (eV/$\AA$)')
axs[1, 1].set_ylabel('DP_${f}$ (eV/$\AA$)')
# 显示图形
# plt.show()

#保存图片，可以选择PDF格式
plt.savefig('RMSE.png', dpi=300)
