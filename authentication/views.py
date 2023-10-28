from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SignupForm, UploadProfilePhotoForm

# class LoginPageView(View):
#     template_name = 'authentication/login.html'
#     form_class = forms.LoginForm

#     def get(self, request):
#         form = self.form_class()
#         message = ""
#         context = {'form': form, 'message': message}
#         return render(request, self.template_name, context)

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Login faild!'
#         context = {'form': form, 'message': message}
#         return render(request, self.template_name, context)

# def logout_user(request):
# logout(request)
# return redirect('login')


def signup_page(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    context = {'form': form}
    return render(request, 'authentication/signup.html', context)


# def upload_profile_photo(request):
#     form = forms.UploadProfilePhotoForm()
#     if request.method == "POST":
#         form = forms.UploadProfilePhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             photo = form.save(commit=False)
#             photo.uploader = request.user
#             photo.save()
#             return redirect('home')
#     context = {"form": form}
#     return render(request, "blog/photo_upload.html", context)

@login_required
def upload_profile_photo(request):
    form = UploadProfilePhotoForm()
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {"form": form}
    ...
