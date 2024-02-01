
from celery import shared_task


@shared_task(name="fund_transfer.fund_transfer_send")
def fund_transfer_send(x, y):
    return x + y