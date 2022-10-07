import psycopg2
from files.models import FileCnab
from rest_framework.views import APIView, Request, Response

from cnabs.models import InfosTable
from cnabs.serializer import CnabsSerializer


class ReturnInfos(APIView):
    def get(self, request: Request) -> Response:

        upload_file = FileCnab.objects.all()

        conn = psycopg2.connect(
            host="localhost",
            database="teste",
            port=5432,
            user="letlm",
            password="123456",
        )
        cur = conn.cursor()
        try:

            with open(upload_file[0].file.path, "r") as Lines:

                for line in Lines:
                    tipo = line[0]
                    data = line[1:9]
                    valor = int(line[9:19]) / 100
                    cpf = line[19:30]
                    cartao = line[30:42]
                    hora = line[42:48]
                    dono = line[48:62]
                    loja = line[62:81]

                    query = f"""INSERT INTO cnabs_infostable(type, date, value, cpf, card, hour, owner, store) VALUES ({tipo},{data},{valor},{cpf},'{cartao}',{hora},'{dono}','{loja}')"""

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
