import json

import psycopg2
from django.shortcuts import render
from files.models import FileCnab
from rest_framework.views import APIView, Request, Response, status


class GetTable(APIView):
    def get(self, request) -> Response:
        upload_file = FileCnab.objects.all()

        with open(upload_file[0], "r") as file:
            import ipdb

            ipdb.set_trace()
            return json.load(file)

        teste = upload_file[0]

        # conn = psycopg2.connect(
        #     host="localhost",
        #     database="teste",
        #     port=5432,
        #     user="letlm",
        #     password="123456",
        # )
        # cur = conn.cursor()
        # try:

        #     with open(teste, "r") as Lines:
        #         for line in Lines:
        #             tipo = line[0]
        #             data = line[1:9]
        #             valor = int(line[9:19]) / 100
        #             cpf = line[19:30]
        #             cartao = line[30:42]
        #             hora = line[42:48]
        #             dono = line[48:62]
        #             loja = line[62:81]

        #             insert = f"""INSERT INTO cnabs_infostable(type, date, value, cpf, card, hour, owner, store) VALUES ({tipo},{data},{valor},{cpf},'{cartao}',{hora},'{dono}','{loja}')"""

        #             cur.execute(insert)
        #     conn.commit()

        # except (Exception, psycopg2.DatabaseError) as error:
        #     print("Error: %s" % error)
        #     conn.rollback()
        #     cur.close()
        #     return 1
        # cur.close()

        # return Response
