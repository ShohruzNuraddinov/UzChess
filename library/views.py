from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from .models import Book, Author, BookCategory
from .serializers import BookSerializer, AuthorSerializer, BookCategorySerializer, TopRecommendBookSerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all().order_by('created_at')
    serializer_class = BookSerializer
    parser_classes = [FormParser, MultiPartParser]


class AuthorListCreateView(ListCreateAPIView):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    parser_classes = [FormParser, MultiPartParser]


class BookCategoryListCreateView(ListCreateAPIView):
    queryset = BookCategory.objects.all().order_by('id')
    serializer_class = BookCategorySerializer
    parser_classes = [FormParser, MultiPartParser]


class TopBookListView(ListAPIView):
    serializer_class = TopRecommendBookSerializer

    def get_queryset(self):
        top_books = Book.objects.filter(is_top=True).order_by('created_at')
        return top_books


class RecommendBookListView(ListAPIView):
    serializer_class = TopRecommendBookSerializer

    def get_queryset(self):
        recommend_books = Book.objects.filter(is_recommend=True).order_by('created_at')
        return recommend_books
