from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
       This viewset automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.

       Additionally we also provide an extra `highlight` action.
       """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """This will handle list and retrieve as per viewsets.py"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Entry point to our API

@api_view(['GET'])
def api_route(request):
    return Response({
        'users': reverse('user-list', request=request),
        'snippets': reverse('snippet-list', request=request)
    })
