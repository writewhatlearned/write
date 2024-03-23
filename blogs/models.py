from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Label(models.Model):
    name = models.CharField(max_length=200, verbose_name='标签')
    pub_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='应用状态')

    class Meta:
        verbose_name = 'label'
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']
        index_together = ('name', 'is_active')
        unique_together = ('name', 'is_active')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='分类')
    pub_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='应用状态')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']
        index_together = ('name', 'is_active')
        unique_together = ('name', 'is_active')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = RichTextField(blank=True, null=True, verbose_name='正文')
    author = models.CharField(max_length=200, verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, verbose_name='标签')
    pub_date = models.DateTimeField(verbose_name='发表时间', auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_published = models.BooleanField(choices=[(True, '已发表'), (False, '未发表')],
                                       default=False, verbose_name='发表状态')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']
        index_together = (
            ('author', 'category'),
            ('author', 'label'),
            ('title', 'author')
        )

    def __str__(self):
        return self.title
