from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
import os
import random
from django.conf import settings
from home.converter import text_to_mp3

class TextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)

class TextToMp3View(APIView):
    parser_classes = (JSONParser, )

    def post(self, request, *args, **kwargs):
        serializer = TextSerializer(data=request.data)

        if serializer.is_valid():
            id = random.randint(0, 5000)
            file_path = f'{settings.BASE_DIR}/media/out_{id}.mp3'
            text = serializer.validated_data['text']

            if text and text.strip() != '':
                text_to_mp3(text, file_path)
                
                with open(file_path, 'rb') as fl:
                    response = HttpResponse(fl.read(), content_type='audio/mp3')
                    response['Content-Disposition'] = f'attachment; filename="out_{id}.mp3"'
                    fl.close()
              
                os.remove(file_path)
                return response

            return Response({'detail': 'Invalid text.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
