from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('event/', views.EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', views.EventRegisterView.as_view(), name='event-detail'),
    path('success/', views.success, name='success'),
]

if settings.DEBUG:
    urlpatterns.extend((
        *static(settings.STATIC_URL,
                document_root=settings.STATICFILES_DIRS[0]),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ))
