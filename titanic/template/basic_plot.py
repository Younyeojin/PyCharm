import matplotlib.pyplot as plt

from common.menu import print_menu

"""
list 값은 y축 이고, x축은 0부터 1까지 자동으로 증가한다.
"""


def plot_show():
    plt.title('plotting')
    plt.plot([10, 20, 30, 40])
    plt.show()


"""
첫번째 list 가 x축 이고, 두번째 list 가 y축 이다.
"""


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


def plot_legend():
    plt.title('legend')
    plt.plot([10, 20, 30, 40], label='asc')
    plt.plot([40, 30, 20, 10], label='desc')
    plt.legend()
    plt.show()


def plot_change_color():
    plt.title('color')
    plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
    plt.plot([40, 30, 20, 10], 'pink', label='pink')
    plt.legend()
    plt.show()


def plot_line_style():
    plt.title('linestyle')
    plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
    plt.plot([40, 30, 20, 10], color='g', ls=':', label='dotted')
    plt.legend()
    plt.show()


def plot_marker():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(['Exit', 'plot Show', 'plot_two_list_show', 'plot_legend', 'plot_change_color', 'plot_line_style',
                           'plot_marker', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_legend()
        elif menu == 4:
            plot_change_color()
        elif menu == 5:
            plot_line_style()
        elif menu == 6:
            plot_marker()
