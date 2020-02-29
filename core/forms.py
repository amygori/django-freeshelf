from django.forms import ModelForm

from .models import Book


class BookForm(ModelForm):
  # in the MDN docs they use forms.Form
    class Meta:
        model = Book
        fields = ('title', 'author', 'category')
