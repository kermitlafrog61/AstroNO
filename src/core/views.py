from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import RegisterForm
from .models import Event


class EventListView(generic.ListView):
    template_name = 'event-list.html'
    queryset = Event.objects.all()


class EventRegisterView(generic.FormView):
    template_name = 'event-detail.html'
    queryset = Event.objects.all()
    form_class = RegisterForm
    success_url = '/success/'

    def dispatch(self, request, *args, **kwargs):
        self.event = get_object_or_404(Event, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        registration = form.save(commit=False)
        registration.event = self.event
        registration.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.event
        return context


def success(request):
    return render(request, "success.html")
