from typing import List, Dict, Tuple
from bs4 import BeautifulSoup
from .interface.html_collector import HtmlCollectorInterface
from ..contract.contract import Contract
from ..config.logs import Logger

class HtmlCollector(HtmlCollectorInterface):

    @classmethod
    def collect_information(cls, html: str) -> List[Tuple[str, str]]:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            Logger.logr.info("Initializing BeautifulSoup for scraping")
            
            countries = soup.find("section", { "id": "countries" })
            container_row = countries.find("div", { "class": "container" }).find_all("div", { "class": "row"})

            countries_world = []
            for item in container_row:
                for i in item("div", { "class": "col-md-4 country" }):
                    countries_world.append(
                        Contract(
                        nome= i.find("h3", { "class": "country-name" }).get_text().strip(),
                        capital= i.find("div", { "class": "country-info" }).find("span", { "class": "country-capital" }).get_text().strip(),
                        populacao= i.find("div", { "class": "country-info" }).find("span", { "class": "country-population" }).get_text().strip(),
                        area= i.find("div", { "class": "country-info" }).find("span", { "class": "country-area" }).get_text().strip()
                    ))
            Logger.logr.info("Data extraction completed successfully")
            return countries_world
        except Exception as e:
            Logger.logr.error(f"{e}")
    
    
