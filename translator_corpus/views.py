from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect


def start(request):
    return render_to_response('start.html')

