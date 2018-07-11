from django import forms

# why use lable here
from article.models import Article

'''
如果 Django 表單內容是來自於 Model，則繼承 forms.ModelForm
一般 Django 表單則繼承 forms.Form， 且不需要 class Meta 類別
'''
class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'content']