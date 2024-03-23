from datetime import timezone, timedelta
from django.utils import timezone
from django.http import HttpRequest
from visit.models import Visit


def visit_process(request: HttpRequest) -> dict:
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    browser = request.META.get('HTTP_USER_AGENT', 'UNKNOWN_USER_AGENT')

    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # None

    time_delta = timezone.now() - timedelta(hours=2)

    visited = Visit.objects.filter(ip=ip).filter(visit_time__gte=time_delta)

    if visited:
        res = {'visited': visited[0]}
    else:
        res = {'visited': Visit.objects.create(ip=ip, visit_time=timezone.now(), browser=browser)}

    return res
