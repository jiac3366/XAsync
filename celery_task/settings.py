from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = ""
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database': 'chase_test_db',
    'taskmeta_collection': 'chase_test_2',
}

CELERY_TASK_TRACK_STARTED = True
TASK_PACKAGES = [
    'celery_task.tasks',
    'celery_task.tasks2',
    'celery_task.tasks3',
]
