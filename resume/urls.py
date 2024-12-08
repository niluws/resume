from django.urls import path
from graphene_django.views import GraphQLView
from .views import  BlogApi, MemberApi, ContactApi, ProjectApi
from .schema import schema

app_name = 'resume'

urlpatterns = [
    path('team/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path("blog/", BlogApi.as_view(), name="blog"),
    path("members/", MemberApi.as_view(), name="member"),
    path("contact/", ContactApi.as_view(), name="contact"),
    path("projects/", ProjectApi.as_view(), name="projects"),
]
