from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from .models import Blog, Message, Member, Project


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
        query = Project.objects.all()
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
    class MessageSerializer(serializers.ModelSerializer):
        class Meta:
            model = Message
            fields = '__all__'

    @extend_schema(request=MessageSerializer, responses=MessageSerializer)
    def post(self, request):
        serializer = self.MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
