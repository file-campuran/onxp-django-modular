from django.db import connection

#Create
def book_create(title:str, author:str, description:str)->str:
  with connection.cursor() as cursor:
       cursor.execute("""
            INSERT into book
                (title, author, description)
            values (%s, %s, %s)
            RETURNING *
            """, [title, author, description]);
  return "success"


#Read
def book_read_all():
    with connection.cursor() as cursor:
       cursor.execute("""
            SELECT id,title,author,description from book
            """);
    return cursor.fetchall()


#Update
def book_update():
  with connection.cursor() as cursor:
       cursor.execute("""
            UPDATE book
            SET title = %s,author = %s
            WHERE id = %s
            RETURNING *
            """, ['Judul Baru','TestingUpdate', 1]);


#read by id
def book_read_by_id(id):
    with connection.cursor() as cursor:
       cursor.execute("""
            SELECT id,title,author from book
            WHERE id = %s
            """, [id]);
    return cursor.fectghone()


#delete
def book_delete():
  with connection.cursor() as cursor:
       cursor.execute("""
            DELETE from book
            WHERE id = %s
            RETURNING *
            """, [1]);