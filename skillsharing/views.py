from django.shortcuts import render
from django.views import generic

from skillsharing.models import Skill, HelpRequest


class IndexView(generic.TemplateView):
    template_name = 'skillsharing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["skills"] = Skill.objects.all()

        context["help_requests"] = HelpRequest.objects.filter(helper__isnull=False)

        return context
