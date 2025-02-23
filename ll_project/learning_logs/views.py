from django.shortcuts import render
from .models import Topic

def index(request):
    """A página inicial do Registro de Aprendizagem"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.order_by('date_added')
    """busca na tabela Topics dentro do banco de dados todos os objetos e os organiza pela linha data"""
    
    context = {'topics' : topics}
    """"Cria o dicionário de contexto que será enviado para o template trabalhar, a nomeação da
    variável como context parece ser padrão por ser assim que a função render reconhece como
    requisito""" 
    return render(request, 'learning_logs/topics.html', context)


def topic(request,topic_id):
    """Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    """Essa querry busca apenas o objeto que tiver o ID específico q está sendo informado"""

    entries = topic.entry_set.order_by('-date_added')
    """Obtemos todas as entradas associadas a este tópico em específico e fazemos a ordenação
    pela data em que foi criado, sendo que o '-', o faz de forma inversa, colocando as mais novas
    na frente"""

    context = {'topic' : topic, 'entries' : entries}
    """Armazena os objetos retornados da tabela de topics e da tabela de entries dentro do 
    dicionário de contexto"""
    return render(request, 'learning_logs/topic.html', context)