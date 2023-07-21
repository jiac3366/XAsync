# Celery System Demo


### Run command
    
- #### Celery Worker

    - window: celery -A celery_task worker -l INFO -P eventlet
    - linux: celery -A celery_task worker -l INFO

- #### Celery Client

    - python manage.py shell
    - from celery_task.tasks3 import test_serializer
    - test_serializer.delay()

#### Stack

- pymongo==3.12.0