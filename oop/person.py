'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다. 로 됩니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''

class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.persons = []

    def addPersons(self, person):
        self.persons.append(person)

    def to_String(self, param):
        print(f'안녕하세요. 제 이름은 {param.name}이고, 나이는 {param.age}세이고, {param.address}에서 거주합니다.')


    @staticmethod
    def main():
        count = int(input('How many ? '))
        for i in range(count):
            person = Person(input('name: '), input('age: '), input('address: '))
        for i in ['\nname: ', 'age: ', 'address: ']:
            person.addPersons(input(f'{i}'))
        for i in ['\nname: ', 'age: ', 'address: ']:
            person.to_String(input(f'{i}'))
        # print(f'안녕하세요. 제 이름은 {person.name}이고, 나이는 {person.age}세이고, {person.address}에서 거주합니다.')

Person.main()