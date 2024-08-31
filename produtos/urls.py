from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet
from . import views

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('produto/novo/', views.produto_create, name='produto_create'),
    path('produto/<int:id>/editar/', views.produto_edit, name='produto_edit'),
    path('produto/<int:id>/deletar/', views.produto_delete, name='produto_delete'),
]