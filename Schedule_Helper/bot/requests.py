import psycopg2


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