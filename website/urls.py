from django.urls import path
from website import views


urlpatterns = [
    path ('',views.index,name='index'),
    path ('blog/',views.blog,name='blog'),
    path ('login/',views.login,name='login'),
    path ('register/',views.register,name='register'),
    path ('about/',views.about,name='about'),
    path ('logout/',views.logout,name='logout'),
    path ('contact/',views.contact,name='contact'),
    path ('marketing/',views.marketing,name='marketing'),
    
   
]