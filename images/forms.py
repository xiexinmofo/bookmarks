from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreatedForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('title','url','description')
        widgets={
            'url':forms.HiddenInput,
        }
    def clean_url(self):
        url=self.cleaned_data['url']#cleaned_data 从哪里来?
        valid_extensions=['jpg','jpeg','png']
        extension=url.split('.')[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url
    def save(self,force_insert=False,force_update=False,commit=True):
        image=super(ImageCreatedForm,self).save(commit=False)
        image_url=self.cleaned_data['url']
        image_name="{}.{}".format(slugify(image.title),image_url.split(".")[1].lower())
        #从给定的url下载图片
        response=request.urlopen(image_url)
        image.image.save(image_name,ContentFile(response.read()),commit=False)
        if commit:
            image.save()
        return image
