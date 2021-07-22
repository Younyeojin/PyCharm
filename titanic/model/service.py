from titanic.model.dataset import Dataset
import pandas as pd


class Service(object):
    dataset = Dataset()

    def new_model(self, payload):                   # payload : 사용에 있어 전송되는 데이터(전송의 근본적인 목적)
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

