from celery import shared_task
from app_one.serializer import PersonSerializer


@shared_task
def add(x, y):
    return x + y


@shared_task
def test_serializer():
    data = {"first_name": "chase2", "last_name": "chen2"}
    ser = PersonSerializer(data=data)
    ser.is_valid(raise_exception=True)
    ser.save()
    print(ser.data)
