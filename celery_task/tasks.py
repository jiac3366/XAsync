from celery import shared_task
import time
from celery_system.settings import MONGO_URL
from app_one.serializer import PersonSerializer
from pymongo import MongoClient


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task(bind=True)
def xsum(self, numbers):
    print(self.priority)
    time.sleep(10)
    return sum(numbers)





@shared_task
def save_ORM():
    data_one = data = {
        'first_name': 'chase',
        'last_name': 'chase',
        'age': 25,
        'school': 'school1',
    }
    ser = PersonSerializer(data=data_one)
    ser.is_valid()
    ser.save()


@shared_task
def save_pymongo():
    data_one = data = {
        'first_name': 'chase',
        'last_name': 'chase',
        'age': 25,
        'school': 'school1',
    }
    with MongoClient(MONGO_URL) as cli:
        clc = cli['mock'].get_collection('app_one_person')
        res = clc.insert_one(data_one)
        print(res)
