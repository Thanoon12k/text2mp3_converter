from django.shortcuts import render
from django.http import HttpResponse
import os 
import random
from django.conf import settings
from .converter import text_to_mp3

def Home(request):
    if request.method=='POST':
        id=random.randint(0, 5000)
        file_path = f'{settings.BASE_DIR}/media/out_{id}.mp3'
        txt=request.POST.get('text')
        if txt and txt != ' ':
            text_to_mp3(txt,file_path)
            with open(file_path, 'rb') as fl:
                response = HttpResponse(fl.read(), content_type='audio/mp3')
                response[f'Content-Disposition'] = f'attachment; filename="{file_path}"'
                print("saved to - ",file_path)
                fl.close()
              
                os.remove(file_path)
                return response
    
    return render(request,'home.html')


