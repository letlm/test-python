## Instalação


- Clone este repositório:
  `git clone git@github.com:letlm/test-python.git`

- Entrar no projeto pelo editor de código e rode os seguintes comandos:
  
  `python -m venv venv`

  `source venv/bin/activate`

  `python -m venv venv`

  `pip install -r requirements.txt`

- Em seguida, crie um arquivo .env na raiz do projeto com as configurações que estão de exemplo no arquivo .env.example. Coloque as suas informações nos campos.  </br>
  ![App Screenshot](https://i.imgur.com/ka8r58j.png)

- Crie um arquivo database.ini na raiz do projeto com as configurações que estão de exemplo no arquivo .database.example.ini. Coloque as suas informações nos campos.
  ![App Screenshot](https://i.imgur.com/kfwO86q.png)

- Após a criação dos arquivos, rode no terminal:

  `python manage.py migrate`

- E então:

  `python manage.py runserver`


- A aplicação estará rodando na porta `http://127.0.0.1:8000/`

- Abra outro terminal, sem parar a execução da aplicação e rode o seguinte comando para criar um superusuário. Coloque as informações que serão pedidas:
  
  `python manage.py createsuperuser`

- Após, acesse o endpoint /admin: `http://127.0.0.1:8000/admin` e coloque as credenciais que você acabou de criar e faça seu login:
  
  ![App Screenshot](https://i.imgur.com/rPBbCp9.png)


- Você será redirecionado para a seguinte tela, então é só clicar em Add em Files para poder adicionar seu arquivo CNAB
  
  ![App Screenshot](https://imgur.com/d1LuM5c.png)


- Então é só clicar em escolher arquivo e carregar o seu arquivo CNAB.txt e clicar em 'SAVE'. OBS: na raiz do projeto há um arquivo CNAB.txt, você pode salvar ele em sua máquina e então carregar ele para testar.
  ![App Screenshot](https://imgur.com/SuBfvHm.png)

- Em seguida, para visualizar os dados do seu arquivo que foram inseridos na aplicação é só acessar o endpoint api/cnabs/: `http://127.0.0.1:8000/api/cnabs/`
  ![App Screenshot](https://i.imgur.com/ks77J9R.png)
