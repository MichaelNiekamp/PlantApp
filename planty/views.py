from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Plant, Event

User = get_user_model()

# Create your views here.
class PlantListView(LoginRequiredMixin, ListView):
    # model = Plant
    context_object_name = "plant_list"
    template_name = "plant_list.html"
    user_id = User.id

    def get_queryset(self):
        return Plant.objects.filter(author=self.request.user)


class PlantDetailView(DetailView):
    model = Plant
    template_name = "plant_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PlantDetailView, self).get_context_data(**kwargs)
        context["events"] = Event.objects.filter(plant_id=self.object)
        return context


class PlantUpdateView(UpdateView):
    model = Plant
    fields = (
        "name",
        "type",
        "description",
        "date_planted",
    )
    template_name = "plant_edit.html"


class PlantDeleteView(DeleteView):
    model = Plant
    template_name = "plant_delete.html"
    success_url = reverse_lazy("plant_list")


class PlantCreateView(CreateView):
    model = Plant
    template_name = "plant_new.html"
    fields = (
        "name",
        "type",
        "description",
        "date_planted",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Event Views
class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context["plants"] = Plant.objects.filter(name=self.object)
        return context


class EventUpdateView(UpdateView):
    model = Event
    fields = (
        "plant_id",
        "event_title",
        "height",
        "picture",
        "description",
    )
    template_name = "event_edit.html"


class EventDeleteView(DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("plant_list")


class EventCreateView(CreateView):
    model = Event
    template_name = "event_new.html"
    fields = (
        "plant_id",
        "event_title",
        "height",
        "picture",
        "description",
    )
