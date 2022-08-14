import sqlite3
import hashlib


# TODO: make exception


class Database:

    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()

    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INT PRIMARY KEY,
                        group_id CHAR(20),
                        notification TINYINT
                    )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS schedule (
                                id INT PRIMARY KEY,
                                group_id CHAR(20),
                                day CHAR,
                                number TINYINT,
                                type CHAR(2),
                                start_time TIME,
                                end_time TIME,
                                title CHAR,
                                classroom CHAR
                            )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS groups (
                                        id CHAR(20) PRIMARY KEY,
                                        faculty CHAR,
                                        group_num TINYINT
                                    )""")
        self.con.commit()

    @staticmethod
    def create_gid(faculty, group):
        fac_hash = hashlib.sha256(faculty.encode('UTF-8')).hexdigest()
        group_hash = hashlib.sha256(group.encode('UTF-8')).hexdigest()
        return fac_hash[:10] + group_hash[:10]

    def create_group(self, gid, faculty, group_num):
        try:
            self.cursor.execute("""INSERT INTO groups VALUES (?, ?, ?)""", (gid, faculty, group_num))
            self.con.commit()
        except BaseException as er:
            print(er)
            return None

    def create_user(self, uid, gid):
        try:
            self.cursor.execute("""INSERT INTO users VALUES (?, ?, ?)""", (uid, gid, 1))
            self.con.commit()
        except BaseException as er:

            print(er)
            return None

    def select_gid(self, faculty, group_num):
        try:
            self.cursor.execute(f"""
                SELECT id FROM groups WHERE faculty = '{faculty}' AND group_num = '{group_num}'
            """)
            return self.cursor.fetchone()
        except BaseException as er:
            print('2')
            print(er)
            return None

    def select_distinct(self, item, table, line=None, value=None, where=False):
        try:
            self.cursor.execute(f"""
                SELECT DISTINCT {item} FROM {table} {f"WHERE {line} = '{value}'" if where else ''} 
            """)
            return self.cursor.fetchall()
        except BaseException as er:
            print(er)
            pass

    def select_all(self, table):
        try:
            self.cursor.execute(f"""SELECT * FROM {table}""")
            return self.cursor.fetchall()
        except BaseException as er:
            print(er)
            return None

    def select_db(self, item, table, line, value):
        try:
            self.cursor.execute(f""" SELECT {item} FROM {table} WHERE {line} = '{value}'""")
            return self.cursor.fetchone()
        except BaseException as er:
            print('1')
            print(er)
            return None

#    def select_te(self, value):
#        try:
#            self.cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = {value}""")
#            return self.cursor.fetchall()
#        except BaseException:
#            pass

    def update_db(self, table, update_line, update_value, line, value):
        try:
            self.cursor.execute(f"""
                UPDATE {table} SET {update_line} = '{update_value}' WHERE {line} = '{value}'
            """)
            self.con.commit()
        except BaseException as er:
            print(er)
            return None
