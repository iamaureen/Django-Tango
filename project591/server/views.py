from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import bookmarkSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BookmarkView(APIView):
    def post(self, request):
        serializer = bookmarkSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
