from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Department, News, NewsCategory, Info, Doc, DocCategory, Image
# from .forms import DepartmentForm, NewsForm, NewsCategoryForm, InfoForm, DocForm, DocCategoryForm
from django.utils.html import format_html  # Import format_html


# class DepartmentAdmin(TranslationAdmin):
#     form = DepartmentForm

# admin.site.register(Department, DepartmentAdmin)


# class NewsAdmin(TranslationAdmin):
#     form = NewsForm

# admin.site.register(News, NewsAdmin)


# class NewsCategoryAdmin(TranslationAdmin):
#     form = NewsCategoryForm
#     list_display = ('id', 'name')

# admin.site.register(NewsCategory, NewsCategoryAdmin)


# class InfoAdmin(TranslationAdmin):
#     form = InfoForm

# admin.site.register(Info, InfoAdmin)


# class DocCategoryAdmin(TranslationAdmin):
#     form = DocCategoryForm

# admin.site.register(DocCategory, DocCategoryAdmin)


# class DocAdmin(TranslationAdmin):
#     form = DocForm

# admin.site.register(Doc, DocAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'full_url')

    @admin.display(description='Image URL')
    def full_url(self, obj):
        return obj.image.url

    @admin.display(description='Image')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />'.format(obj.image.url))
        return "No Image"

    def get_queryset(self, request):
        self.request = request  # Save the request object for later use
        return super().get_queryset(request)


admin.site.register([
    Department, News, NewsCategory, Info, Doc, DocCategory
])