from celery import shared_task


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
