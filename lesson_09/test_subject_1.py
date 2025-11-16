from Subject_table import SubjectTable


db = SubjectTable("postgresql://postgres:1538@localhost:5432/QA")

# Добавление записи в таблицу subject и удаление созданной записи
def test_create():
    subject_id = 17
    subject_title = 'Drawing'
    db.insert(subject_id, subject_title)
    max_id = db.get_max_id()
    db.delete(max_id)

# Добавление, изменение и удаление записи из таблицы subject
def test_update():
    subject_id = 17
    subject_title = 'Drawing'
    db.insert(subject_id, subject_title)
    subject_id = 17
    subject_title = 'NewDrawing'
    db.update(subject_id, subject_title)
    max_id = db.get_max_id()
    db.delete(max_id)


# Удаление записи из таблицы subject по ID
def test_delete():
    subject_id = 13
    db.delete(subject_id)
