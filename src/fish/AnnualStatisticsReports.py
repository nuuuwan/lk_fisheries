from dataclasses import dataclass

from scraper import AbstractPDFDoc
from utils import Log

from fish.CommonMixin import CommonMixin

log = Log("AnnualStatisticsReports")


@dataclass
class AnnualStatisticsReports(CommonMixin, AbstractPDFDoc):

    @classmethod
    def get_doc_class_label(cls) -> str:
        return "lk_fisheries_annual_statistics_reports"

    @classmethod
    def get_doc_class_description(cls) -> str:
        return (
            "Annual Fisheries Statistics Reports of"
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
            + "/web/index.php/en/statistics/annual-statistics-reports"
        )

    @classmethod
    def get_ul_class(cls):
        return "pdf"
