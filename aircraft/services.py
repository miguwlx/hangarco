import requests

BASE_URL = "https://www.datos.gov.co/resource/qsim-wdzj.json"
TIMEOUT = 10


class DataServiceError(Exception):
    """Raised when the open data API cannot be queried."""


def search_aircraft(query, limit=50):
    params = {"$q": query, "$limit": limit}
    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as exc:
        raise DataServiceError("Could not query the data source") from exc