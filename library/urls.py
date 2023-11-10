from django.urls import path

from .views import BookListCreateView, AuthorListCreateView, BookCategoryListCreateView, TopBookListView, \
    RecommendBookListView, BookDetailView

urlpatterns = [
    path('book', BookListCreateView.as_view(), name='book'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('category', BookCategoryListCreateView.as_view(), name='category'),
    path('author', AuthorListCreateView.as_view(), name='author'),

    path('top-book', TopBookListView.as_view(), name='top_book'),
    path('recommend-book', RecommendBookListView.as_view(), name='recommend_book'),
]
