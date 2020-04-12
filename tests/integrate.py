import requests
import psycopg2
connection = psycopg2.connect(user="cs162_user",
                                  password="cs162_password",
                                  host="localhost",
                                  port="5432",
                                  database="cs162")
cursor = connection.cursor()

def test_add_response():
    response = requests.post('http://127.0.0.1:5000/add',data={'expression':'2+2'})
    assert response.status_code == 200

def test_add_db():
    cursor.execute("SELECT * FROM Expression WHERE text='2+2' LIMIT 1")
    es = cursor.fetchall()
    assert es is not None
    assert es[0] is not None
    assert es[0][2] == 4

def test_add_error():
    response = requests.post('http://127.0.0.1:5000/add', data={'expression':'2/0'})
    assert response.status_code == 500

def test_last_exp():
    cursor.execute("SELECT * FROM Expression ORDER BY id DESC LIMIT 1")
    es = cursor.fetchall()
    assert es is not None
    assert es[0] is not None
    assert es[0][1] == '2+2'

if __name__=="__main__":
    print("Testing")
    test_add_response()
    test_add_db()
    test_add_error()
    test_last_exp()
    print("All passed")
