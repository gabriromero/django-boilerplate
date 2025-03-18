from rest_framework.routers import DefaultRouter
from initial_app.views.first_viewset import FirstViewSet

router = DefaultRouter()
router.register(r'', FirstViewSet, basename='my-viewset')

urlpatterns = router.urls
