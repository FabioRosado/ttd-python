"""To-Do Lists views"""

from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """Base view for the homepage"""
    return render(request, 'home.html')


def view_list(request):
    """A view for each individual todo list"""
    items = Item.objects.all()
    return render(request, 'lists.html', {'items': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
