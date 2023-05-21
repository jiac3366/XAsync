from celery import shared_task
import time


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
