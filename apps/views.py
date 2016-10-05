from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .request_handler import AboutHandler


@require_http_methods(['GET', 'POST'])
def index(request):
    return render(request, 'index.html')


@require_http_methods(['GET', 'POST'])
def about(request):
    handler = AboutHandler(request)
    return handler.handle()