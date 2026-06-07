#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .gemini_client import GeminiClient
from .serializers import GenerateTextSerializer, ChatSerializer
from django.conf import settings

class GenerateTextView(APIView):
    """POST /api/generate/ - Generate text from a prompt"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = GenerateTextSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        client = GeminiClient()
        temperature = settings.TEMPERATURE
        max_tokens = settings.MAX_TOKENS
        try:
            response_text = client.generate_text(
                prompt=serializer.validated_data['prompt'],
                temperature=serializer.validated_data.get('temperature', temperature),
                max_tokens=serializer.validated_data.get('max_tokens', max_tokens)
            )
            return Response({
                'success': True,
                'response': response_text
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChatView(APIView):
    """POST /api/chat/ - Chat with Gemini"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        client = GeminiClient()
        try:
            response_text = client.chat(
                messages=serializer.validated_data['messages'],
                temperature=serializer.validated_data.get('temperature', 0.7)
            )
            return Response({
                'success': True,
                'response': response_text
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)