from blog.models import Post
from django.forms import ModelForm


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'publication_date')
