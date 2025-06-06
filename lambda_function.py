import json
import boto3

ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        name = event['name']
        email = event['email']
        message = event['message']
        
        response = ses.send_email(
            Source='seu-email-verificado@dominio.com',
            Destination={'ToAddresses': ['destinatario@dominio.com']},
            Message={
                'Subject': {'Data': f'Nova mensagem de {name}'},
                'Body': {'Text': {'Data': f'{message}\n\nDe: {name} <{email}>'}}
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Email enviado com sucesso!')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro: {str(e)}')
        }
