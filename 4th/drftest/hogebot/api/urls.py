from rest_framework import routers
from .views import QuoteViewSet

router = routers.DefaultRouter()
router.register('quotes', QuoteViewSet)
