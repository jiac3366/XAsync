
from celery import shared_task


@shared_task()
def fund_transfer_send(x, y):
    return x + y