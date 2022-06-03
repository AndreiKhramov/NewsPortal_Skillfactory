from django.urls import path
from .views import NewsList, NewsDetail, PostCreateView, PostDeleteView, PostEditView, NewsListSearch


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', NewsListSearch.as_view(), name='news_search'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create/<int:pk>', PostEditView.as_view(), name='post_edit'),

]