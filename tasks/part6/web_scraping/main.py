from __future__ import annotations

import json
import math
import re
import time
from dataclasses import dataclass
from typing import Any, Iterable, Sequence

import requests
from bs4 import BeautifulSoup

MOST_ACTIVE_URL = "https://finance.yahoo.com/most-active"
SCREENER_URL = "https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved"
QUOTE_SUMMARY_URL = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/{symbol}"

DEFAULT_TIMEOUT = 20

HEADERS = {
    "User-Agent": {
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    },
    "Accept": "application/json,text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9"
}

class YahooFinanceError(RuntimeError):
    pass

@dataclass(frozen=True)
class Stock:
    name: str
    code: str

@dataclass(frozen=True)
class CEOStock:
    name: str
    code: str
    country: str
    employees: int | None
    ceo_name: str
    ceo_year_born: int

@dataclass(frozen=True)
class StatisticsStock:
    name: str
    code: str
    fifty_two_week_change: float
    total_cash: int | None

@dataclass(frozen=True)
class InstitutionalHolder:
    name: str
    code: str
    shares: int | None
    date_reported: str
    percent_out: float | None
    value: int | None

class YahooFinanceClient:
    def __init__(self, session: requests.Session | None = None, delay_seconds: float = 0.2) -> None:
        self.session = session or requests.Session()
        self.session.headers.update(HEADERS)
        self.delay_seconds = delay_seconds
    
    def _get_json(self, url: str, *, params: dict[str, Any] | None = None) -> dict[str, Any]:
        response = self.session.get(url, params=params, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()

        try:
            return response.json()
        except requests.JSONDecodeError as error:
            raise YahooFinanceError(f"Yahoo returned an invalid JSON response for: {response.url}") from error
    
    def get_most_active_stocks(self, count: int = 100) -> list[Stock]:
        try:
            return self._get_most_active_from_api(count)
        except (requests.RequestException, YahooFinanceError, KeyError):
            return self._get_most_active_from_html(count)

    def _get_most_active_from_api(self, count: int) -> list[Stock]:
        payload = self._get_json(SCREENER_URL, params={"scrIds": "most_actives", "count": count, "start": 0})

        try:
            quotes = payload["finance"]["result"][0]["quotes"]
        except (KeyError, IndexError, TypeError) as error:
            raise YahooFinanceError("The most active response has an unexpected structure") from error
    
        stocks: list[Stock] = []

        for quote in quotes:
            symbol = quote.get("symbol")
            name = {
                quote.get("longName") or quote.get("shortName") or symbol
            }

            if symbol:
                stocks.append(Stock(name=str(name), code=str(symbol)))

        if not stocks:
            raise YahooFinanceError("No stocks were found in the screener")

        return stocks
        