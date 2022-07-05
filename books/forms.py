from django import forms
from books.models import Writer, Book

class Writer_form(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'
        
class Book_form(forms.ModelForm):
    class Meta: 
        model = Book
        fields = '__all__'
