from django.shortcuts import HttpResponse , redirect ,render 
from django.http import JsonResponse


def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,blog_number):
 
    return HttpResponse(f"placeholder to display blog number: {blog_number}")

def edit(request,blog_number):
    return HttpResponse(f"placeholder to edit blog number: {blog_number}")

def destroy(request,blog_number):
    return redirect("/blogs")

def blog_json(request):
    return JsonResponse(
        {"title": "my first blog", 
         "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." ,
         }
        )
    