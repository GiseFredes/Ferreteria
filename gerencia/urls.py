from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, PedidoCreateView
from gerencia import views

urlpatterns = [
    path('', views.indexG, name='indexGerencia'),
    #Carga de urls del CRUD clientes
    path('cliente/',ClienteListView.as_view(), name='indexCliente' ),
    path('cliente/add', ClienteCreateView.as_view(), name = 'nuevoCliente'),
    path('cliente/editar/<int:pk>', ClienteUpdateView.as_view(), name='editarCliente'),
    path('cliente/eliminar/<int:pk>',ClienteDeleteView.as_view(), name='eliminarCliente'),
    path('pedido/add/', PedidoCreateView.as_view(), name = 'nuevoPedido'),

]