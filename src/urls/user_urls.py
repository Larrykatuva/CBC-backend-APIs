from src.views.user_views import RegisterUserView, VerifyUserView, RequestResetCodeView, CheckResetCode, \
    SetPasswordView, AccessTokenView
from django.urls import path


urlpatterns = [
    path('register', RegisterUserView.as_view(), name='register-user'),
    path('verify', VerifyUserView.as_view(), name='verify-user'),
    path('request-reset-code', RequestResetCodeView.as_view(), name='reset-code'),
    path('check-code', CheckResetCode.as_view(), name='check-code'),
    path('set-new-password', SetPasswordView.as_view(), name='set-new-password'),
    path('access-token', AccessTokenView.as_view(), name='access-token')
]
