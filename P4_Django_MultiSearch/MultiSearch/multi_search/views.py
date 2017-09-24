from django.shortcuts import render

# Create your views here.
from multi_search import models


def video(request):
    direction_list = models.Direction.objects.all().values('id', 'name')
    class_list = models.Classification.objects.all().values('id', 'name')
    level_list = models.Video.level_choice
    # ((1, '初级'), (2, '中级'), (3, '高级'))
    print(level_list)

    # 将元组转化为【列表套字典】
    ret = map(lambda x: {"id": x[0], "name": x[1]}, models.Video.level_choice)
    print(list(ret))
    # 将 ((1, '初级'), (2, '中级'), (3, '高级')) 转化为 ↓
    # [{'name': '初级', 'id': 1}, {'name': '中级', 'id': 2}, {'name': '高级', 'id': 3}]

    return render(request, 'video.html', {'direction_list': direction_list,
                                          'class_list': class_list,
                                          'level_list': level_list})
