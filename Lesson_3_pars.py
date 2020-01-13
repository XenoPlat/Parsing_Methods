import pandas as pd
from pprint import pprint
from pymongo import MongoClient

#Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и
# реализовать функцию, записывающую собранные вакансии в созданную БД

# Загружаем напарсенное нами из файла .csv
data = pd.read_csv("vac.csv", sep=';')

# снова превращаем в словарь то, что достали из файла
data_dict = data.to_dict('r')

# запускаем базу данных Монго
client = MongoClient('localhost', 27017)

# создаём новую БД и коллекцию
db = client['jobs']
vacancies = db.vacancies

# вносим в БД весь словарь
db.vacancies.insert_many(data_dict)


# Написать функцию, которая производит поиск и выводит на экран вакансии с
# заработной платой больше введенной суммы
# функция принимает на вход название коллекции и желаемый уровень зарплаты
def extract_vacancies(collection, salary_level):
    objects = collection.find({'salary_from': {'$gt': salary_level}})
    for obj in objects:
        pprint(obj)

# достаём вакансии с зарплатой не ниже определённой
extract_vacancies(vacancies, 130000)