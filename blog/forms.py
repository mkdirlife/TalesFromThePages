from django import forms
from .models import Blog, Comment, Tag, Category
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    tags = forms.CharField(required=False, help_text="태그를 입력 해주세요. 예)소설, 작가, 재밌다")  # tags 필드 추가
    
    class Meta:
        model = Blog
        fields = ['title', 'thumb_image', 'content', 'category'] # 'tags' 필드는 별도 처리
        widgets = {         
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thumb_image'].required = True  # 썸네일 이미지 필드를 필수 항목으로 설정
        self.fields['category'].required = True  # 썸네일 이미지 필드를 필수 항목으로 설정

    def clean_thumb_image(self):
        thumb_image = self.cleaned_data.get('thumb_image')
        if thumb_image:
            return thumb_image
        else:
            raise forms.ValidationError("썸네일 이미지는 필수 입력 항목입니다.")

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError('본문 내용을 입력해주세요.')
        return content

    def clean_tags(self):
        tags_str = self.cleaned_data.get('tags', '')
        if not tags_str:
            return []
        tags_list = [tag.strip() for tag in tags_str.split(',')]
        return tags_list


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']