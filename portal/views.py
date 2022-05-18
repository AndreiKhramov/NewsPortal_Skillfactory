from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post

from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = 'add_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        # context['time_now'] = datetime.utcnow()
        # context['next_post'] = None
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
