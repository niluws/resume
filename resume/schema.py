import graphene
from graphene_django import DjangoObjectType

from .models import Team


class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = '__all__'


class Query(graphene.ObjectType):
    team = graphene.List(TeamType)

    def resolve_team(self, info):
        return Team.objects.all()


schema = graphene.Schema(query=Query)
