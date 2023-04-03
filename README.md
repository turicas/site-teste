# site-teste

Esse repositório é um **site** que possui:

- Robô do [Telegram](https://telegram.org/)
- Integração com o Google Sheets
- Site em Flask
- ...

## Configuração inicial

Não se esqueça de:

- Criar uma *service account* no Google Cloud
- Criar o *token* do seu robô no Telegram
- Configurar o `setWebhook` do Telegram

### Configurando o webhook do Telegram

Execute o seguinte código:

```
import requests

token = "SEU TOKEN"
url = "https://site-teste-turicas.onrender.com/telegram-bot"
response = requests.post(f"https://api.telegram.org/bot{token}/setWebhook", data={"url": url})
print(response.text)
```
