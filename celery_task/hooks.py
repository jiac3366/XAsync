from celery.signals import after_task_publish, celeryd_init


@after_task_publish.connect
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2.
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(
        info=info,
    ))


@celeryd_init.connect
def celeryd_init(sender=None, conf=None, **kwargs):
    print(f'celeryd_init: sender={sender}')
