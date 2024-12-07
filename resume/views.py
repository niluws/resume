from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from .models import Blog, Form, Team, Member, Contact, Project


class TeamApi(APIView):
    class TeamSerializer(serializers.ModelSerializer):
        class Meta:
            model = Team
            fields = '__all__'

    @extend_schema(responses=TeamSerializer)
    def get(self, request):
        query = Team.objects.all().first()
        return Response(self.TeamSerializer(query, context={"request": request}).data)


class BlogApi(APIView):
    class BlogSerializer(serializers.ModelSerializer):
        class Meta:
            model = Blog
            fields = '__all__'

    @extend_schema(responses=BlogSerializer)
    def get(self, request):
        query = Blog.objects.all()
        return Response(self.BlogSerializer(query, context={"request": request}, many=True).data)


class ProjectApi(APIView):
    class ProjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = '__all__'

    @extend_schema(responses=ProjectSerializer)
    def get(self, request):
        query = Blog.objects.all()
        return Response(self.ProjectSerializer(query, context={"request": request}, many=True).data)


class MemberApi(APIView):
    class MemberSerializer(serializers.ModelSerializer):
        class Meta:
            model = Member
            fields = '__all__'

    @extend_schema(responses=MemberSerializer)
    def get(self, request):
        query = Member.objects.all()
        return Response(self.MemberSerializer(query, context={"request": request}, many=True).data)


class ContactApi(APIView):
    class ContactSerializer(serializers.ModelSerializer):
        class Meta:
            model = Contact
            fields = '__all__'

    class FormSerializer(serializers.ModelSerializer):
        class Meta:
            model = Form
            fields = '__all__'

    @extend_schema(responses=ContactSerializer)
    def get(self, request):
        query = Contact.objects.all()
        return Response(self.ContactSerializer(query, context={"request": request}, many=True).data)

    @extend_schema(request=FormSerializer, responses=FormSerializer)
    def post(self, request):
        serializer = self.FormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)