from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from common.util import user_verifier

def index(request):
    """A página inicial do Registro de Aprendizagem"""
    return render(request, 'learning_logs/index.html')


# Inserido o decorator para modificar o comportamento dessa função, logo, apenas usuários cadastrados 
# poderão requisitar o acesso a esta página
@login_required
def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    """busca na tabela Topics dentro do banco de dados todos os objetos que sejam do dono que está 
    logado e os organiza pela linha data"""
    
    context = {'topics' : topics}
    """"Cria o dicionário de contexto que será enviado para o template trabalhar, a nomeação da
    variável como context parece ser padrão por ser assim que a função render reconhece como
    requisito""" 
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request,topic_id):
    """Mostra um único tópico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    """Essa querry busca apenas o objeto que tiver o ID específico q está sendo informado"""

    #verifica se o tópico pertence ao usuário atual
    user_verifier(topic, request)
    #if topic.owner != request.user:
    #    raise Http404

    entries = topic.entry_set.order_by('-date_added')
    """Obtemos todas as entradas associadas a este tópico em específico e fazemos a ordenação
    pela data em que foi criado, sendo que o '-', o faz de forma inversa, colocando as mais novas
    na frente"""

    context = {'topic' : topic, 'entries' : entries}
    """Armazena os objetos retornados da tabela de topics e da tabela de entries dentro do 
    dicionário de contexto"""
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        # Nenhum dado enviado; cria um formulário em branco
        form = TopicForm

    else:
        # Dados POST enviados; processa os dados
        form = TopicForm(data=request.POST)
        # colocamos em form uma instância de TopicForm na qual recebe as informações envaidas
        # pelo usuário, que obtemos através do request.post

        if form.is_valid():
            # é importante realizar a verificação da validade dos dados antes de salva-los no bd
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        
    # Exibe um formulário em branco ou inválido
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    user_verifier(topic, request)


    if request.method != "POST":
        #nenhum dado enviado, cria um formulário em branco
        form = EntryForm
    else:
        # dados POST enviados; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            """Intrui o Django a criar um objeto de entrada e atribuílo a new_entry, sem salva-lo
            no bd para que se possa add o topic ao objeto na linha abaixo"""
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # Exibe um formulário em branco ou inválido
    context = {'topic' : topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    user_verifier(topic, request)


    if request.method!='POST':
        # Requisição inicial; pré-preenche formulário com a entrada atual
        form=EntryForm(instance=entry)
    else:
        #dados POST enviados; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry':entry,'topic':topic ,'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)