from celery import shared_task
import time
from app_one.models import Person


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
def person():
    obj = Person.objects.create(first_name='chase', last_name='chen')
    obj.save()
