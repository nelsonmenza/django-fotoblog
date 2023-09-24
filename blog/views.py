from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import forms, models


@login_required
def home(request):
    photos = models.Photo.objects.all()
    context = {"photos": photos}
    return render(request, "blog/home.html", context)


@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    context = {"form": form}
    return render(request, "blog/photo_upload.html", context)
