from sqlalchemy import create_engine, text

class SubjectTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def insert(self, subject_id, subject_title):
        connection = self.db.connect()
        transaction = connection.begin()
        sql = text("INSERT INTO subject (subject_id, subject_title)" 
               "VALUES (:new_id, :new_name)")
        connection.execute(sql, {"new_id": subject_id, "new_name": subject_title})
        transaction.commit()
        connection.close()


    def update(self, subject_id, subject_title):
        connection = self.db.connect()
        transaction = connection.begin()
        sql = text("UPDATE subject SET subject_title = :new_name WHERE subject_id = :id")
        connection.execute(sql, {"new_name": subject_title, "id": subject_id})
        transaction.commit()
        connection.close()


    def delete(self, subject_id):
        connection = self.db.connect()
        transaction = connection.begin()
        sql = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql, {"id": subject_id})
        transaction.commit()
        connection.close()


    def get_max_id(self):
        connection = self.db.connect()
        sql = text("SELECT MAX (subject_id) FROM subject")
        result = connection.execute(sql)
        max_id = result.scalar()
        connection.close()
        return max_id
        