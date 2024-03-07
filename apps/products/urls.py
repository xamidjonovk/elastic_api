from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductSearchView

router = SimpleRouter()
router.register(r'search', ProductSearchView, basename='product-search')

urlpatterns = [
    path('', include(router.urls)),
]
