from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogForm, PhotoForm
from .models import Blog, Photo


# Home page
@login_required
def home(request):
    photos = Photo.objects.all()
    blogs = Blog.objects.all()
    context = {"photos": photos, "blogs": blogs}
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


# blog/forms.py
@login_required
def blog_and_photo_upload(request):
    blog_form = BlogForm()
    photo_form = PhotoForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('home')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
    }
    return render(request, 'blog/create_blog_post.html', context=context)


@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {"blog": blog})
