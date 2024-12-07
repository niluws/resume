from django.urls import path
from .views import TeamApi, BlogApi, MemberApi,ContactApi

app_name = 'resume'

urlpatterns = [
    path("team/", TeamApi.as_view(), name="team"),
    path("blog/", BlogApi.as_view(), name="blog"),
    path("member/", MemberApi.as_view(), name="member"),
    path("contact/", ContactApi.as_view(), name="contact"),
]
