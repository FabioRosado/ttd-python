"""Django Models"""

from django.db import models


class List(models.Model):
    """Model for a To-Do List"""
    pass


class Item(models.Model):
    """To-Do List Item"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
