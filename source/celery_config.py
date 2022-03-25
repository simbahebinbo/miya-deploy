# coding=utf-8
from datetime import timedelta

from kombu import Queue

CELERY_TASK_RESULT_EXPIRES = 60 * 5  # 指定任务结果的过期时间

CELERY_DEFAULT_QUEUE = 'mytask0'
CELERY_QUEUES = (
    Queue('mytask0', routing_key='celery_tasks.mytask0'),
    Queue('mytask1', routing_key='celery_tasks.mytask1'),
)

CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'celery_tasks.mytask0'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ROUTES = {
    'celery_tasks.mytask0': {
        'queue': 'mytask0',
        'routing_key': 'celery_tasks.mytask0',
    },
    'celery_tasks.mytask1': {
        'queue': 'mytask1',
        'routing_key': 'celery_tasks.mytask1',
    },
}

CELERY_TASK_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = False
CELERYBEAT_SCHEDULE = {
    # 用于调试的任务,每隔一段时间执行一次
    'hello-every': {
        'task': 'celery_tasks.hello',
        'schedule': timedelta(seconds=10),
        'args': ('Hello World',)
    }
}
