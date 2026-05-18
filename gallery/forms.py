from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Photo, Tag

class PhotoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label=_("Select Tags"),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Photo
        fields = ('title', 'description', 'image', 'tags')
        widgets = {
            'image': forms.FileInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Style text inputs beautifully
        self.fields['title'].widget.attrs.update({
            'class': 'block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-brand-500 sm:text-sm sm:leading-6',
            'placeholder': 'Enter a catchy title...'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-brand-500 sm:text-sm sm:leading-6',
            'placeholder': 'Describe your masterpiece...'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'block w-full text-sm text-gray-900 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-brand-50 file:text-brand-500 hover:file:bg-brand-100 cursor-pointer'
        })
