from django import forms



class PostForm(forms.Form):
    categoly = forms.CharField(max_length=30, label='カテゴリー' )
    title = forms.CharField(max_length=50, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    