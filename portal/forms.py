from django.forms import ModelForm, BooleanField
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # check_box = BooleanField(label='Алло, Галочка!')
    class Meta:
        model = Post
        fields = ['name', 'type', 'category', 'text', 'post_auth']