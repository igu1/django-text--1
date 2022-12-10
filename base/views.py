from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogModel, CommentModel
from django.utils import timezone


def home(request):
    return redirect('home2', id=1)


def index(request, id):
    form = BlogForm()
    blog = {}
    message = {}
    try:
        blog = BlogModel.objects.get(id=id)
    except:
        blog = {
            'title': "Hello There",
            'desc': "",
            'image': {'url': "https://picsum.photos/500/500?random=2"}
        }
        
    if request.method == 'POST':
        if 'comment' not in request.POST:
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.created = timezone.now()
                form.save()
        else:
            message = request.POST['message']
            if message.strip() != "":
                print(request.POST)
                CommentModel.objects.create(message=message, user=request.user, blog=BlogModel.objects.get(id=request.POST['blog'])) 
    comments = []
    try:
        comments = CommentModel.objects.filter(blog=BlogModel.objects.get(id=id))
    except:
        print('Error')
    return render(request, 'index.html', {
        'form': form,
        'data': BlogModel.objects.all(),
        'blog': blog,
        'comments': comments
    })


def delete_blog(request, id):
    BlogModel.objects.get(id=id).delete()
    return redirect('home')