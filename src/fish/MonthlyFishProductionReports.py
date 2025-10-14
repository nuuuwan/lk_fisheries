from dataclasses import dataclass

from scraper import AbstractExcelSpreadsheet
from utils import Log

from fish.CommonMixin import CommonMixin

log = Log("MonthlyFishProductionReports")


@dataclass
class MonthlyFishProductionReports(CommonMixin, AbstractExcelSpreadsheet):

    @classmethod
    def get_doc_class_label(cls) -> str:
        return "lk_fisheries_monthly_fish_production_reports"

    @classmethod
    def get_doc_class_description(cls) -> str:
        return (
            "Monthly Fish Production Reports of"
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
            + "/web/index.php/en/statistics/monthly-fish-production"
        )

    @classmethod
    def get_ul_class(cls):
        return "excel"
