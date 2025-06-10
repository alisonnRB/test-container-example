from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert # type: ignore

# função que cria as tabelas no banco de dados
def init_db(connection_url):
    connection_url = connection_url.replace("mysql://", "mysql+pymysql://")
    engine = create_engine(connection_url)
    metadata = MetaData()

    users = Table(
        "users", metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(50))
    )

    metadata.create_all(engine)  # Cria a tabela

    #se conecta ao DB com a conexão passada por paramentro
    with engine.connect() as conn:

        # Limpar a tabela caso tenha algo
        conn.execute(users.delete())

        # Insere os dados na database
        conn.execute(insert(users), [{"name": "Alice"}, {"name": "Bob"}])
        conn.commit()  # Commit para salvar

    return engine #retorna a DB

