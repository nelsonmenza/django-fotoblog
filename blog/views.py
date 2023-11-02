from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogForm, DeleteBlogForm, PhotoForm
from .models import Blog, Photo


# Home page
@login_required
def home(request):
    """
    Render the home page, displaying photos and blogs.

    This view fetches all Photo and Blog objects and renders them on the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered home page.
    """
    photos = Photo.objects.all()
    blogs = Blog.objects.all()
    context = {"photos": photos, "blogs": blogs}
    return render(request, "blog/home.html", context)


# Photo upload
@login_required
def photo_upload(request):
    """
    Handle photo uploads and display the photo upload form.

    This view handles the photo upload form submission and saves the uploaded photo.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered photo upload page.
    """
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "blog/photo_upload.html", context)


# Create multiple photos
def create_multiple_photos(request):
    """
    Create multiple photo objects.

    This view allows the user to create multiple photo objects using a formset.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered create multiple photos page.
    """
    PhotoFormset = formset_factory(PhotoForm, extra=5)
    formset = PhotoFormset()
    if request.method == "POST":
        formset = (request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect("home")
    return render(request, "blog/create_multiple_photos.html", {"formset": formset})


# Blog and Photo upload
@login_required
def blog_and_photo_upload(request):
    """
    Handle blog and photo uploads and display the blog and photo upload form.

    This view handles the submission of both a blog and a photo, associating them.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered blog and photo upload page.
    """
    blog_form = BlogForm()
    photo_form = PhotoForm()
    if request.method == "POST":
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
            return redirect("home")
    context = {
        "blog_form": blog_form,
        "photo_form": photo_form,
    }
    return render(request, "blog/create_blog_post.html", context=context)


# View Blog
@login_required
def view_blog(request, blog_id):
    """
    View a specific blog post.

    This view retrieves and displays a specific blog post based on its ID.

    Args:
        request: The HTTP request object.
        blog_id: The ID of the blog post to view.

    Returns:
        HttpResponse: A response containing the rendered blog post.
    """
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog/view_blog.html", {"blog": blog})


# Edit Blog
@login_required
def edit_blog(request, blog_id):
    """
    Edit or delete a specific blog post.

    This view allows the user to edit or delete a specific blog post.

    Args:
        request: The HTTP request object.
        blog_id: The ID of the blog post to edit or delete.

    Returns:
        HttpResponse: A response containing the rendered edit blog page.
    """
    blog = get_object_or_404(Blog, id=blog_id)
    edit_form = BlogForm(instance=blog)
    delete_form = DeleteBlogForm()
    if request.method == "POST":
        if "edit_blog" in request.POST:
            edit_form = BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
        if "delete_blog" in request.POST:
            delete_form = DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect("home")
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, "blog/edit_blog.html", context=context)
