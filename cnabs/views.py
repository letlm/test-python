import psycopg2
from config import config
from files.models import FileCnab
from rest_framework.views import APIView, Request, Response

from cnabs.models import InfosTable
from cnabs.serializer import CnabsSerializer


class ReturnInfos(APIView):
    def get(self, request: Request) -> Response:

        upload_file = FileCnab.objects.all()
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        try:
            for key in upload_file:
                with open(key.file.path, "r") as Lines:
                    for line in Lines:
                        tipo = line[0]
                        data = line[1:9]
                        lst = list(data)
                        data_format = f"{lst[0]}{lst[1]}{lst[2]}{lst[3]}-{lst[4]}{lst[5]}-{lst[6]}{lst[7]}"
                        valor = int(line[9:19]) / 100
                        cpf = line[19:30]
                        cartao = line[30:42]
                        hora = line[42:48]
                        lst_h = list(hora)
                        hora_format = f"{lst_h[0]}{lst_h[1]}:{lst_h[2]}{lst_h[3]}:{lst_h[4]}{lst_h[5]}"
                        dono = line[48:62]
                        loja = line[62:80]

                        query = f"""INSERT INTO cnabs_infostable(type, date, value, cpf, card, hour, owner, store) VALUES ({tipo},'{data_format}',{valor},{cpf},'{cartao}','{hora_format}','{dono}','{loja}')"""

                        cur.execute(query)

                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            cur.close()

            return 1
        cur.close()

        table = InfosTable.objects.all()
        serializer = CnabsSerializer(table, many=True)

        return Response(serializer.data)
