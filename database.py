import sqlite3


def connect():
    user_db = sqlite3.connect('users.db')
    user_cursor = user_db.cursor()
    return user_db, user_cursor


def create_db():
    db, cursor = connect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY,
                    group_id INT,
                    notification INT
                )""")
    db.commit()


def update_db(message, update_line, value, post_id=0, user=True):
    if user:
        db, cursor = connect()
        cursor.execute(f"""UPDATE users SET {update_line} = {value} WHERE id ={message.chat.id}""")
        db.commit()
    else:
        db, cursor = connect()
        cursor.execute(f"""UPDATE article SET {update_line} = {value} WHERE id ={post_id}""")
        db.commit()
