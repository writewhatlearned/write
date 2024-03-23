from django.db import models


# Create your models here.
class Visit(models.Model):
    visit_time = models.DateTimeField(verbose_name='访问时间', auto_now_add=True)
    ip = models.GenericIPAddressField(verbose_name='访问IP', null=True, blank=True)
    browser = models.CharField(max_length=200, verbose_name='浏览器', null=True, blank=True)

    class Meta:
        verbose_name = '访问信息'
        verbose_name_plural = verbose_name
        db_table = 'blogs_visit'
        ordering = ['-visit_time']

    def __str__(self):
        return self.ip
