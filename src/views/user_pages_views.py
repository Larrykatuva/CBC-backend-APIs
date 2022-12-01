from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from src.services.user_service import UserService
from src.services.app_service import AppService
from src.services.auth_service import AuthService


def validate_params(request, template_name):
    if request.method == 'POST':
        kwargs = request.POST
    else:
        kwargs = request.GET
    client_id = kwargs.get('client_id', '')
    if not AppService.get_app_by_client_id(client_id=client_id):
        messages.error(request, "Invalid client_id")
        return render(
            request=request,
            template_name=template_name
        )
    scope = kwargs.get('scope', '')
    redirect_uri = kwargs.get('redirect_uri', '')
    if not client_id or not scope or not redirect_uri:
        messages.error(request, "Authentication denied")
        return render(
            request=request,
            template_name=template_name
        )
    return client_id, scope, redirect_uri


class RegistrationView(View):
    user_service = UserService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='register.html'
        )
        return render(request=request, template_name='register.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='register.html'
        )
        email = request.POST['email']
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if not email or not username or not phone or not password:
            messages.error(request, "All the required fields must be filled")
            return render(request, 'register.html', context)
        if self.user_service.get_user_by_username(username=username):
            messages.error(request, "Username already exists")
            return render(request, 'register.html', context)
        if phone.__len__() < 10 or phone.__len__() > 12:
            messages.error(request, "Invalid phone number")
            return render(request, 'register.html', context)
        if self.user_service.get_user_by_email(email=email):
            messages.error(request, "Email already registered")
            return render(request, 'register.html', context)
        if self.user_service.get_user_by_phone(phone=phone):
            messages.error(request, "Phone already exists")
            return render(request, 'register.html', context)
        user = self.user_service.register_user(
            email=email,
            username=username,
            phone=phone,
            password=password
        )
        self.user_service.send_activation_code(
            user=user
        )
        messages.success(request, "Account created successfully, verification code sent to email")
        return render(
            request=request,
            template_name='verify.html',
            context=context
        )


class LoginView(View):
    user_service = UserService()
    auth_service = AuthService()
    app_service = AppService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='login.html'
        )
        return render(request=request, template_name='login.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='login.html'
        )
        username = request.POST['username']
        password = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if not username or not password:
            messages.error(request, "All the required fields must be filled")
            return render(request, 'login.html', context)
        if not self.user_service.get_user_by_username(username=username):
            messages.error(request, "Username does not exists")
            return render(request, 'login.html', context)
        client_id, scope, redirect_uri = args
        app = self.app_service.get_app_by_client_id(
            client_id=client_id
        )
        user = self.auth_service.authenticate_user(
            username=username,
            password=password
        )
        if not user:
            messages.error(request, "Invalid login details")
            return render(request, 'login.html', context)
        if not user.is_verified:
            messages.error(request, "User account not verified, "
                                    "verification code already send to your email.")
            return render(
                request=request,
                template_name='verify.html',
                context=context
            )
        auth_code = self.auth_service.create_code(user=user, app=app)
        redirect_url = redirect_uri + "?code=" + auth_code.code
        return redirect(
            to=redirect_url
        )


class VerifyView(View):
    user_service = UserService()
    auth_service = AuthService()
    app_service = AppService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='verify.html'
        )
        return render(request=request, template_name='verify.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='verify.html'
        )
        code = request.POST['code']
        context = {
            'fieldValues': request.POST
        }
        if not code:
            messages.error(request, "Code is required")
            return render(request, 'verify.html', context)
        try:
            user = self.user_service.get_user_by_code(code=code)
        except Exception as error:
            messages.error(request, "Invalid verification code")
            return render(request, 'verify.html', context)
        messages.success(request, 'Account verified successfully')
        self.user_service.verify_user_account(email=user.email)
        return render(
            request=request,
            template_name='login.html',
            context=context
        )


class RequestVerificationView(View):
    user_service = UserService()
    auth_service = AuthService()
    app_service = AppService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='request-verify.html'
        )
        return render(request=request, template_name='request-verify.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='request-verify.html'
        )
        email = request.POST['email']
        context = {
            'fieldValues': request.POST
        }
        if not email:
            messages.error(request, "Email is required")
            return render(request, 'request-verify.html', context)
        user = self.user_service.get_user_by_email(email=email)
        if not user:
            messages.error(request, "Email does not exist")
            return render(request, 'request-verify.html', context)
        self.user_service.send_activation_code(
            user=user
        )
        messages.success(request, 'Verification code sent to email.')
        return render(
            request=request,
            template_name='verify.html',
            context=context
        )


class RequestCodeView(View):
    user_service = UserService()
    auth_service = AuthService()
    app_service = AppService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='request-code.html'
        )
        return render(request=request, template_name='request-code.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='request-code.html'
        )
        email = request.POST['email']
        context = {
            'fieldValues': request.POST
        }
        if not email:
            messages.error(request, "Email is required")
            return render(request, 'request-code.html', context)
        user = self.user_service.get_user_by_email(email=email)
        if not user:
            messages.error(request, "Email does not exist")
            return render(request, 'request-code.html', context)
        self.user_service.send_activation_code(
            user=user
        )
        messages.success(request, 'Password reset code sent to email.')
        return render(
            request=request,
            template_name='confirm-code.html',
            context=context
        )


class ConfirmCodeView(View):
    user_service = UserService()
    auth_service = AuthService()
    app_service = AppService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='confirm-code.html'
        )
        return render(request=request, template_name='confirm-code.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='confirm-code.html'
        )
        code = request.POST['code']
        context = {
            'fieldValues': request.POST
        }
        if not code:
            messages.error(request, "Code is required")
            return render(request, 'confirm-code.html', context)
        try:
            user = self.user_service.get_user_by_code(code=code)
        except Exception as error:
            messages.error(request, "Invalid verification code")
            return render(request, 'confirm-code.html', context)
        valid_code = self.user_service.confirm_activation_code(
            code=code,
            user=user
        )
        if not valid_code:
            messages.error(request, "Invalid verification code")
            return render(request, 'confirm-code.html', context)
        messages.success(request, 'Code accepted, Set a new password.')
        return render(
            request=request,
            template_name='new-password.html',
            context=context
        )


class SetPasswordView(View):
    user_service = UserService()
    auth_service = AuthService()
    app_service = AppService()

    def get(self, request):
        validate_params(
            request=request,
            template_name='new-password.html'
        )
        return render(request=request, template_name='new-password.html')

    def post(self, request):
        args = validate_params(
            request=request,
            template_name='login.html'
        )
        code = request.POST['code']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']
        context = {
            'fieldValues': request.POST
        }
        if not password or not password_confirm:
            messages.error(request, "All fields are required")
            return render(request, 'new-password.html', context)
        if password != password_confirm:
            messages.error(request, "Password should match confirm password")
            return render(request, 'new-password.html', context)
        try:
            user = self.user_service.get_user_by_code(code=code)
        except Exception as error:
            messages.error(request, "Enter your password reset code")
            return render(request, 'confirm-code.html', context)
        self.user_service.set_new_password(
            email=user.email,
            password=password
        )
        self.user_service.verify_user_account(email=user.email)
        messages.success(request, 'Password updated successfully')
        return render(
            request=request,
            template_name='login.html',
            context=context
        )


