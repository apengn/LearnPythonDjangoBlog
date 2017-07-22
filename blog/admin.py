from django.contrib import admin
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
    #设置可选的添加字段
    # fields = ('title','desc','content')
    #列表显示
    list_display = ('title','desc','click_count')

    #设置列表中是否支持链接 list_display_links = ('click_count',)
    #设置在查看列表中是否可以修改当前列
    list_editable = ('click_count',)

    # list_filter = ('desc',)
    fieldsets = (
        (None,{
            'fields':('title','desc','content')
        }),
        ('高级设置',{
            'classes':('collapse'),
            'fields':('click_count','is_recommend')

        })
    )
    #添加媒体资源文件    富文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Ad)
admin.site.register(Links)
admin.site.register(Category)
admin.site.register(Comment)

