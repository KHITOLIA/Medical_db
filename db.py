import mysql.connector as sql
import os


class Database:
    def __init__(self):
        self.conn = sql.connect(
            host = '127.0.0.1',
            port = '3306',
            user = 'root',
            password = 'Tushar@2000',
            database = 'md_db'
        )
        self.cursor = self.conn.cursor()
        print(f"Connection build")
    
        # step 2: Create a new table for predition data
        self.cursor.execute(f"""create table if not exists predictions(
            id int auto_increment primary key,
            age int,
            sex varchar(10),
            bmi float,
            children int,
            smoker varchar(10),
            region varchar(20),
            prediction float)
        """)

    def save_predictions(self, age, sex, bmi, children, smoker, region, prediction):
        pred = float(prediction)
        query = '''
        insert into predictions(age, sex, bmi, children, smoker, region, prediction)
        values(%s, %s, %s, %s, %s, %s, %s)'''

        self.cursor.execute(query, (age, sex, bmi, children, smoker, region, prediction))
        self.conn.commit()