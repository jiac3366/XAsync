import datetime
from celery import shared_task
import time
import bson
from celery_system.settings import MONGO_URL
from app_one.models import Person
from pymongo import MongoClient

"""
author: chase
time: 2023-08-11
"""


def generate_mock_data(num_records: int, is_pymongo: bool = False):
    # {'first_name': 'Courtney', 'last_name': 'Lewis', 'age': 58, 'school': 'Taylor-Miller'}
    # {'first_name': 'Katherine', 'last_name': 'Frazier', 'age': 39, 'school': 'Tanner, Bradshaw and Manning'}
    # {'first_name': 'Matthew', 'last_name': 'Lopez', 'age': 43, 'school': 'Ross and Sons'}
    import random
    from faker import Faker
    faker = Faker()

    mock_data = []
    for _ in range(num_records):
        first_name = faker.first_name()
        last_name = faker.last_name()
        age = random.randint(18, 60)
        school = faker.company()
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'school': school
        }
        if is_pymongo:
            data.update({
                'is_archived': False,
                'datetime': datetime.datetime.utcnow(),
                'update_time': datetime.datetime.utcnow(),
            })
        mock_data.append(data)
    return mock_data


@shared_task
def save_ORM(num_records: int, bulk_write: bool = False):
    datas = generate_mock_data(num_records)
    print(f'save {num_records} records by ORM with bulk_write={bulk_write}')

    time1 = time.time()
    if bulk_write:
        res = [Person(_id=bson.ObjectId(), **data) for data in datas]
        Person.objects.bulk_create(res)
    else:
        for data in datas:
            Person.objects.create(**data)
    time_cost = time.time() - time1
    print(f'save by ORM costs: {time_cost:.4f} seconds.')


@shared_task
def save_pymongo(num_records: int, bulk_write: bool = False):
    datas = generate_mock_data(num_records, is_pymongo=True)
    print(f'save {num_records} records by pymongo with bulk_write={bulk_write}')

    time1 = time.time()
    with MongoClient(MONGO_URL) as cli:
        clc = cli['mock'].get_collection('app_one_person')
        if bulk_write:
            clc.insert_many(datas)
        else:
            for data in datas:
                clc.insert_one(data)
    time_cost = time.time() - time1
    print(f'save by pymongo costs: {time_cost:.4f} seconds.')
