
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PlantListView,
    PlantDetailView,
    PlantUpdateView,
    PlantDeleteView,
    PlantCreateView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,
    EventCreateView,
)


urlpatterns = [
    # Plant URLS
    path("<int:pk>/", PlantDetailView.as_view(), name="plant_detail"),
    path("<int:pk>/edit/", PlantUpdateView.as_view(), name="plant_edit"),
    path("<int:pk>/delete/", PlantDeleteView.as_view(), name="plant_delete"),
    path("new/", PlantCreateView.as_view(), name="plant_new"),
    path("", PlantListView.as_view(), name="plant_list"),
    # Event URLS
    path("event/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("event/<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
    path("event/new/", EventCreateView.as_view(), name="event_new"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
