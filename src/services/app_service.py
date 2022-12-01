from src.models.server_models import App
from django.db.models.query import QuerySet
import random
import string


class AppService:
    """
    Class to handle all app operations
    """

    @staticmethod
    def register_app(
            name: str,
            manager: str,
            client_id: str,
            client_secret: str
    ) -> App:
        """Method to register new app"""
        return App.objects.create(
            name=name,
            manager=manager,
            client_id=client_id,
            client_secret=client_secret
        )

    def generate_client_id(self) -> str:
        """Generating a random unique app client_id"""
        result_str = ''.join(
            random.choice(string.ascii_letters)
            for i in range(100)
        )
        if App.objects.filter(client_id=result_str).exists():
            self.generate_client_id()
        return result_str

    def generate_client_secret(self) -> str:
        """Generating a random app client_secret"""
        result_str = ''.join(
            random.choice(string.ascii_letters)
            for i in range(100)
        )
        if App.objects.filter(client_secret=result_str).exists():
            self.generate_client_secret()
        return result_str

    @staticmethod
    def get_app_by_client_id(client_id: str) -> App:
        """Get app by a client id"""
        try:
            return App.objects.get(client_id=client_id)
        except App.DoesNotExist:
            return None

    @staticmethod
    def get_app_by_client_secret(client_secret: str) -> App:
        """Getting an app by client secret"""
        try:
            return App.objects.get(
                client_secret=client_secret
            )
        except App.DoesNotExist:
            return None

    @staticmethod
    def get_apps_by_manager(manager: str) -> QuerySet[App]:
        """Getting all applications for a certain manager"""
        return App.objects.filter(manager=manager)

    @staticmethod
    def get_all_apps():
        """Getting all apps"""
        return App.objects.all()

    @staticmethod
    def validate_app_details(
            client_id: str,
            client_secret: str,
            redirect_url: str
    ) -> App:
        """Validate app credentials"""
        try:
            return App.objects.get(
                client_id=client_id,
                client_secret=client_secret,
                redirect_url=redirect_url
            )
        except App.DoesNotExist:
            return None
