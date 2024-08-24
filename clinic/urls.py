from django.urls import path
from .views import (
    home_view,
    info_view,
    department_detail_view,
    news_view,
    news_detail_view,
    doc_list_view,
    doc_detail_view,
)

app_name = 'clinic'

urlpatterns = [
    path('', home_view, name='home'),
    path('info/<int:pk>/', info_view, name='info'),
    path('department/<int:pk>/', department_detail_view, name='department'),
    path('news/', news_view, name='news'),
    path('news/<int:pk>/', news_detail_view, name='news_detail'),
    path('docs/<int:pk>/', doc_list_view, name='doc'),
    path('docs/detail/<int:pk>/', doc_detail_view, name='doc_detail'),
]
