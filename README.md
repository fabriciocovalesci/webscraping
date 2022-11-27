## WEb Scraping


Dentro da pasta [algoritmos](https://github.com/fabriciocovalesci/webscraping/tree/main/algoritmos "algoritmos") contém os dois exercicios de lógica.

O código do web scraping está na pasta **/src** e o arquivo **main.py** é utilizado como inicializador da automação.

Pensando em manter os módulos de **service**, **extract**, **infra** individuais, foi desenvolvido classes para encapsular as responsabilidades.

O módulo [service](https://github.com/fabriciocovalesci/webscraping/tree/main/src/service "service") realiza a requisição para o site obtendo o html, atravéz da biblioteca [requests](https://pypi.org/project/requests/ "requests"). Caso seja necessário substituir a *lib*,  apenas será preciso sobrescrever a classe [HttpRequest](https://github.com/fabriciocovalesci/webscraping/tree/main/algoritmos "HttpRequest").

O módulo [extract](https://github.com/fabriciocovalesci/webscraping/tree/main/src/extract "extract") faz a extração do HTML com a *lib* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/ "BeautifulSoup"), caso seja preciso substituir a lib, deve se  sobrescrever a classe [HtmlCollector](https://github.com/fabriciocovalesci/webscraping/blob/main/src/extract/collector.py "HtmlCollector"). 
Foi definido um contrato por meio do **namedtuple**, que a classe **HtmlCollector** deve retornar uma lista com os seguintes campos: **nome, capital, populacao, area**.

O módulo [infra](https://github.com/fabriciocovalesci/webscraping/tree/main/src/infra "infra") é responsável por armazenar os dados em ***csv***, e salva dos dados dentro da pasta [data](https://github.com/fabriciocovalesci/webscraping/tree/main/data "data").

Foi desenvolvido logs para acompanhar todos os procedimentos que a automação faz, os logs são salvos dentro da pasta [src/logs](https://github.com/fabriciocovalesci/webscraping/tree/main/src/logs "src/logs")

O arquivo [start.py](https://github.com/fabriciocovalesci/webscraping/blob/main/src/start.py "start.py"). contém a classe **Start** que centraliza os imports, entre os módulos.

#### Como executar a automação local

1 - Clone repositório:

    git clone https://github.com/fabriciocovalesci/webscraping.git

2 - Acesse pasta webscraping

    cd webscraping

3 - Crie virtual env

    python3 -m venv venv

4 - Ative virtual env

    source venv/bin/activate

5 - Instale as dependências

    pip3 install -r requirements.txt
    
6 - Execute a automação

    python3 main.py

#### Como executar a automação com Docker

1 - Clone repositório:

    git clone https://github.com/fabriciocovalesci/webscraping.git

2 - Acesse pasta webscraping

    cd webscraping
 
3 - Faz o build da imagem

    docker build -t raspador .

4 - Execute o container 

OBS: Escolha caminho de uma pasta do seu computador para acessar volume do container, para acessar o arquivo csv gerado.

    docker run -v <CAMINHO DA PASTA DO SEU DESKTOP>:/app/data -it raspador
