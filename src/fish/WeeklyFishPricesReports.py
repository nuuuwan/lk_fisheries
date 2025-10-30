from dataclasses import dataclass

from scraper import AbstractExcelSpreadsheet
from utils import Log, TimeFormat

from fish.CommonMixin import CommonMixin

log = Log("WeeklyFishPricesReports")


@dataclass
class WeeklyFishPricesReports(CommonMixin, AbstractExcelSpreadsheet):

    @classmethod
    def get_doc_class_label(cls) -> str:
        return "lk_fisheries_weekly_fish_prices_reports"

    @classmethod
    def get_doc_class_description(cls) -> str:
        return (
            "Weekly Fish Prices Reports of"
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
            + "/web/index.php/en/statistics/weekly-fish-prices"
        )

    @classmethod
    def get_ul_class(cls):
        return "excel"

    @staticmethod
    def parse_date_str_from_description(description: str) -> str:
        x = CommonMixin.clean_description_for_time(description)
        if not x:
            return None
        tokens = x.split(" ")
        month_and_year_str = " ".join(tokens[-2:]).strip()
        week_num = x[0]
        day = (int(week_num) - 1) * 7 + 1
        return TimeFormat.DATE.format(
            TimeFormat("%d %B %Y").parse(f"{day} {month_and_year_str}")
        )
