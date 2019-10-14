from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls'), name='home'),
    path('accounts/', include('accounts.urls')),
]
