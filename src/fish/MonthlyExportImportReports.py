from dataclasses import dataclass

from scraper import AbstractExcelSpreadsheet
from utils import Log, TimeFormat

from fish.CommonMixin import CommonMixin

log = Log("MonthlyExportImportReports")


@dataclass
class MonthlyExportImportReports(CommonMixin, AbstractExcelSpreadsheet):

    @classmethod
    def get_doc_class_label(cls) -> str:
        return "lk_fisheries_monthly_export_import_reports"

    @classmethod
    def get_doc_class_description(cls) -> str:
        return (
            "Monthly Fish Export and Import Reports of"
            + " the Ministry of Fisheries,Aquatic and Ocean Resources,"
            + " Sri Lanka"
        )

    @classmethod
    def get_doc_class_emoji(cls) -> str:
        return "🐟"

    @classmethod
    def get_url_metadata(cls):
        return (
            "https://www.fisheries.gov.lk"
            + "/web/index.php/en/statistics/export-import"
        )

    @classmethod
    def get_ul_class(cls):
        return "excel"

    @staticmethod
    def parse_date_str_from_description(description: str) -> str:
        x = CommonMixin.clean_description_for_time(description)
        month_and_year_str = x.split("-")[-1].strip()
        return TimeFormat.DATE.format(
            TimeFormat("%B %Y").parse(month_and_year_str)
        )
