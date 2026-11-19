from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView

from skillsharing.forms import HelpRequestForm
from skillsharing.models import Skill, HelpRequest


class IndexView(generic.TemplateView):
    template_name = 'skillsharing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["skills"] = Skill.objects.all()

        context["help_requests"] = HelpRequest.objects.filter(helper__isnull=False)

        return context


class HelpRequestListView(LoginRequiredMixin, ListView):
    model = HelpRequest
    template_name = 'skillsharing/help_requests.html'
    context_object_name = 'help_requests'

    def get_queryset(self):
        return HelpRequest.objects.filter(
            skill__users=self.request.user,
            helper__isnull=True
        )


class HelpRequestCreateView(LoginRequiredMixin, CreateView):
    model = HelpRequest
    form_class = HelpRequestForm
    template_name = "skillsharing/add_help_request.html"
    success_url = reverse_lazy("skillsharing:index")

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)


@login_required
@require_POST
def accept_help_request(request, help_request_id):

    # Utilisation de la méthode update pour éviter les risques de concurrence
    updated = HelpRequest.objects.filter(
        pk=help_request_id,
        helper__isnull=True,
        skill__users=request.user
    ).update(
        helper=request.user
    )

    if updated == 1:
        messages.success(
            request,
            "Demande prise en charge"
        )
    else:
        messages.error(
            request,
            "Cette demande n'est plus disponible."
        )

    return HttpResponseRedirect(reverse_lazy("skillsharing:help_requests"))

