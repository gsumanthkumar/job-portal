from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('getjobv',views.getjobv,name='getjobv'),
    path('postjobv',views.postjobv,name='postjobv'),
    path('logout',views.logout,name='logout'),
    path('mypostedjobs',views.mypostedjobs,name='mypostedjobs'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('profile',views.profile,name='profile'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search')
]