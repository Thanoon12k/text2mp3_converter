from rest_framework import serializers



class Mp3UploadSerializer(serializers.Serializer):
    mp3file = serializers.FileField()
