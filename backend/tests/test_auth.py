import unittest
from app import create_app, db
from app.models.user import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        response = self.client.post('/api/auth/register', json={
            'email': 'test@example.com',
            'password': 'password123',
            'name': 'Test User'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('Usuário registrado com sucesso', data['message'])
        self.assertIn('token', data)

    def test_login_user(self):
        user = User(email='test@example.com', name='Test User')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/api/auth/login', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('Login realizado com sucesso', data['message'])
        self.assertIn('token', data)

if __name__ == "__main__":
    unittest.main()
