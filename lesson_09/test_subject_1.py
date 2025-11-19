from Subject_table import SubjectTable


db = SubjectTable("postgresql://postgres:1538@localhost:5432/QA")

# Добавление записи в таблицу subject и удаление созданной записи
def test_create():
    # создаём новую запись в таблице
    max_id = db.get_max_id()
    subject_id = max_id + 1
    subject_title = 'Drawing'
    db.insert(subject_id, subject_title)
    # проверяем, что новый ID созданной записи больше чем максимальный ID таблицы
    # до создания записи, ноая запись в таблице создалась
    new_max_id = db.get_max_id()
    assert new_max_id > max_id
    # удаляем созданную запись (подчищаем за собой таблицу)
    db.delete(subject_id)

# Добавление, изменение и удаление записи из таблицы subject
def test_update():
    # создаём новую запись в таблице
    max_id = db.get_max_id()
    subject_id = max_id + 1
    subject_title = 'Drawing'
    db.insert(subject_id, subject_title)
    # изменяем созданную запись
    new_subject_title = 'NewDrawing'
    db.update(subject_id, new_subject_title)
    # проверяем, что значение subject_title изменилось
    result = db.select(subject_id)
    assert result[0]['subject_title'] == new_subject_title
    # удаляем созданную запись (подчищаем за собой таблицу)
    db.delete(subject_id)


# Удаление записи из таблицы subject по ID
def test_delete():
    # создаём новую запись в таблице
    max_id = db.get_max_id()
    subject_id = max_id + 1
    subject_title = 'Drawing'
    db.insert(subject_id, subject_title)
    # удаляем созданную запись (подчищаем за собой таблицу)
    db.delete(subject_id)
    # проверяем, что созданная запись удалена из таблицы
    result = db.select(subject_id)
    assert len(result) == 0
