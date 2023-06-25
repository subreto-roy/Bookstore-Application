from django.contrib import admin
from django.urls import path,include 
from bookstoreapp import views
from bookstoreapp import api
from django.conf.urls.static import static
from django.conf import settings
app_name = 'bookstoreapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    #path('books/cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('api/books/', api.BookListAPI.as_view(), name='book_api_list'),
    path('api/books/create/', api.BookCreateAPI.as_view(), name='book_api_create'),
    #path('cart/', views.cart_view, name='cart_view'),
    #path('<int:book_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart_view'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


