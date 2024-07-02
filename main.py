import psycopg2
import pandas as pd

def check_database_existence(database_name):
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='Dan23456',
            host='localhost',
            port='5432'
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (database_name,))
        exists = cur.fetchone()
        cur.close()
        conn.close()
        return bool(exists)
    except psycopg2.Error as e:
        print(f"Ошибка при проверке существования базы данных: {e}")
        return False

def create_database(database_name):
    # Подключение к серверу PostgreSQL (замените параметры подключения на ваши)
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='Dan23456',
        host='localhost',
        port='5432'
    )

    # Создание объекта курсора
    cur = conn.cursor()

    # Запрос имени новой базы данных у пользователя
    new_database_name = database_name

    # Завершение текущей транзакции
    conn.set_isolation_level(0)

    # SQL запрос для создания новой базы данных
    create_database_query = f"CREATE DATABASE {new_database_name};"

    # Выполнение SQL запроса
    cur.execute(create_database_query)

    # Подтверждение изменений
    conn.commit()

    # Закрытие курсора и соединения
    cur.close()
    conn.close()

    print(f"База данных '{new_database_name}' успешно создана.")

def excel_to_postgres(database_name, excel_file_path, sheet_number, table_name):
    conn = psycopg2.connect(
        dbname=database_name,
        user='postgres',
        password='Dan23456',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()

    xl = pd.ExcelFile(excel_file_path)
    sheet_names = xl.sheet_names
    selected_sheet_name = sheet_names[sheet_number - 1]
    df = xl.parse(selected_sheet_name)

    # Создание таблицы в базе данных PostgreSQL с типом данных VARCHAR для всех столбцов
    create_table_query = f'CREATE TABLE {table_name} ('
    for column in df.columns:
        column = column.replace(" ", "_")
        create_table_query += f'{column} VARCHAR, '
    create_table_query = create_table_query[:-2] + ');'  # Убираем лишнюю запятую и пробел перед закрывающей скобкой
    cur.execute(create_table_query)
    print(create_table_query)
    for row in df.itertuples(index=False):
        values = ", ".join([f"'{(value)}'" for value in row])
        insert_query = f"INSERT INTO {table_name} VALUES ({values});"
        cur.execute(insert_query)

    conn.commit()

    cur.close()
    conn.close()

    print(f"Данные из листа '{selected_sheet_name}' файла '{excel_file_path}' успешно загружены в таблицу '{table_name}' в базу данных.")

# Получение пользовательского ввода
database_name = input("Введите название базы данных PostgreSQL: ")
if (check_database_existence(database_name)==False):
    # Вызов функции для создания новой базы данных
    create_database(database_name)
excel_file_path = input("Введите путь к Excel файлу: ")
sheet_number = int(input("Введите номер листа Excel файла для загрузки данных (нумерация начинается с 1): "))
table_name = input("Введите имя таблицы, которую вы хотите создать в базе данных: ")

# Вызов функции для загрузки данных из указанного листа Excel файла в базу данных PostgreSQL
excel_to_postgres(database_name, excel_file_path, sheet_number, table_name)



