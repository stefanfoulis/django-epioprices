#-*- coding: utf-8 -*-
from .base import *

DEBUG = False

MIDDLEWARE_CLASSES = (
    'project.middleware.HTTPSMiddleware',
) + MIDDLEWARE_CLASSES