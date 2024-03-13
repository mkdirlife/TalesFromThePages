from django import forms
from .forms import UserProfileForm
from .models import UserProfile
from django.views.generic import UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "photo")

    # 클라이언트에서 유효성 검사를 하지만 서버에서 한번 더 체크해준다.
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("유저ID가 이미 있습니다.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("이메일이 이미 있습니다.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        
        # Django의 비밀번호 유효성 검사 시스템 사용
        validate_password(password2, self.instance)
        return password2
    

class UserSignUpView(FormView):
    template_name = 'accounts/user_signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:user_login')  # 성공 시 리다이렉트할 URL

    def form_valid(self, form):
        user = form.save()
        message = self.request.POST.get('message')
        # 프로필 사진 처리
        photo = self.request.FILES.get('photo')
        if photo:
            UserProfile.objects.create(user=user, message=message, photo=photo)
        else:
            UserProfile.objects.create(user=user, message=message)
        
        # 사용자 인증 및 로그인
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

        if user:
            login(self.request, user)
        return super().form_valid(form)  


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('blog:blog_list')    
    

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('blog:blog_list')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('accounts:profile')  # 성공 시 리다이렉션할 URL 지정

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.save()  # UserProfile 저장
        
        # 이메일 업데이트 처리
        self.request.user.email = self.request.POST.get('email')
        self.request.user.save()  # User 객체의 이메일 필드 업데이트       
        return super().form_valid(form)