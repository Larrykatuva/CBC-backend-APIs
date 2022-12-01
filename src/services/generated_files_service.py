from src.models import GeneratedFile, ChildInstance
from django.db.models.query import QuerySet


class GenerateFileService:
    """
    Class to handle report files
    """

    @staticmethod
    def create_report_file(
            filename: str,
            url: str,
            child_instance: ChildInstance
    ):
        """Creating child report"""
        return GeneratedFile.objects.create(
            filename=filename,
            url=url,
            child_instance=child_instance
        )

    @staticmethod
    def get_report_by_id(id: str) -> GeneratedFile:
        """Get report by id"""
        try:
            return GeneratedFile.objects.get(pk=id)
        except Exception as er:
            return None

    @staticmethod
    def update_report(filter_keys: dict, update_data: dict) -> tuple:
        """Update report"""
        is_updated, updated_data = GeneratedFile.objects.filter(
            filter_keys
        ).update(update_data)
        return is_updated, updated_data

    @staticmethod
    def get_all_reports() -> QuerySet[GeneratedFile]:
        """Get all reports"""
        return GeneratedFile.objects.all()

    @staticmethod
    def filter_reports(filter_keys) -> QuerySet[GeneratedFile]:
        """Filter child instances"""
        return GeneratedFile.objects.filter(**filter_keys)


