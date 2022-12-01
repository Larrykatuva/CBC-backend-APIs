from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.urls.user_urls')),
    path('test-moc/', include('src.urls.moc_urls')),
    # path('user/page/', include('src.urls.user_page_urls')),
    path('', include('config.swagger_urls')),
    path('school/', include('src.urls.school_urls')),
    path('teacher/', include('src.urls.teacher_urls')),
    path('child/', include('src.urls.children_urls')),
    path('grade/', include('src.urls.grade_urls')),
    path('subject/', include('src.urls.subject_urls')),
    path('feed/', include('src.urls.feed_urls')),
    path('comment/', include('src.urls.comment_urls')),
    path('notifications/', include('src.urls.notifications_url'))
]
