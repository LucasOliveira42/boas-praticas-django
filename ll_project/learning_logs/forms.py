from django import forms
from .models import Topic, Entry

#o arquivo forms.py precisa ser criado manualmente na mesma pasta que models.py

class TopicForm(forms.ModelForm):
    """A versão mais simples de ModelForm consiste em uma classe Meta aninhada
    que informa ao Django em qual modelo basear o formulário e quais campos incluir"""
    class Meta:
        model = Topic
        #informamos que o formulário deve ser baseado no model Topic
        fields = ['text']
        #informamos que ele deve incluir apenas o campo text
        labels = {'text' : ''}
        #informamos que o django n deve gerar um rótulo para o campo text


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        """Um widget é um elemento de formulário HTML, como uma caixa de
        texto de linha única, área de texto de v;arias linhas ou uma
        lista suspensa. Aqui estamos instruindo o Djnago a usar um textarea
        com 80 colunas, ao invés das 40 tradicionais"""