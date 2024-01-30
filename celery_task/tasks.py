from celery import shared_task
import time


@shared_task(bind=True)
def tasks_sleep(self, priority: int):
    num = 20
    for i in range(num):
        print(f"tasks_sleep params priority:{priority}, {i}")
        time.sleep(1)
