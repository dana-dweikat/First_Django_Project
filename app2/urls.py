from django.urls import path
from . import views

urlpatterns = [
    path('',views.root), # Redirect 
    path('blogs', views.index), # HttpResponse "placeholder to later display a list of all blogs"
    path('blogs/new', views.new), # HttpResponse 
    path('blogs/create',views.create), # Redirect
    path('blogs/<int:blog_number>',views.show),
    path('blogs/<int:blog_number>/edit',views.edit),
    path('blogs/<int:blog_number>/delete',views.destroy),
    path('blogs/json',views.blog_json),

]