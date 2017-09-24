from django.shortcuts import render
from app01 import models

# Create your views here.


def index(request):
    # models.BxSlider.objects.filter(status=1)  # 对象
    queryset_dict = models.BxSlider.objects.filter(status=1).values('img', 'href', 'name')
    # queryset_list = models.BxSlider.objects.filter(status=1).values_list('img', 'href', 'name')
    return render(request, 'index.html', {'queryset_dict': queryset_dict})


def students(request):

    return render(request, 'student.html')