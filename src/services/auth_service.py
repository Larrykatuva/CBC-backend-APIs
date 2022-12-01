from src.models.server_models import App
from src.models.user_models import User, AuthCode
from rest_framework_simplejwt.tokens import RefreshToken
import random
import string


class AuthService:

    @staticmethod
    def generate_auth_code() -> str:
        """Generating a random app client_secret"""
        result_str = ''.join(
            random.choice(string.ascii_letters)
            for i in range(50)
        )
        return result_str

    def create_code(self, user: User, app: App) -> AuthCode:
        """Create authentication code used for generating access token"""
        code = self.generate_auth_code()
        AuthCode.objects.filter(user=user, app=app).delete()
        return AuthCode.objects.create(
            user=user,
            app=app,
            code=code,
            redeemed=False
        )

    @staticmethod
    def authenticate_user(username: str, password: str) -> User:
        """Authenticate user with username and password"""
        user = User.objects.filter(username=username)
        if user.__len__() == 0:
            return None
        # print(username, password)
        # user = auth.authenticate(
        #     username=username,
        #     password=password
        # )
        return user[0]

    @staticmethod
    def get_code(code: str) -> AuthCode:
        """Get auth code by code"""
        try:
            return AuthCode.objects.get(code=code)
        except AuthCode.DoesNotExist:
            return None

    @staticmethod
    def redeem_code(code: str):
        """Redeem authentication token"""
        return AuthCode.objects.filter(
            code=code
        ).update(redeemed=True)

    @staticmethod
    def generate_access_token(auth_code: AuthCode) -> dict:
        """Generate access token"""
        tokens = RefreshToken.for_user(auth_code.user)
        kwargs = {
            'refresh_token': str(tokens),
            'access_token': str(tokens.access_token)
        }
        return kwargs



