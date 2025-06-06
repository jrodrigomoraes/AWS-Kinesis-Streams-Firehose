# -*- coding: utf-8 -*-
"""ProdutorKinesisFireHose.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aLdzpbb75hUKAJjyE4_s4v-3VouqGLTM
"""



"""# Programa de Streaming de Entrega

## Cliente

Agora o consumidor não será mais um aplicativo python, e sim o Kinesis Firehose que irá realizar a entrega!

Nesse caso, vamos definir que ele fará a entrega em um bucket S3, dentro da própria AWS.

Não é preciso codificar nada.
"""

from dotenv import load_dotenv
import os
import boto3
import json

load_dotenv()

cliente = boto3.client('kinesis',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION'))


#Vamos serializar os dados. No registro, terá os dados que quero que seja serializado
#Abaixo os dados são ficticíos.


registro = {'idvendedor': '1000', 'nome': 'José'}

#Vamos produzir a informação
resposta = cliente.put_record(
    StreamName='stream1',
    Data=json.dumps(registro),
    PartitionKey='1'
)

#Verificando
print(resposta)

