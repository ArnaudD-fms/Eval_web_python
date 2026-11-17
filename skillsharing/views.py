from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from skillsharing.forms import HelpRequestForm
from skillsharing.models import Skill, HelpRequest


class IndexView(generic.TemplateView):
    template_name = 'skillsharing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["skills"] = Skill.objects.all()

        context["help_requests"] = HelpRequest.objects.filter(helper__isnull=False)

        return context


class HelpRequestCreateView(CreateView):
    model = HelpRequest
    form_class = HelpRequestForm
    template_name = "skillsharing/add_help_request.html"
    success_url = reverse_lazy("skillsharing:index")