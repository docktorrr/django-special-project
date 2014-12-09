# -*- coding: utf-8 -*-
from django import forms
from sp.contest.models import Work


#forms
class WorkForm(forms.ModelForm):
    
    def __init__(self, name_required, image_required, text_required, videocode_required, videolink_required, category_required, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        if name_required:
            self.fields['name'].required = True
        if image_required:
            self.fields['image'].required = True
        if text_required:
            self.fields['text'].required = True
        if videocode_required:
            self.fields['video_code'].required = True
        if videolink_required:
            self.fields['video_link'].required = True
        if category_required:
            self.fields['category'].required = True
    
    class Meta:
        model = Work
        fields = ['name', 'image', 'text', 'video_code', 'video_link', 'category', 'tags']        
        
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 5*1024*1024:
                raise forms.ValidationError(u"Изображение слишком большое (>5mb)")
        else:
            if self.fields['image'].required:
                raise forms.ValidationError("Couldn't read uploaded image")        
        return image
