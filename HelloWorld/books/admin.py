from django.contrib import admin
from books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')#列表显示内容
    search_fields = ('first_name', 'last_name')#搜索框

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')#列表显示内容
    list_filter = ('publication_date',)#列表用日期排序
    date_hierarchy = 'publication_date'#列表用日期排序功能同上
    ordering = ('-publication_date',)#出版日期逆序排序
    fields = ('title', 'authors', 'publisher', 'publication_date')#编辑页面中可编辑栏目
    filter_horizontal = ('authors',)#好用的多选框
    raw_id_fields = ('publisher',)
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)
# Register your models here.