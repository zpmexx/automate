from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemModel
from django.contrib import messages
from .forms import AddItemForm

def main(request):
    
    search_query = request.GET.get('search_query', '')
    if search_query:
        items = ItemModel.objects.filter(name__icontains=search_query)
        context = {'items' : items}
        return render(request, 'xkom/main.html', context)

    else:
        if request.method == 'POST':
            for key in request.POST:
                if key.startswith('price'):
                    _, item_id = key.split('_')
                    price = request.POST.get(key)
                    if item_id:
                        obj = get_object_or_404(ItemModel, id=item_id)
                        obj.target_price = price
                        obj.save()
                        return redirect('main')
                elif key.startswith('deactivate'):
                    print(key)
                    _, item_id = key.split('_')
                    print(item_id)
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
        form = AddItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = AddItemForm()
            messages.success(request,'Przedmiot dodany do bazy.', extra_tags='add_item')
        else:
            messages.warning(request,'Problem z zapisaniem przedmiotu.', extra_tags='add_item_fail')
    context = {'form':form}
    return render (request, 'xkom/addItem.html',context)


def test(request):
    search_query = request.GET.get('search_query', '')
    if search_query:
        items = ItemModel.objects.filter(name__icontains=search_query)
        context = {'items' : items}
        return render(request, 'xkom/main.html', context)

    else:
        if request.method == 'POST':
            for key in request.POST:
                if key.startswith('price'):
                    _, item_id = key.split('_')
                    price = request.POST.get(key)
                    if item_id:
                        obj = get_object_or_404(ItemModel, id=item_id)
                        obj.target_price = price
                        obj.save()
                        return redirect('main')
                elif key.startswith('deactivate'):
                    print(key)
                    _, item_id = key.split('_')
                    print(item_id)
                    if item_id:
                        obj = get_object_or_404(ItemModel, id=item_id)
                        obj.status = 1
                        obj.save()
                        return redirect('main') 
    
        items = ItemModel.objects.filter(status = 0)
        context = {'items' : items}
        return render(request, 'xkom/test.html', context)