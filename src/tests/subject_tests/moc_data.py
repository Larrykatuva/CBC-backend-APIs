from django.conf import settings
import os


class SubjectMocs:
    """School test moc data"""

    def __init__(self):
        self.create_data = {
            "subject_title": "English",
            "status": 1,
            "course": "Literature",
            "color": "Blue",
            "abbreviation": "abbreviation"
        }

        self.update_data = {
            "subject_title": "English",
            "status": 1,
            "course": "Literature",
            "color": "Blue",
            "abbreviation": "abbreviation"
        }
