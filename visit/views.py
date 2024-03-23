from django.shortcuts import render
from visit.utils import visit_process
from visit.models import Visit


# Create your views here.


def index(request):
    # 当前用户信息查询
    visit = visit_process.visit_process(request)['visited']

    # 访问量总计
    visit_count = Visit.objects.count()

    return render(request, 'visit/index.html',
                  {'ip': visit.ip, 'browser': visit.browser, 'datetime': visit.visit_time,
                   'visit_count': visit_count})
