from django.shortcuts import render,redirect
from food.models import Item
from .forms import ItemForm
from  django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexClassView(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class FoodDetail(LoginRequiredMixin,DetailView):
    model = Item
    template_name = 'food/detail.html'


# class based create view

class CreateItem(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/form-add.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
@login_required()
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/form-add.html',{'form':form,'item':item})
@login_required()
def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete-item.html',{'item':item})