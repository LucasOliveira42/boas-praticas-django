"""Define padrões de URL para contas"""

from django.urls import path, include
from . import views

"""django.contrib.auth.urls inclui URLs de autenticação default definidos pelo Django, 
incuindo, login e logout, por isso eles não precisam ser criados na view"""

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Página de cadastro
    path('register/', views.register, name='register'),
]
