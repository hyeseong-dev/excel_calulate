from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', include('calculate.urls'), name='calculate'),
    path('', include('main.urls'), name='main'),
    path('email/', include('sendEmail.urls'), name='email'),
    
]
