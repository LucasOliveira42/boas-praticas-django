from django.db import models

class Topic(models.Model):
    """Um tópico que o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma representação de string do modelo"""
        return self.text
    
class Entry(models.Model):
    """Algo específico aprendido sobre um tópico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retorna uma string simples representando a entrada"""
        if len(self.text)>50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"






"""
Podemos usar o shell do django pelo terminal para realizarmos alguns testes
nas querrys direto pelo terminal antes de implementarmos algo no código, basta
usarmos:
"python manage.py shell"

e podemos realizar comandos como:
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Xadez>, <Topic: Escalar Montanha>]>

>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
... 
1 Xadez
2 Escalar Montanha

>>> t = Topic.objects.get(id=1) 
>>> t.text
'Xadez'

>>> t.date_added
datetime.datetime(2025, 2, 17, 3, 56, 38, 609522, tzinfo=datetime.timezone.utc)

>>> t.entry_set.all()
<QuerySet [<Entry: A abertura é a primeira parte do jogo, mais ou men...>, <Entry: Na fase de abertura do jogo, é importante avançar ...>]>

Para finalizaro Shell, basta apertar ctrl+D, ou ctrl+z no windows e enter 
"""