import psycopg2


def read_cnab(database_path):
    with open(database_path, "r") as cnab:
        for key in cnab:
            tipo = key[0]
            date = key[1:8]
            valor = int(key[9:18]) / 100
            print(valor)
            CPF = key[19:29]
            Cartao = key[30:41]
            hora = key[42:47]

            # ipdb.set_trace()
            dono = key[48:61]
            loja = key[62:81]


def create_table():
    """create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE infos (
            type INT,
            date BIGINT,
            value FLOAT,
            cpf BIGINT,
            card TEXT,
            hour VARCHAR(128),
            owner CHAR(14),
            store CHAR(19)
        )
        """,
    )
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="teste",
            port=5432,
            user="letlm",
            password="123456",
        )
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def inserir_db():
    conn = psycopg2.connect(
        host="localhost",
        database="teste",
        port=5432,
        user="letlm",
        password="123456",
    )
    cur = conn.cursor()
    try:

        with open("CNAB.txt", "r") as Lines:
            for line in Lines:
                tipo = line[0]
                data = line[1:9]
                valor = int(line[9:19]) / 100
                cpf = line[19:30]
                cartao = line[30:42]
                hora = line[42:48]
                dono = line[48:62]
                loja = line[62:81]

                insert = f"""INSERT INTO infos(type, date, value, cpf, card, hour, owner, store) VALUES ({tipo},{data},{valor},{cpf},'{cartao}',{hora},'{dono}','{loja}')"""

                cur.execute(insert)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        return 1
    cur.close()
