# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from product.models import *
# ref: https://docs.djangoproject.com/en/dev/intro/tutorial03/

# Create your views here.

# The below is converted into generic view
# def index(request):
#     # topic_list = Topic.objects.all().order_by('id') #[:5]
#     topic_list = get_list_or_404(Topic, price=0)
#     context = {'topic_list': topic_list} # render(request, template, dict) 
#     return render(request, 'product/index.html', context)

# def detail(request, topic_id):
#     topic = get_object_or_404(Topic, pk=topic_id)
#     return render(request, 'product/detail.html', {'topic': topic})

class IndexView(generic.ListView):
    template_name = 'product/index.html'
    # context_object_name = 'topic_list'

    def get_queryset(self):
        """
        Return the topics.

        group in template (by {% regroup %} tag)

         """
#  How can I display a group one after one in Django template?

#  Google: how to render queryset group by category in django template?

# *  -> [django template view queryset group by] (http://stackoverflow.com/search?q=django+template+view+queryset+group+by)
#     * http://stackoverflow.com/questions/8678336/django-grouping-querysets-by-a-certain-field-in-template
#     * {regroup} tag in https://docs.djangoproject.com/en/1.7/ref/templates/builtins/
        # return Topic.objects.order_by('-id') #[:5]
        # closed = Topic.objects.filter(status='closed').order_by('-id') #[:5]
        # new =  Topic.objects.filter(status='new').order_by('-id') #[:5]
        return  Topic.objects.order_by('status') # queryset is a list


class DetailView(generic.DetailView):
    model = Topic # a shorthand for  queryset = Topic.objects.all()
    # template_name = 'product/detail.html'

def max_purchase(request):
    pass