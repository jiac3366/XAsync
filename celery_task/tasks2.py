from celery import shared_task
import time


@shared_task
def tasks2_sleep():
    num = 10
    for i in range(num):
        print(f"tasks2_sleep {i}")
        time.sleep(1)