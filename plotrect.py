import matplotlib.pyplot as plt

# 多行数据
data = [
    [0, 0, 1, 48, 0, 54, 1, 96],
    [1.5, 120, 2.2, 10, 2.5, 65, 3, 80],
    [0, 20, 0.8, 40, 1.5, 10, 2, 60],
    [1, 30, 2.5, 70],
    [0, 60, 1, 20],
    [2.5, 80, 0.6, 10]
]

# 计算行列数
nrows = 3
ncols = 2

# 设置画布大小
fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols*2.5, nrows*2.5))

# 循环绘制每一行矩形
for i in range(len(data)):
    # 获取当前行的数据
    row_data = data[i]
    # 计算当前行绘图所在子图的索引
    row_index = i // ncols
    col_index = i % ncols
    # 创建当前行的子图
    ax = axs[row_index][col_index]
    # 绘制当前行的所有矩形
    for j in range(0, len(row_data), 4):
        x = row_data[j]
        y = row_data[j+1]
        width = row_data[j+2]
        height = row_data[j+3]
        color = 'blue' if j//4 % 2 == 0 else 'red'
        rect = plt.Rectangle((x, y), width, height, color=color)
        ax.add_patch(rect)
    # 为当前行设置x、y轴范围和标题
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 150)
    ax.set_title(f"Row {i+1}")

# 调整子图间距
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# 显示图形
plt.show()
