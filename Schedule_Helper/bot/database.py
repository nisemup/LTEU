import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / "settings" / ".env")


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'),
                                     password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'))
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

    def get_faculty(self):
        self.cursor.execute("""SELECT DISTINCT faculty FROM backend_groups""")
        return sorted([key[0] for key in self.cursor.fetchall()])

    def get_gnum(self, faculty):
        self.cursor.execute("""SELECT gnum FROM backend_groups WHERE faculty = %s""", (faculty, ))
        return sorted([key[0] for key in self.cursor.fetchall()])

    def get_gid(self, faculty, gnum):
        self.cursor.execute("""SELECT gid FROM backend_groups WHERE faculty = %s AND gnum = %s""", (faculty, gnum))
        return self.cursor.fetchone()[0]

    def create_user(self, uid, gid, username=None):
        self.cursor.execute("""
            INSERT INTO backend_profiles (user_id, username, group_id, notification)
            VALUES (%s, %s, %s, True) 
            ON CONFLICT (user_id) 
            DO UPDATE SET
                username = EXCLUDED.username,
                group_id = EXCLUDED.group_id;
        """, (uid, username, gid))
        self.conn.commit()
        return True

    def get_admins(self):
        self.cursor.execute("""SELECT user_id FROM backend_profiles WHERE is_admin = True""")
        return [key[0] for key in self.cursor.fetchall()]

    def get_moderators(self):
        self.cursor.execute("""SELECT user_id FROM backend_profiles WHERE is_moderator = True""")
        return [key[0] for key in self.cursor.fetchall()]

    def get_notification(self, uid):
        self.cursor.execute("""SELECT notification FROM backend_profiles WHERE user_id = %s""", (uid, ))
        return self.cursor.fetchone()[0]

    def update_notification(self, uid, data):
        state = False if data else True
        self.cursor.execute("""UPDATE backend_profiles SET notification = %s WHERE user_id = %s""", (state, uid))
        self.conn.commit()
        return True

    def get_group(self, uid):
        self.cursor.execute("""SELECT group_id FROM backend_profiles WHERE user_id = %s""", (uid, ))
        return self.cursor.fetchone()[0]

    def get_schedule(self, gid, week_type):
        self.cursor.execute("""
            SELECT day, number, name, start_time, end_time, classroom, url
            FROM backend_schedule WHERE group_id = %s AND week_type = %s
        """, (gid, week_type))
        return self.cursor.fetchall()
