"""configuracoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from banco_digital.views.cliente_viewset import ClienteViewSet
from banco_digital.views.conta_viewset import ContaViewSet
from banco_digital.views.lista_conta_cliente_viewset import ListaContaClienteViewset
from banco_digital.views.lista_transacao_conta_viewset import ListaTransacaoContaViewset
from banco_digital.views.transacao_viewset import TransacaoViewSet




router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'conta', ContaViewSet)
router.register(r'transacoes', TransacaoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/conta/', ListaContaClienteViewset.as_view()),
    path('conta/<int:pk>/transacao/', ListaTransacaoContaViewset.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
