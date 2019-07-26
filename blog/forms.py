import re
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Invest
        fields = '__all__'
    def clean_team(self):
        data = self.cleaned_data.get('team',None)
        if data:
            if not re.search(r'[ㄱ-힣]',data):
                raise forms.ValidationError('팀 컬럼에 한글이 한 글자 이상 필요합니다.')
            return data