# Bot de Telegram para Cardápio Diário do Restaurante Universitário da UFRN

## Descrição do Projeto

Este repositório contém o código-fonte de um bot para Telegram que realiza web scraping da página do Restaurante Universitário (RU) da Universidade Federal do Rio Grande do Norte (UFRN) - [ru.ufrn.br](https://ru.ufrn.br/). O objetivo do bot é coletar e enviar o cardápio diário do restaurante diretamente no chat do Telegram de qualquer usuário interessado.

### Funcionalidades

- **Web Scraping**: O bot utiliza técnicas de web scraping para extrair as informações do cardápio diretamente do site oficial do RU.
- **Atualizações Diárias**: As informações são atualizadas em tempo-real, garantindo que os usuários tenham sempre o cardápio mais recente.
- **Interface Simples**: Interação amigável e intuitiva através do Telegram e comandos simples de uso, facilitando o acesso às informações do RU.

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando a linguagem Python e faz uso das seguintes bibliotecas:

- **beautifulsoup4**: Utilizada para realizar o web scraping e extrair as informações desejadas do HTML da página.
- **requests**: Utilizada para fazer requisições HTTP ao site do RU.
- **python-telegram-bot**: Utilizada para integrar o bot com a API do Telegram e enviar mensagens aos usuários.

## Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie um ambiente virtual e ative-o**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o token do bot de ambiente**:
    No arquivo main.py, configure seu token de bot do telegram
    ```env
    TELEGRAM_TOKEN=seu-token-do-telegram
    ```

5. **Execute o bot**:
    ```bash
    python bot.py
    ```

## Contribuições

Contribuições são bem-vindas! Se você tiver alguma ideia de melhoria ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.


Espero que este bot seja útil para todos os estudantes da UFRN que utilizam o Restaurante Universitário. Aproveite e bom apetite!

## Autoria

Projeto desenvolvido por Lisandra Melo (<lisandramelo34@gmail.com>).

&copy; IMD/UFRN 2023.
