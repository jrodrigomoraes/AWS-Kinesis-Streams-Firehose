# Projeto de Streaming com AWS Kinesis e Python

Este projeto demonstra duas abordagens diferentes para ingestão de dados em tempo real usando AWS Kinesis:

- **Kinesis Streams + Consumidor Python**
- **Kinesis Streams + Firehose + Entrega automática para S3**

## 🧪 Casos de Uso

1. Produção e consumo de eventos diretamente via Streams.
2. Produção de eventos via Streams que são posteriormente entregues ao S3 via Firehose.

## 🚀 Tecnologias

- Python
- AWS Kinesis (Streams, Firehose)
- AWS S3
- boto3
- dotenv

## 🎯 Objetivo

Desenvolver um pipeline de ingestão e processamento de dados em tempo real utilizando AWS, com foco na comparação entre Kinesis Streams e Kinesis Firehose:

1. **Produtor (Python)** envia dados no formato JSON para um Kinesis Stream.
2. **Consumidor (Python)** lê os dados diretamente do Stream, aplica lógica de deduplicação e simula processamento em tempo real.
3. **Firehose** consome dados do Stream e realiza a entrega automática em um bucket S3.
4. Os dados armazenados no S3 podem ser utilizados posteriormente para análises, cargas em Data Lakes ou integrações com ferramentas de BI.

O projeto também permite observar as diferenças de latência e comportamento entre Streams e Firehose.

## 📁 Estrutura

```bash
aws-kinesis-streaming-case/
│
├── producer_stream/ -> Produtor que envia para Kinesis Stream
├── consumer_stream/ -> Consumidor Python do Stream
├── producer_firehose/ -> Produtor que envia para Firehose (via Stream)
```

