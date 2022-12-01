from django.conf import settings
import os


class SchoolMocs:
    """School test moc data"""

    def __init__(self):
        self.create_data = {
            "name": "Kahawa Primary",
            "location": "Ruiru",
            "address": "0984200 Ruiru",
            "telephone": "0879098890",
            "motto": "Kurasa we can",
            "logo": open(file=os.path.join(settings.BASE_DIR, 'g.jpg'), encoding="utf8", errors='ignore'),
            "status": 1
        }

        self.update_data = {
            "name": "Kahawa Accademy",
            "location": "Ruiru",
            "address": "0984200 Ruiru",
            "telephone": "0879098890",
            "motto": "Kurasa we can",
            "logo": open(file=os.path.join(settings.BASE_DIR, 'g.jpg'), encoding="utf8", errors='ignore'),
            "status": 1
        }
