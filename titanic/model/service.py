from titanic.model.dataset import Dataset
import pandas as pd


class Service(object):
    dataset = Dataset()

    def new_model(self, payload: str) -> object:                   # payload : 사용에 있어 전송되는 데이터(전송의 근본적인 목적)
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


def creatr_train(this) -> str:
    return this

def drop_feature(this, *feature) -> str:
    return this

def embarked_nominal(this) -> str:
    return this

def fare_oridnal(this) -> str:
    return this

def title_nominal(this) -> str:
    return this

def gender_norminal(this) -> str:
    return this

def age_ordinal(this) -> str:
    return this

def create_k_fold() -> object:
    return None

def accuracy_by_classfier(this) -> str:
    return ""