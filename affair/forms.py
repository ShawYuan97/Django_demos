from django import forms


class submitfileForm(forms.Form):
    title = forms.CharField(label='标题', max_length=128)
    file = forms.FileField(label='文件', max_length=128)
