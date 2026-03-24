from django.urls import path
from . import views

# Nombre de la app
app_name = 'products'

# URL's Para el CRUD de Productos (Create, Read, Update, Delete)
urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
]
