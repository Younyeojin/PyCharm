import matplotlib.pyplot as plt

from common.menu import print_menu


def plot_show():
    plt.plot([10, 20, 30, 40])
    plt.show()


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(['Exit', 'plot Show', 'plot_two_list_show', 'Bugs Output', 'Melon Output', 'Print Dict',
                           'Dict to Dataframe', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()