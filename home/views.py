from django.shortcuts import render
from django.http import HttpResponse
from .converter import to_mp3
import os
import random
from base.settings import BASE_DIR

def Home(request):
    if request.method=='POST':
        clean()
        
        txt=request.POST.get('text')
        if txt and txt != ' ':
            name=f'output_{random.randint(0, 5000)}.mp3'
            name=to_mp3(txt,name)
        
            file_path =str(BASE_DIR)+ 'media/'+name
            with open(file_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='audio/mp3')
                response[f'Content-Disposition'] = f'attachment; filename="{name}"'
                return response
    
    return render(request,'home.html')

def clean():
    
    folder_path=str(BASE_DIR)+'/media/'
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) and '.mp3' in file_path:
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path} : {e}")