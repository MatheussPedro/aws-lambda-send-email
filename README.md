## Envio de E-mails com Amazon SES

Este projeto consiste em uma função AWS Lambda escrita em Python que utiliza o serviço Amazon SES (Simple Email Service) para enviar e-mails com base em dados recebidos via JSON. A função foi criada como parte do trabalho da disciplina **Arquitetura em Cloud**.

A função recebe uma entrada JSON contendo `name`, `email` e `message`, e envia um e-mail com essas informações usando o Amazon SES.

---

## Saída

A resposta será um JSON com:

- `statusCode: 200` se o e-mail for enviado com sucesso.
- `statusCode: 500` se houver algum erro no envio.

---

## Dependências

- **AWS Lambda**
- **Amazon SES** (na região `us-east-1`)
- **Permissões IAM** para `ses:SendEmail`
- **boto3** (já incluso nas Lambdas em Python)

---

## Como configurar e testar

URL da função (https://6waurgqcjqijy6rcx5xfow5m4a0cvnza.lambda-url.us-east-1.on.aws/)

### 1. Verifique os e-mails no SES
Se sua conta estiver no **modo sandbox**, você precisa **verificar tanto o remetente quanto o destinatário** ou você pode colocar o source e destination iguais.

- Acesse o [Amazon SES Console](https://console.aws.amazon.com/ses/home?region=us-east-1)
- Vá em **"Verified identities"**
- Verifique seu e-mail remetente e os e-mails que vão receber

### 2. Configure o código da Lambda

Altere os campos abaixo no código:

```python
Source='seuemailverificado@dominio.com',
Destination={'ToAddresses': ['destinatario@dominio.com']},
```

### 3. Teste a função

No console da AWS Lambda, clique em **"Test"** e insira este exemplo de evento:

```json
{
  "name": "Matheus",
  "email": "matheusrizo@gmail.com",
  "message": "Olá, isso é um teste da função Lambda!"
}
```

Se estiver tudo certo, você verá:

```json
{
  "statusCode": 200,
  "body": "\"Email enviado com sucesso!\""
}
```