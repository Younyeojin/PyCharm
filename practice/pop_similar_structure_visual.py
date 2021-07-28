import csv
import matplotlib.pyplot as plt
import numpy as np


class Similar(object):

    data: [] = list()
    name: str = ''
    home = []

    def read_data(self):
        data = csv.reader(open('../modu/template/data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        self.data = data

    def curious_pop(self) -> []:
        home = self.home
        self.name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ')
        [home.append(int(i)) for i in self.data if self.name in i[0] for i in i[3:]]
        # [print(i) for i in home]
        # return home

    def np_pop(self):
        name = self.name
        for i in self.data:
            if name in i[0]:
                self.home = np.array(i[3:], dtype=int)
        print(self.home)
        # return home

    def show_plot(self):
        plt.rc('font', family='Malgun Gothic')
        plt.title(self.name+'지역의 인구구조')
        plt.plot(self.home)
        plt.show()


if __name__ == '__main__':
    sim = Similar()
    sim.read_data()
    # sim.curious_pop()
    # sim.np_pop(sim.curious_pop())
    sim.np_pop()
    # sim.show_plot(sim.np_pop())
