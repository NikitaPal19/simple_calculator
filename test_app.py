from app import app

def test_add():
    with app.test_client() as client:
        response = client.get('/add?a=5&b=3')
        assert response.json['result'] == 8

def test_divide_by_zero():
    with app.test_client() as client:
        response = client.get('/divide?a=5&b=0')
        assert response.status_code == 400
        assert 'error' in response.json
