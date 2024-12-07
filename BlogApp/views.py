from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all() # To get all the objects from the database (Post model)
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    single_post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'single_post': single_post})