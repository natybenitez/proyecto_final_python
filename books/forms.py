from django import forms
from books.models import Writer

# class Writer_form(forms.Form):
#     name = forms.CharField(max_length=100)
#     lastname = forms.CharField(max_length=100)
#     #image = forms.ImageField(default='profile-pic-default.jpg', upload_to='profile_pics')
#     #bio = RichTextField(blank=True, help_text="Agrega información sobre este/a autor/a")
#     #country = CountryField()

#     twitter_url = forms.CharField(max_length=250)
#     instagram_url = forms.CharField(max_length=250)
    
#     web_url = forms.URLField()

class Writer_form(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__' #si quiero todo
        #fields = ('name', 'lastname', 'country')  #si quiero solo algunos

    