"""Django Models"""

from django.db import models


class Item(models.Model):
    """To-Do List Item"""
    text = models.TextField(default='')
