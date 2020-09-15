from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('',views.welcome, name='home'),
    path('about-us/', views.about, name='about'),
    path('ussdapp/', views.ussdapp,name="us")
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)