from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url='tube/'), name='root'),
    path('', RedirectView.as_view(pattern_name='blog:blog_list'), name='root'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)