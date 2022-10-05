# def create_table():
#     """create tables in the PostgreSQL database"""
#     commands = (
#         """
#         CREATE TABLE infos (
#             type INT,
#             date BIGINT,
#             value FLOAT,
#             cpf BIGINT,
#             card TEXT,
#             hour VARCHAR(128),
#             owner CHAR(14),
#             store CHAR(19)
#         )
#         """,
#     )
#     conn = None
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="teste",
#             port=5432,
#             user="letlm",
#             password="123456",
#         )
#         cur = conn.cursor()

#         for command in commands:
#             cur.execute(command)

#         cur.close()
#         conn.commit()

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
