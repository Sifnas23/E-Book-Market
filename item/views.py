from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from .models import Item, Category

# Searching
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(Name_id=category_id)

    if query:
        items = items.filter(Q(Book_Name=query) | Q(Description=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    item = get_object_or_404(Item, id=pk)
    related_items = Item.objects.filter(Name=item.Name, is_sold=False).exclude(id=pk)[0:6]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    form = NewItemForm()

    return render(request, 'item/form.html',{
        'form': form
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, id=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Edit item'
    })


@login_required
def  delete(request, pk):
    item = get_object_or_404(Item, id=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


