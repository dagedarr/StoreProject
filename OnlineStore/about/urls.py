from django.urls import path

from .views import AboutAuthorView, AboutProjectView

app_name = 'about'

urlpatterns = [
    path('project/', AboutProjectView.as_view(), name='about_project'),
    path('me/', AboutAuthorView.as_view(), name='about_me'),
]
