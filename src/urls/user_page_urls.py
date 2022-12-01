from src.views.user_pages_views import RegistrationView, LoginView, VerifyView, RequestCodeView, \
    RequestVerificationView, ConfirmCodeView, SetPasswordView
from django.urls import path


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register-page'),
    path('login', LoginView.as_view(), name="login-page"),
    path('verify', VerifyView.as_view(), name="verify-page"),
    path('request-vefify', RequestVerificationView.as_view(), name='request-verify-page'),
    path('request-code', RequestCodeView.as_view(), name='request-code-page'),
    path('confirm-code', ConfirmCodeView.as_view(), name='confirm-code'),
    path('new-password', SetPasswordView.as_view(), name='set-password-page')
]
