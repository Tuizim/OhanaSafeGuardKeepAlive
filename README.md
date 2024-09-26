# ohanaSafeguard - DbKeepAlive

![Status Check](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12%2B-316192)

**ohanaSafeguard - DbKeepAlive** é um projeto destinado a monitorar o status do servidor PostgreSQL periodicamente. Ele utiliza a biblioteca `schedule` para executar verificações regulares e garantir que o banco de dados esteja sempre ativo e funcional.

## ⚙️ Funcionalidades

- **Monitoramento Regular**: Verifica o status do servidor PostgreSQL em intervalos regulares configuráveis.
- **Notificações Simples**: Informa no console o status atual do banco de dados.
- **Facilidade de Configuração**: Fácil de configurar para uso em diferentes ambientes de desenvolvimento.

## 🚀 Tecnologias Utilizadas

- **Python 3.7+**
- **psycopg2**: Para conectar e interagir com o banco de dados PostgreSQL.
- **schedule**: Para agendar verificações periódicas do status do banco.
