import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def create_result(self):
        """Создаем бд"""
        with self.connection:
            return self.cursor.execute("""
                                          CREATE TABLE "results" (
                                            "id"	INTEGER,
                                            "text"	TEXT,
                                            PRIMARY KEY("id" AUTOINCREMENT)
                                          )""")

    def add_result(self, text):
        """Добавляем новую запись в БД"""
        with self.connection:
            return self.cursor.execute(
                                        "INSERT INTO `results` (`text`) VALUES(?)",
                                        (text,))
