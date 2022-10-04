from cnabs_test.cnab_handler import create_table, inserir_db

DATABASE_PATCH = "CNAB.txt"


def main():

    # try:

    create_table()
    inserir_db()


# except json.JSONDecodeError:
#     return []
# except FileNotFoundError:
#     return []


if __name__ == "__main__":
    main()
