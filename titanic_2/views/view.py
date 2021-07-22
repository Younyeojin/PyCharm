from titanic_2.modle.dataset import Dataset
from titanic_2.modle.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        this = self.preprocessing(train, test)
        print(f'The Type of This is {type(this.train)}')
        print(f'The head of Train is \n {this.train.head(2)}')
