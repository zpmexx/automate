from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemModel
from django.contrib import messages
from .forms import AddItemForm

def main(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id:
            obj = get_object_or_404(ItemModel, id=item_id)
            obj.status = 1
            obj.save()
            return redirect('main')  
    items = ItemModel.objects.filter(status = 0)
    context = {'items' : items}
    return render(request, 'xkom/main.html', context)


def addItem(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Przedmiot dodany do bazy.', extra_tags='add_item')
        else:
            messages.warning(request,'Problem z zapisaniem przedmiotu.', extra_tags='add_item_fail')
    context = {'form':form}
    return render (request, 'xkom/addItem.html',context)