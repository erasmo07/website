from django.core.cache import cache
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'marketing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            slack_member_count=cache.get('slack_member_count', 0),
            github_repos=cache.get('github_projects', None),
        )
        return context


class TermsOfService(TemplateView):
    template_name = 'marketing/terms_of_service.html'
