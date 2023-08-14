import os
from celery_system import settings
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_system.settings')

app = Celery('chase_celery1')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(settings.TASK_PACKAGES)
# for redis: 0 being highest priority.
app.conf.broker_transport_options = {
    'priority_steps': list(range(1, 4)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}
app.conf.worker_prefetch_multiplier = 1

# app.conf.task_routes = {
#     'celery_task.tasks.*': {'queue': 'celery:1'},
#     'celery_task.tasks2.*': {'queue': 'celery:2'},
#     'celery_task.tasks3.*': {'queue': 'celery:3'},
# }

# from kombu import Queue
#
# # 优先级队列方案
# app.conf.task_queues = (
#     Queue('default', routing_key='task.#'),
#     Queue('feed_tasks', routing_key='feed.#'),
# )

# 定义队列的routing key
# 重写一下 任务对象的代码  routing_key
#

# from kombu import Exchange, Queue, binding
# from celery.schedules import crontab
#
# #
# # # app.conf.task_queues == CELERY_QUEUES
# app.conf.task_queues = (
#     Queue('celery:1', routing_key="high"),
#     Queue('celery:2', routing_key="default"),
#     Queue('celery:3', routing_key="low"),
# )
# app.conf.task_default_routing_key = 'default'
# # app.conf.task_default_queue = 'default'
# # app.conf.task_default_exchange = 'default'
#
# app.conf.beat_schedule = {
#     'test-task': {
#         'task': 'celery_task.tasks.xsum',
#         'schedule': crontab(minute='*/1')
#     },
# }