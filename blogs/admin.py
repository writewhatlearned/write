from django.contrib import admin
from .models import Label, Category, Article

# Register your models here.
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm


class ArticleAdmin(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget()  # 使用CKEditorWidget作为content字段的widget
        }


@admin.register(Article)
class BlogPostAdmin(admin.ModelAdmin):
    form = ArticleAdmin  # 使用自定义的表单类，包含富文本编辑器
    list_display = ('title', 'content')  # 在列表页显示的字段
    search_fields = ('title', 'content')

