from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import OrderForm
from .models import DesireInfo




def Order_list(request):
    info = DesireInfo.objects.all()
    return render(request, 'Order_list.html', {
        'info': info
    })




def delete_Order(request, pk):
    if request.method == 'POST':
        Order = DesireInfo.objects.get(pk=pk)
        Order.delete()
    return redirect('Order_list')


class OrderListView(ListView):
    model = DesireInfo
    template_name = 'class_Order_list.html'
    context_object_name = 'info'


class UploadOrderView(CreateView):
    model = DesireInfo
    form_class = OrderForm
    success_url = reverse_lazy('class_Order_list')
    template_name = 'upload_Order.html'