# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template

from councilmatic import settings
from councilmatic.rhok import models

def index(request):
    context = RequestContext(request)
    context['RHOK_STATIC_URL'] = settings.RHOK_STATIC_URL
    #context['rhok'] = models.Rhok.objects.active()
    template = get_template('rhok/index.html')
    return HttpResponse(template.render(context))
