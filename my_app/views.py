from django.shortcuts import render
import io
from PIL import Image
from .encrypt_by_allam import encode , decode
def encrypt(request):
    if request.method == 'POST' :
        my_f = request.FILES["myfile"].read()
        img = Image.open(io.BytesIO(my_f))
        password = request.POST['password']
        data = request.POST['encrypt_data']
        print(password)
        print(data)
        encode(img,password,data)
    return render(request,'index.html')
def decrypt(request):
    context = {}
    if request.method == 'POST' :
        my_f = request.FILES["myfile"].read()
        image = Image.open(io.BytesIO(my_f))
        password = request.POST['password']
        data = decode(image,password)
        context = {"data" : data}
    return render(request,'decrypt.html' , context )