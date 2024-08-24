from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Department, News, NewsCategory, Info, Doc, DocCategory
from .forms import DepartmentForm, NewsForm, NewsCategoryForm, InfoForm, DocForm, DocCategoryForm


class DepartmentAdmin(TranslationAdmin):
    form = DepartmentForm

admin.site.register(Department, DepartmentAdmin)


class NewsAdmin(TranslationAdmin):
    form = NewsForm

admin.site.register(News, NewsAdmin)


class NewsCategoryAdmin(TranslationAdmin):
    form = NewsCategoryForm
    list_display = ('id', 'name')

admin.site.register(NewsCategory, NewsCategoryAdmin)


class InfoAdmin(TranslationAdmin):
    form = InfoForm

admin.site.register(Info, InfoAdmin)


class DocCategoryAdmin(TranslationAdmin):
    form = DocCategoryForm

admin.site.register(DocCategory, DocCategoryAdmin)


class DocAdmin(TranslationAdmin):
    form = DocForm

admin.site.register(Doc, DocAdmin)
