from django.http import Http404


def user_verifier(topic, request):
    if topic.owner != request.user:
        raise Http404