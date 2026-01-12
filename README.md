# Projeto Scraper API

Este projeto tem como objetivo realizar **web scraping de processos e informações públicas** (inicialmente foi pensado para mapear os processos da Detic/Unicamp ou estruturas similares), organizando os dados coletados de forma estruturada e expondo-os por meio de uma **API REST construída com FastAPI**.

A arquitetura foi pensada desde o início para permitir:

* Evolução gradual do crawler
* Validação e padronização de dados com Pydantic
* Testes e inspeção via Swagger
* Possível expansão futura (persistência, autenticação, filas, etc.)

O projeto combina o espírito explorador do scraping com a disciplina de uma API moderna. 🕷️➡️📦

---

## 🧭 Visão Geral da Arquitetura

```
project_root/
├── app/
│   ├── main.py            # Ponto de entrada FastAPI
│   ├── core/              # Configurações globais
│   ├── routers/           # Rotas da API (crawler, healthcheck, etc.)
│   ├── services/          # Lógica de scraping e processamento
│   └── utils/             # Funções auxiliares
│
├── tests/                 # Testes automatizados
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** – Framework web moderno e performático
* **Pydantic** – Validação e serialização de dados
* **Requests / HTTPX** – Requisições HTTP
* **BeautifulSoup / lxml** – Parsing de HTML
* **Uvicorn** – Servidor ASGI

(Dependendo da evolução do projeto, outras bibliotecas como Scrapy, Playwright ou Selenium podem ser incorporadas.)

---

## 📦 Instalação (usando Poetry)

Este projeto utiliza **Poetry** para gerenciamento de dependências e ambientes virtuais, garantindo reprodutibilidade e isolamento.

### Pré-requisitos

* Python **3.10 ou superior**
* Poetry instalado

Caso ainda não tenha o Poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Ou, se preferir via `pipx`:

```bash
pipx install poetry
```

### Passos de instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/spiders-from-mars.git
cd spiders-from-mars
```

2. Configure o Poetry para criar o ambiente virtual no projeto (opcional, mas recomendado):

```bash
poetry config virtualenvs.in-project true
```

3. Instale as dependências:

```bash
poetry install
```

---

## ▶️ Executando o Projeto

Após a instalação via Poetry, existem duas formas principais de executar a aplicação.

### Opção 1: Usando `poetry run`

```bash
poetry run uvicorn app.main:app --reload
```

### Opção 2: Ativando o shell do Poetry

```bash
poetry shell
uvicorn app.main:app --reload
```

A API ficará disponível em:

* **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* Documentação Swagger: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
* Redoc: **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)**

Durante o desenvolvimento, o modo `--reload` reinicia automaticamente o servidor a cada alteração de código.

---

## 🧪 Testando o Crawler

O projeto já inclui um **router dedicado ao crawler**, permitindo testar o scraping diretamente pelo Swagger.

Exemplo de rota:

```
POST /crawler/run
```

Essa rota pode:

* Receber parâmetros como URL alvo, filtros ou identificadores
* Executar o scraping
* Retornar os dados estruturados (JSON)

Sites recomendados para testes iniciais de scraping:

* [https://quotes.toscrape.com](https://quotes.toscrape.com)
* [https://books.toscrape.com](https://books.toscrape.com)

Esses sites são feitos especificamente para testes e evitam problemas legais ou éticos.

---

## 📐 Modelagem de Dados

Os dados coletados são validados e serializados usando **Pydantic**, garantindo:

* Tipagem explícita
* Estruturas previsíveis
* Facilidade de integração futura com banco de dados ou mensageria

Exemplo conceitual:

```python
class Processo(BaseModel):
    numero: str
    titulo: str
    data_publicacao: date
    url_origem: HttpUrl
```

---

## 🔒 Boas Práticas e Ética

* Respeite o `robots.txt` dos sites
* Evite sobrecarregar servidores
* Use delays e headers adequados
* Scrape apenas dados públicos e permitidos

Este projeto tem finalidade educacional e experimental.

---

## 🛣️ Próximos Passos Planejados

* Persistência dos dados (PostgreSQL / SQLite)
* Execução assíncrona de crawlers
* Agendamento de coletas
* Versionamento de resultados
* Autenticação e controle de acesso
* Logs estruturados e métricas

---

## 🧠 Observação Final

Este projeto foi estruturado para crescer sem tropeçar nos próprios fios. Começa simples, mas já fala a língua de sistemas maiores.

Se o scraper é a aranha, o FastAPI é a teia. 🕸️

