from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Department, News, NewsCategory, Info, Doc, DocCategory

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class NewsCategoryForm(forms.ModelForm):
    class Meta:
        model = NewsCategory
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class DocCategoryForm(forms.ModelForm):
    class Meta:
        model = DocCategory
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }
