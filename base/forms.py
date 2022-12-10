from django import forms
from .models import BlogModel



class BlogForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control my-1',
				   'placeholder':'Title'}))

    class Meta:
        model = BlogModel
        fields = ("title",'desc')

        labels = {
            "desc": ''
        }