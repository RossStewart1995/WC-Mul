import unittest
import mul
from flask import Flask,json
from app import app

class TestMultiply(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul.multiply(3,3), 9)

    def test_HTTP_200(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'x': '6', 'y': '7'})
            assert response.status_code == 200

    def test_HTTP_400(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'x': 'h', 'y': '7'})
            assert response.status_code == 400
    
    def test_HTTP_200_And_Data(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'x': '3', 'y': '2'})
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['error'] == False
            assert data['string'] == "3*2=6"
            assert data['author'] == "Ross Stewart"
            assert data['answer'] == 6

    def test_HTTP_400_And_Error_Data(self):
        with app.test_client() as c:
            response = c.get('/', query_string={'x': '2', 'y': 'h'})
            assert response.status_code == 400
            data = json.loads(response.get_data(as_text=True))
            assert data['error'] == True
            assert data['string'] == "You must provide valid input for x/y"


if __name__ == 'main':
    unittest.main()