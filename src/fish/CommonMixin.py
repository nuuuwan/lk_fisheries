import re
import sys

from scraper import GlobalReadMe
from utils import WWW, Log

log = Log("CommonMixin")


class CommonMixin:
    @classmethod
    def clean_description(cls, description: str) -> str:
        # remove non-alphanumeric and space
        description = re.sub(r"[^a-zA-Z0-9\s]", "", description)
        # replace multiple spaces with single space
        description = re.sub(r"\s+", " ", description)
        # replace space with "-"
        description = description.replace(" ", "-")
        return description.lower()

    @classmethod
    def gen_docs(cls):
        url_metadata = cls.get_url_metadata()
        soup = WWW(url_metadata).soup

        ul = soup.find("ul", class_=cls.get_ul_class())
        for li in ul.find_all("li"):
            a = li.find("a")
            href = a.get("href")

            description = a.text.strip()
            year = description.split("[")[0].split("(")[0].strip()[-4:]
            assert year.isdigit(), (year, description)
            date_str = f"{year}-12-31"
            num = cls.clean_description(description)
            lang = "en"
            url_doc = "https://www.fisheries.gov.lk" + href

            yield cls(
                num=num,
                date_str=date_str,
                description=description,
                url_metadata=url_metadata,
                lang=lang,
                url_pdf=url_doc,
            )

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
