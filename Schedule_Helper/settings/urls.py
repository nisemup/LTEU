from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from backend import views
import debug_toolbar
from django.conf.urls.static import static
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet, basename='MyModel')
router.register(r'profiles', views.ProfileViewSet)
router.register(r'schedule', views.ScheduleViewSet)


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
