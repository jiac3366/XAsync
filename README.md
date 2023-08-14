# Celery System Demo


### Run command
    
- #### Celery Worker
    - window: celery -A celery_task worker -l INFO -P eventlet
    - linux: celery -A celery_task worker -l INFO

- #### Celery Client Send Task

    - python manage.py shell
    - from celery_task.tasks3 import test_serializer
    - test_serializer.delay()
  
- #### Test djongo vs pymongo
    - from celery_task.tasks import save_pymongo, save_ORM


#### Stack
- python=3.8.10
- Django==3.2.15
- djongo==1.3.6
- celery==5.2.7
- kombu==5.2.4
- django-celery-beat==2.3.0
- pymongo==3.12.0

- Faker==19.3.0

- MongoDB Version: 4.4.12
- 