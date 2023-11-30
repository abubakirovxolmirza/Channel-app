from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return render(request, 'posts/index.html', {'postlar': models.post.objects.all()})
