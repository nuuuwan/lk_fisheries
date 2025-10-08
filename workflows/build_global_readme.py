from scraper import GlobalReadMe


def main():
    GlobalReadMe(
        {
            "lk_fisheries": [
                "lk_fisheries_annual_statistics_reports",
            ]
        }
    ).build()


if __name__ == "__main__":
    main()
