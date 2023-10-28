from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PhotoForm
from .models import Photo


# Home page
@login_required
def home(request):
    photos = Photo.objects.all()
    context = {"photos": photos}
    return render(request, "blog/home.html", context)

# Photo upload


@login_required
def photo_upload(request):
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    context = {"form": form}
    return render(request, "blog/photo_upload.html", context)
