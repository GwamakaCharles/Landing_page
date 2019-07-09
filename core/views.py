from django.shortcuts import render
from .models import Post


def PostView(request):
    post = Post.objects.all()
    return render(request, 'core/index.html', {'post': post})