from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import *
from django.views import *

from .service import replace

from .forms import UploadFileForm


# class IndexPage(TemplateView):
#     template_name = 'index.html'

class IndexPage(FormView):
    template_name = 'index.html'
    form_class = UploadFileForm


class ProcessView(View):
    def post(self, request : HttpRequest):
        replace(request.FILES['file'])
        return HttpResponseRedirect('/')