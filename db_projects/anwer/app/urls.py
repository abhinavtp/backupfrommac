from unicodedata import name
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.baabtra,name='baabta'),
    path('blog',views.blog,name='bl'),
    path('login',views.login,name='lo'),
    path('aboutus',views.aboutus,name='ab'),
    path('placement',views.placement,name='pl'),
    path('anwer',views.anwer,name='an'),
    path('new',views.new,name='ne'),
    path('db',views.db,name='d'),
    path('profile',views.profile,name='pro'),
    path('logout',views.logout,name='logout'),
    path('addproduct',views.addproduct,name='productadd'),
    path('home',views.home,name='hom'),
    path('view_products',views.view_products,name='view'),
    path('updateproduct/<int:id>',views.updateproduct,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('emailcheck',views.emailcheck,name='email'),
    path('insert',views.insert,name='ins'),
    path('doctors',views.serve_doctors,name='doc'),
    path('doctors/<int:id>',views.serve_doctors,name='doc'),
  

]
