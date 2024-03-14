from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Blog, Comment, Tag, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class BlogListView(ListView):
    model = Blog
    context_object_name = 'posts'  # 컨텍스트 변수 이름 설정
    paginate_by = 8  # 한 페이지에 보여줄 객체 수
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        qs = super().get_queryset().order_by('-created_at')
        q = self.request.GET.get('q', '')   # 제목 검색 쿼리
        if q:
            qs = qs.filter(title__icontains=q)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['categories'] = Category.objects.all()  # 카테고리 목록 전달
        return context    
blog_list = BlogListView.as_view()


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = PostForm
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/form.html'

    def form_valid(self, form):
        blog = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        blog.author = self.request.user
        blog.save()

        # 태그 처리
        tags_list = form.cleaned_data.get('tags', [])
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            blog.tags.add(tag)
        return super().form_valid(form)
blog_create = BlogCreateView.as_view()


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'post'
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        # 현재 포스트 객체 가져와서
        post = context['post']  
        # 삭제되지 않은 댓글만 골라서 보여줌.
        #comments = post.comments.filter(is_deleted=False)  
        # 모든 댓글 보여주도록 수정. 
        comments = Comment.objects.filter(post=post, parent__isnull=True)  # 실제 DB에 삭제하지 않고, 삭제되었습니다. 라고 뜨게 함
        context['comments'] = comments  # 필터링된 댓글을 컨텍스트에 추가
         
        context['top_tags'] = Tag.objects.annotate(num_posts=Count('blog')).order_by('-num_posts')[:5] # 가장 많이 사용된 태그 5개 추가
        context['categories'] = Category.objects.all()  # 카테고리 목록 추가   
        context['recent_posts'] = Blog.objects.order_by('-created_at')[:3]  # 최근 블로그 글 3개 추가     
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        print(self.kwargs)
        post = get_object_or_404(Blog, pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)
blog_detail = BlogDetailView.as_view()


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = PostForm
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user
blog_update = BlogUpdateView.as_view()


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:blog_list')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user
blog_delete = BlogDeleteView.as_view()


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.post.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user  # 댓글 작성자 설정
        form.instance.post = get_object_or_404(Blog, pk=self.kwargs['pk'])  # 댓글이 달릴 글 설정
        return super().form_valid(form)
    

class CommentDeleteView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = []  # 뷰에서 업데이트할 필드가 없으므로 비워둡니다.
    template_name = 'blog/comment_delete.html'

    def form_valid(self, form):
        """
        폼 유효성 검사가 성공하면 호출됩니다.
        댓글의 is_deleted를 True로 설정합니다.
        """
        comment = form.save(commit=False)
        comment.is_deleted = True
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return reverse_lazy('blog:blog_detail', kwargs={'pk': comment.post.pk})
    
    def get_queryset(self):
        """ 사용자가 자신의 댓글만 삭제할 수 있도록 합니다. """
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class BlogTagListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_name = self.kwargs['tag']
        return Blog.objects.filter(tags__name=tag_name).order_by('-created_at')


class BlogCategoryListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        category_name = self.kwargs['category']
        return Blog.objects.filter(category__name=category_name).order_by('-created_at')
    

class AuthorPostsListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog.objects.filter(author__username=self.kwargs.get('username')).order_by('-created_at')