import sys

from utils import Log

from fish import (AnnualStatisticsReports, MonthlyFishProductionReports,
                  WeeklyFishPricesReports)

log = Log("pipeline")

if __name__ == "__main__":
    doc_class_label = sys.argv[1]
    log.debug(f"{doc_class_label=}")
    for doc_class in [
        AnnualStatisticsReports,
        MonthlyFishProductionReports,
        WeeklyFishPricesReports,
    ]:
        if doc_class.get_doc_class_label() == doc_class_label:
            doc_class.run_pipeline()
            sys.exit(0)
    raise ValueError(f"Unknown doc_class_label: {doc_class_label}")
