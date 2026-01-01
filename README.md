# ChatBot Sonar
# Link para acessar na web:
  https://chat-bot-eosin-three.vercel.app/
  
# Colaboradores:
  Nicolas-End: Fez o sistema de configuração do chatbot tanto no python quanto no javascript
  Ferreirar: estilizou a pagina e fez o sistema no javascript para mostrar a resposta do bot no lugar certo
# Descrição:
  Um chatbot que utiliza a API Cohere para gerar respostas a perguntas dos usuários sobre um projeto escolar, implementado em Python com Flask.

# Instalação:
  # Pre-Requisitos:
    python 3 ou superior 
    Pip (gerenciador de pacotes do Python)
    JavaScript (para funcionalidades no lado do cliente, se aplicável)
  # Passos Para Instalação:
    1- Clone esse Projeto:
       no git: git clone https://github.com/nimaste/ChatBot.git
    2-Navegue até o diretório do projeto:
      cd ChatBot
    3-Baixe os modulos necessarios:
       pip install -r requirements.txt
    4- Api Key:
      Coloque uma api key valida pelo site da corre em algum arquivo .env com o nome YOUR_COHERE_API_KEY
    5- Inicializando Projeto:
      Rode o arquivo Main.py e coloque no seu navegador o seguinte : http://127.0.0.1:8080 ou http://192.168.1.8:8080
**ChatBot**

Aplicação web simples em Flask que serve uma interface de chatbot com integrações locais em [cohere_connection](cohere_connection) (ex.: `co.py` e `gemini_response.py`). Fornece uma UI estática em [templates/index.html](templates/index.html) e recursos estáticos em [static/](static).

**Visão Geral**
- **Propósito:** Fornecer uma interface web para enviar mensagens a um modelo de chatbot e receber respostas em JSON.
- **Servidor web:** `Flask` servindo a rota principal `/` (UI) e a rota `POST /home` (API).

**Arquivos Principais**
- **`[main.py](main.py)`**: Ponto de entrada do servidor Flask. Executa a aplicação em `0.0.0.0:8080` por padrão.
- **`[cohere_connection](cohere_connection)`**: Conector local com `co.py`, `gemini_response.py` e `ChatBot_Presets.json`.
- **`[templates/index.html](templates/index.html)`**: Interface web para interação com o bot.
- **`[static/](static)`**: CSS, JS e imagens usados pela UI.
- **`Dockerfile`**: Imagem para containerizar a aplicação.
- **`requirements.txt`**: Dependências Python.

**Pré-requisitos**
- **Python:** 3.8+ (recomendado 3.10+)
- **pip** para instalar dependências
- **Docker** (opcional) para executar em container

**Instalação (local)**
1. Clonar o repositório.
2. Criar e ativar ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate     # Windows PowerShell
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Executar a aplicação:

```bash
python main.py
```

A aplicação ficará disponível em `http://localhost:8080/`.

**API**
- **GET /**: Serves UI (página principal).
- **POST /home**: Recebe formulário com campo `input_from_user` e devolve uma resposta JSON do chatbot.
  - **Parâmetro form:** `input_from_user` (string)
  - **Resposta:** JSON com o resultado retornado pelo conector (ex.: `co` ou `gemi`).

Exemplo em `curl`:

```bash
curl -X POST http://localhost:8080/home -F "input_from_user=Olá"
```

**Execução com Docker**
1. Build da imagem:

```bash
docker build -t chatbot:latest .
```

2. Rodar container (mapeando a porta 8080):

```bash
docker run chatbot:latest
```

**Configuração / Credenciais**
- As integrações com serviços (se houver) podem ser configuradas em `[cohere_connection/ChatBot_Presets.json](cohere_connection/ChatBot_Presets.json)` ou via variáveis de ambiente, dependendo da implementação em `co.py`/`gemini_response.py`.
- Verifique os arquivos em `[cohere_connection](cohere_connection)` para instruções específicas sobre chaves/segredos.

**Deploy**
- Há um arquivo `[vercel.json](vercel.json)` — caso deseje deploy em Vercel, ajuste conforme as instruções da plataforma e inclua build steps apropriados.

**Estrutura rápida do projeto**
- `main.py` — servidor Flask
- `Dockerfile` — containerização
- `requirements.txt` — dependências
- `templates/index.html` — UI
- `static/` — assets (CSS/JS/imagens)
- `cohere_connection/` — lógica do chatbot

**Contribuições**
- Abra uma issue para discutir mudanças maiores.
- Pull requests são bem-vindas para correções e melhorias.


