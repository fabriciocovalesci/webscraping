from src.service.http import HttpRequest
from src.extract.collector import HtmlCollector
from src.infra.write_file import WriteFile
from src.paths import get_root_project
from src.config.logs import Logger



class Start:
    
    def run_automation(self):
        Logger.logr.info(f"Automation started")
        
        response = HttpRequest()
        html = response.request_from_page()["html"]
        
        collector = HtmlCollector()
        extract = collector.collect_information(html)
        
        write = WriteFile()
        write.write(extract)
        
        Logger.logr.info(f"Finished automation")
