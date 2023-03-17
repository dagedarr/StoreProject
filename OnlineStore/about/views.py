from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'


class AboutProjectView(TemplateView):
    template_name = 'about/project.html'
