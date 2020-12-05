from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.contrib.auth import views as auth_views

from main import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('about', views.intro, name='intro'),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('community/', include('community.urls')),
                  path('workout/', include('workout.urls')),

                  url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

                  # 비밀번호 찾기
                  path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
                       name="reset_password"),
                  path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_done.html"),
                       name="password_reset_done"),
                  path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html"),
                       name="password_reset_confirm"),
                  path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"),
                       name="password_reset_complete"),
              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
handler404 = 'accounts.views.page_not_found'