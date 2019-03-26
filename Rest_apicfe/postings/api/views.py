# Generic views are used
from django.db.models import Q
from rest_framework import generics, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly

class BlogPostApiView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'  # can also use slug,ID)
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)| Q(content__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'  # can also use slug,ID
# A way to override lookup_field
    # def get_object(self):
    #   pk = self.kwargs.get("pk")
    #   return BlogPost.objects.get(pk=pk)
    serializer_class = BlogPostSerializer # getting the serializer class and using it to convert and validate data
    permission_classes = [IsOwnerOrReadOnly]
# query_set  = BlogPost.objects.all() below is the way to override it

    def get_queryset(self):
        return BlogPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


