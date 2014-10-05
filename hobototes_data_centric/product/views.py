from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from product.models import *
# ref: https://docs.djangoproject.com/en/dev/intro/tutorial03/

# Create your views here.
def index(request):
    topic_list = Topic.objects.all().order_by('id')[:5]
    context = {'topic_list': topic_list} # render(request, template, dict) 
    return render(request, 'product/index.html', context)

def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'product/detail.html', {'topic': topic})

def max_purchase(request):
    pass