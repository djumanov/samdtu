from modeltranslation.translator import translator, TranslationOptions
from .models import Department, News, NewsCategory, Info, Doc, DocCategory


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Department, DepartmentTranslationOptions)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(News, NewsTranslationOptions)


class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(NewsCategory, NewsCategoryTranslationOptions)


class InfoCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Info, InfoCategoryTranslationOptions)


class DocCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(DocCategory, DocCategoryTranslationOptions)


class DocTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Doc, DocTranslationOptions)

