from django.contrib import admin
from django.urls import path, include  # 引入 include 函数
from accounts.views import login_view, upload_file  # 导入你的登录视图和上传文件视图
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),  # 已有的 URL
    path('upload/', upload_file, name='upload_file'),  # 已有的 URL
    path('lecturer/', include('lecturer.urls')),  # 已有的 URL
    path('publication/', include('publication.urls')),  # 新添加的 URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)