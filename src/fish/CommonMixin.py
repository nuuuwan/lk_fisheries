import re
import sys

from scraper import GlobalReadMe
from utils import WWW, Log

log = Log("CommonMixin")


class CommonMixin:

    @staticmethod
    def clean_description_for_time(description: str) -> str:
        x = description

        x = x.replace("\xa0", " ")

        for phrase in ["[", "(", "PROVISIONAL", "EXCEL"]:
            if phrase in x:
                x = x.split(phrase)[0]

        x = x.strip()
        return x

    @classmethod
    def clean_description(cls, description: str) -> str:
        description = re.sub(r"[^a-zA-Z0-9\s]", "", description)
        description = re.sub(r"\s+", " ", description)
        description = description.replace(" ", "-")
        return description.lower()

    @classmethod
    def gen_docs(cls):
        url_metadata = cls.get_url_metadata()
        soup = WWW(url_metadata).soup

        for ul in soup.find_all("ul", class_=cls.get_ul_class()):
            for li in ul.find_all("li"):
                a = li.find("a")
                href = a.get("href")

                description = a.text.strip()
                if "Final Report" in description:  # HACK
                    continue

                if "June)" in description or "- 2019" in description:  # HACK
                    continue

                date_str = cls.parse_date_str_from_description(description)
                if not date_str:
                    continue
                num = cls.clean_description(description)
                lang = "en"
                url_doc = "https://www.fisheries.gov.lk" + href

                d = dict(
                    num=num,
                    date_str=date_str,
                    description=description,
                    url_metadata=url_metadata,
                    lang=lang,
                )
                d["url_" + cls.get_ul_class()] = url_doc
                yield cls(**d)

    @classmethod
    def run_pipeline(cls, max_dt=None):
        max_dt = (
            max_dt
            or (float(sys.argv[2]) if len(sys.argv) > 2 else None)
            or cls.MAX_DT
        )
        log.debug(f"{max_dt=}s")

        cls.cleanup_all()
        cls.scrape_all_metadata(max_dt)
        cls.write_all()
        cls.scrape_all_extended_data(max_dt)
        cls.build_summary()
        cls.build_doc_class_readme()
        cls.build_and_upload_to_hugging_face()

        if not cls.is_multi_doc():
            GlobalReadMe(
                {cls.get_repo_name(): [cls.get_doc_class_label()]}
            ).build()
