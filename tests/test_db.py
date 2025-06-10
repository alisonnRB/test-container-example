from testcontainers.mysql import MySqlContainer # type: ignore
from sqlalchemy import text # type: ignore

#importa a função necessaria para se conectar ao DB containerizado
from app.db import init_db

def test_mysql_container():

    #prepara um container com mysql para realizar os testes de integração
    with MySqlContainer("mysql:8.0") as mysql:

        # Passa a conexão com o BD criado para nossa função que cria as tabelas
        engine = init_db(mysql.get_connection_url())

        # Verifica se estão salvas os nomes que deveriam estar na tabela
        with engine.connect() as conn:

            #faz a consulta
            result = conn.execute(text("SELECT name FROM users ORDER BY id"))

            #cria uma lista de resultados da consulta
            names = [row[0] for row in result]

            #compara os valores
            assert names == ["Alice", "Bob"]
