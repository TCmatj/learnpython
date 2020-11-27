import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
                cmap='pink',edgecolor='none',s=1)
    # 突出始终
    # plt.scatter(0,0,c='green',edgecolor='none',s=50)
    # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolor='none',s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make anothor walk?(y/n):")
    if keep_running == 'n':
        break