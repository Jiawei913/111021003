from django.contrib import admin
from django.urls import path, include
from myapp.views import index  # 導入你的 index 視圖

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # 將空路徑指向 index 視圖
]
