from django.shortcuts import render, redirect
from .models import UploadedImages
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addImage(request):
    if request.method == 'POST':
        profileImage = request.FILES['add-image-file']
        form = UploadedImages(updated_image =profileImage)
        form.save()
        messages.success(request, 'Profile Updated Successfully')
        profileImage =form.updated_image
        print(profileImage)
        return render(request, 'uploaded_image.html', {"uploaded_image":profileImage})
    return redirect('/')


def imagesView(request):
    images = UploadedImages.objects.all()
    return render(request, 'images_view.html', {"uploaded_images": images})
