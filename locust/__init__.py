'''
Author:EricLiu
modify: 2017-05-28
'''
from .core import HttpLocust, Locust, TaskSet, task
from .exception import InterruptTaskSet, ResponseError, RescheduleTaskImmediately

__version__ = "0.8a2"
