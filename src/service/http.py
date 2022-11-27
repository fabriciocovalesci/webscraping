from typing import Dict
import requests
from requests.structures import CaseInsensitiveDict
from .interfaces.http_interface import HttpRequesterInterface
from ..config.logs import Logger


class HttpRequest(HttpRequesterInterface):
    
    def __init__(self) -> None:
        self.__url = 'https://www.scrapethissite.com/pages/simple/'


    def request_from_page(self) -> Dict[int, str]:
        try:
            headers = CaseInsensitiveDict()
            headers['Accept'] = 'text/plain'
            headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            response = requests.get(self.__url, headers=headers)
            Logger.logr.info(f"Request for page www.scrapethissite.com")
            return {
                "status_code": response.status_code,
                "html": response.text
            }
        except Exception as e:
            Logger.logr.error(f"{e}")