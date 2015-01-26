from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('pubWeb/index.html')
    context = RequestContext(request, {
        'get_selection': 1
    })
    return HttpResponse(template.render(context));
