"""To-Do Lists views"""

from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    """Base view for the homepage"""
    return render(request, 'home.html')


def view_list(request):
    """A view for each individual todo list"""
    items = Item.objects.all()
    return render(request, 'lists.html', {'items': items})


def new_list(request):
    return redirect('/lists/the-only-list-in-the-world/')
