from django.contrib import admin
from django.urls import path, include
from cesmericanas.views import ClienteViewSet, FuncionarioViewSet, ProdutoViewSet, PagamentoViewSet, OfertasViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'pagamento', PagamentoViewSet)
router.register(r'ofertas', OfertasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
