from django.contrib import admin
from django.urls import include, path
from . import views

#path zoals hieronder members/ bepaald de url. Dus verander members naar abc en dan is het link /abc ipv link/members

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', include('members.urls')),
     path('admin/', admin.site.urls),


]
     