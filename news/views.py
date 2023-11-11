from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from django.db.models import Q, F

from .models import New, Tag
from .serializers import NewSerializer, TagSerializer


class TagListAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NewsListAPIView(ListCreateAPIView):
    queryset = New.objects.all().order_by('-created_at')
    serializer_class = NewSerializer
    parser_classes = [FormParser, MultiPartParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class NewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance, "User:", request.user.id)
        serializer = self.get_serializer(instance)

        # New.objects.filter(id=self.kwargs['pk']).update(view=F('view') + 1)

        if request.user.is_authenticated:
            New.objects.filter(id=self.kwargs['pk']).update(view=F('view') + 1)

        return Response(serializer.data)


class NewQueryListAPIView(ListAPIView):
    serializer_class = NewSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search')

        if search_query:
            return New.objects.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            ).order_by('-created_at')

        return {"message": "Hech qanday ma’lumot topilmadi!"}
