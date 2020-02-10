from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('Apis/',views.getter),
    path('Apis/<int:ID>',views.getters),
    # path('Apis/<int:ID>',views.deleter),


    # path('',include('Api.urls'))

]