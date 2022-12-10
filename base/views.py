from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogModel

def home(request):
    return redirect('home2', id=1)


def index(request, id):
    form = BlogForm()
    blog = {}
    try:
        blog = BlogModel.objects.get(id=id)
    except:
        blog = {
            'title': "Hello There",
            'desc': "",
            'image': {'url': "https://picsum.photos/500/500?random=2"}
        }
        print("Error")
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {
        'form': form,
        'data': BlogModel.objects.all(),
        'blog': blog
    })