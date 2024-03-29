from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=6)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ("username", "email",
                  "first_name", "last_name", "role")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UploadProfilePhotoForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("profile_photo",)
