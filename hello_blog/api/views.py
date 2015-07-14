import hello_blog.models as models
import hello_blog.api.serializers as serializers

from rest_framework import generics, viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer


class CategoryNameView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.CategorySerializer
    lookup_field = 'name'
 
    def get_queryset(self):
        return models.Category.objects.filter(name=self.kwargs['name'])
