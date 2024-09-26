import psycopg2
import schedule
import os

_host = os.getenv('host')
_database = os.getenv('database')
_password = os.getenv('password')
_port = os.getenv('port')
_user = os.getenv('user')

def verificar_status_banco():
    try:
        connection = psycopg2.connect(
            host=_host,
            database=_database,
            password=_password,
            port=_port,
            user=_user
        )
        context = connection.cursor()
        context.execute('SELECT 1')
        rows = context.fetchall()
        if rows[0][0]==1:
            print("Servidor funcionando normalmente")
    except Exception as ex:
        print ("Erro ao se conectar ao banco...")
    finally:
        if context:
            context.close()
        if connection:
            connection.close()
print('StartService')
schedule.every(3).hours.do(verificar_status_banco)

while True:
    schedule.run_pending()