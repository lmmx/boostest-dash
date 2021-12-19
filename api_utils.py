from __future__ import annotations
from urllib.parse import urlencode

__all__ = ["ApiQuery", "create_boostest_url"]

class ApiQuery:
    """
    Query for the UK Coronavirus Data Dashboard API, expressed as a URL string through
    the :attr:`url_string` property.
    """
    url_prefix: str = "https://api.coronavirus.data.gov.uk/v2/data"
    query_keys: list[str] = "areaType metric format".split()

    def __init__(
        self,
        metric_keys: list[str],
        area_type: str = "overview",
        data_format: str = "csv",
    ):
        if 1 > len(metric_keys):
            raise ValueError("Minimum of 1 metric required for an API call")
        elif len(metric_keys) > 5:
            raise ValueError("Maximum of 5 metrics permitted for an API call")
        self.areaType: str = area_type
        self.metric: list[str] = metric_keys
        self.format: str = data_format

    @property
    def query_string(self):
        """
        Generate list of 2-tuples with duplicate keys (multiple metrics) as
        ``[("areaType", "overview"), ("metric", "..."), ("metric", "..."), ...]``
        then encode as a parameterised query string ("?areaType=overview&metric=...")
        """
        query: list[tuple[str, str]] = [
            (k, val)
            for k, v in [(key, getattr(self, key)) for key in self.query_keys]
            for val in (v if isinstance(v, list) else [v])
        ]
        return f"?{urlencode(query)}"

    @property
    def url_string(self):
        return f"{self.url_prefix}{self.query_string}"


def create_boostest_url():
    boostest_metrics = [
        "cumVaccinationFirstDoseUptakeByPublishDatePercentage",
        "cumVaccinationSecondDoseUptakeByPublishDatePercentage",
        "cumVaccinationThirdInjectionUptakeByPublishDatePercentage",
        "newPCRTestsByPublishDate",
        "newLFDTestsBySpecimenDate",
    ]
    api_url = ApiQuery(metric_keys=boostest_metrics).url_string
    return api_url
