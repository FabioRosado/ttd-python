"""To-Do Lists views"""

from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """Base view for the homepage"""
    return render(request, 'home.html')


def view_list(request, list_id):
    """A view for each individual todo list"""
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists.html', {'list': list_})


def new_list(request):
    """Create new todo list"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


def add_item(request, list_id):
    """ Adds new item to list"""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
