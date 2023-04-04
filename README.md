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

## Próximos passos

- [ ] Implementar Web scraping
  - [x] Criar código para raspar o site
  - [x] Alimentar planilha com resultado da raspagem
  - [ ] Configurar Pipedream para chamar código 1x por dia
- [ ] Implementar envio de emails
  - [ ] Coletar dados que foram raspados na planilha
  - [ ] Coletar emails de quem se cadastrou
  - [ ] Enviar emails
  - [ ] Configurar Pipedream para chamar 1x por semana
