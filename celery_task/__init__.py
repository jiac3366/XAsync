from celery_system.celery import app as celery_app
from .hooks import *

__all__ = ('celery_app',)
