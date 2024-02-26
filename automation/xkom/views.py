from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemModel
from django.contrib import messages
from .forms import AddItemForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    if request.method == 'POST':
            print("post z main")
            print(request.POST)
            for key in request.POST:
                print("essa")
                print(key)
                if key.startswith('price'):
                    print("price")
                    _, item_id = key.split('_')
                    price = request.POST.get(key)
                    if item_id:
                        obj = get_object_or_404(ItemModel, id=item_id)
                        obj.target_price = price
                        obj.save()
                elif key.startswith('deactivate'):
                    print(key)
                    _, item_id = key.split('_')
                    print(item_id)
                    if item_id:
                        obj = get_object_or_404(ItemModel, id=item_id)
                        obj.status = 1
                        obj.save()
            search_query = request.GET.get('search_query', '')
            if search_query:   
                print("query from post")
                items = ItemModel.objects.filter((Q(name__icontains=search_query) | Q(category__icontains=search_query)) & Q(status=0))
                context = {'items' : items}
                return render(request, 'xkom/main.html', context)
            else:
                return redirect('main')
            
    search_query = request.GET.get('search_query', '')
    if search_query:
        print('query nto post')
        items = ItemModel.objects.filter((Q(name__icontains=search_query) | Q(category__icontains=search_query)) & Q(status=0))
        context = {'items' : items}
        return render(request, 'xkom/main.html', context)
    
    items = ItemModel.objects.filter(status = 0)
    context = {'items' : items}
    return render(request, 'xkom/main.html', context)

@login_required
def addItem(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = AddItemForm()
            messages.success(request,'Przedmiot dodany do bazy.', extra_tags='add_item')
        else:
            messages.warning(request,'Problem z zapisaniem przedmiotu.', extra_tags='add_fail')
    context = {'form':form}
    return render (request, 'xkom/addItem.html',context)

@login_required
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