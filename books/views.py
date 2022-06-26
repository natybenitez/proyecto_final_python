from django.shortcuts import render
from books.models import Writer

# Create your views here.


def writers(request):
    writers = Writer.objects.all()
    context = {'writers': writers}
    return render(request, 'writers.html', context = context)