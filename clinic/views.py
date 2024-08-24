from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Department, News, NewsCategory, Info, Doc, DocCategory


def home_view(request):
    departments = Department.objects.all()
    latest_news = News.objects.order_by('-created').all()[:4]

    return render(request, 'home/index.html', {'departments': departments, 'latest_news': latest_news})

def info_view(request, pk):
    news_item = get_object_or_404(Info, id=pk)
    return render(request, 'info/info.html', {'info': news_item})


def news_view(request):
    category_id = request.GET.get('category_id')
    news_list = News.objects.order_by('-created').all()
    
    if category_id:
        try:
            category = NewsCategory.objects.get(id=category_id)
            news_list = news_list.filter(category=category)
        except NewsCategory.DoesNotExist:
            pass

    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    news_categories = NewsCategory.objects.all()
    return render(request, 'news/news.html', {'page_obj': page_obj, 'news_categories': news_categories})

def news_detail_view(request, pk):
    news_item = get_object_or_404(News, id=pk)
    latest_news = News.objects.order_by('-created').all()[:5]
    return render(request, 'news/news_detail.html', {'news_item': news_item, 'latest_news': latest_news})

def department_detail_view(request, pk):
    department = get_object_or_404(Department, id=pk)
    return render(request, 'department/department.html', {'department': department})

def doc_list_view(request, pk):
    docs_list = []
    try:
        category = DocCategory.objects.get(id=pk)
        docs_list = Doc.objects.filter(category=category)
    except NewsCategory.DoesNotExist:
        pass
    print(docs_list)
    return render(request, 'docs/docs.html', {'docs': docs_list, 'category': category})

def doc_detail_view(request, pk):
    document = get_object_or_404(Doc, id=pk)
    return render(request, 'docs/doc.html', {'doc': document})
