from django.shortcuts import render

def index(request):
    """A página inicial do Registro de Aprendizagem"""
    return render(request, 'learning_logs/index.html')