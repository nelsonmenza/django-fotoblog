from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ("image", "caption")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
