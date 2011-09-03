#-*- coding: utf-8 -*-
from .base import *

MIDDLEWARE_CLASSES = (
    'project.middleware.HTTPSMiddleware',
) + MIDDLEWARE_CLASSES