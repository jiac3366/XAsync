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

# app.conf.task_routes = {
#     'celery_task.fund_transfer.tasks.t1.*': {'queue': 'fund_transfer'},
#     'celery_task.tasks.*': {'queue': 'celery'},
# }


from kombu import Queue

# app.conf.task_queues = (
#     Queue('celery',   routing_key='celery'),
#     Queue('fund_transfer', routing_key='fund_transfer'),
# )

# queue只能指定的是队列名，例如：celery，而非celery:1
# task_routes的key匹配的是shared_task中的name
app.conf.task_routes = {
    'fund_transfer.*': {'queue': 'fund_transfer'},
    'celery_task.tasks.*': {'queue': 'celery'},
}


app.conf.broker_transport_options = {
    'priority_steps': list(range(1, 4)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}
app.conf.worker_prefetch_multiplier = 1

