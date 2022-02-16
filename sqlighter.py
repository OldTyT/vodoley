import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def create_result(self):
        """Проверяем, есть ли уже пост в базе"""
        with self.connection:
            self.cursor.execute("""
                                                            CREATE TABLE "results" (
                                                                "id"	INTEGER,
                                                                "text"	TEXT,
                                                                "no_text"	TEXT,
                                                                PRIMARY KEY("id" AUTOINCREMENT)
                                                            )""")
        return False

    def add_result(self, text):
        """Добавляем новый пост в БД"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `results` (`text`, `no_text`) VALUES(?,?)", (text, 1))
            #return self.cursor.execute("INSERT INTO `results` (`text`,) VALUES(?,)", (text, 1))
