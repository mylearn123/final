from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    # path('', Home.as_view(), name='home'),
    # path('upload/', upload, name='upload'),
    path('info/',Order_list, name='Order_list'),
    # path('info/upload/', upload_Order, name='upload_Order'),
    path('info/<int:pk>/', delete_Order, name='delete_Order'),

    path('class/info/', OrderListView.as_view(), name='class_Order_list'),
    path('class/info/upload/',UploadOrderView.as_view(), name='class_upload_Order'),

    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)