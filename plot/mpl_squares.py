import matplotlib.pyplot as plt

input_values = list(range(1000))
squares = [x*x for x in input_values]
##plt.plot(input_values,squares,linewidth=0.5)
plt.scatter(input_values,squares,edgecolor='none',c=squares,cmap=plt.cm.Blues,s=40)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,1000,0,1000000])

plt.show()