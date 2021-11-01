import json
import os
from django.forms.widgets import Media
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from uploads.core.utills import upload_image_to_ipfs,upload_json_to_ipfs,access_local_file,filepath
from uploads.core.contract_function import create_nft
from django.conf import settings
from pathlib import Path
import jsonpickle
from json import JSONEncoder
from rest_framework.response import Response



def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
     
            
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        description = "xyz"
        image_data =filepath()
        try:              
            image_Data = upload_image_to_ipfs(image_data,filename,description)
            image_url = image_Data[image]
        except Exception as e:
            print(f"exception rasise in upload json {e}")
            pass
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def nft_upload(request):     
    if request.method == 'POST':
        address = request.POST.get('address')
        image_url = request.POST.get('image_url')
        token_id = request.POST.get('token_id')
        tx_hash = create_nft(address,token_id,image_url)        
        return JsonResponse({"Transaction Hash":tx_hash, "message":"Your art is minted on our chain successfully"})
    else:
        return render(request, 'core/Mint_NFT.html')
    


