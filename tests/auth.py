import unittest

from auth import authenticate_user

class TestAuthenticateUser(unittest.TestCase):

    def setUp(self):
        self.user_data = [
            {'username': 'user1', 'password': 'pass1'},
            {'username': 'user2', 'password': 'pass2'},
            {'username': 'user3', 'password': 'pass3'}
        ]

    def test_authenticate_valid_user(self):
        self.assertTrue(authenticate_user('user1', 'pass1', self.user_data))
        self.assertTrue(authenticate_user('user2', 'pass2', self.user_data))
        self.assertTrue(authenticate_user('user3', 'pass3', self.user_data))

    def test_authenticate_invalid_user(self):
        self.assertFalse(authenticate_user('user4', 'pass4', self.user_data))
        self.assertFalse(authenticate_user('user1', 'wrongpass', self.user_data))
        self.assertFalse(authenticate_user('wronguser', 'pass1', self.user_data))

    def test_authenticate_empty_username(self):
        self.assertFalse(authenticate_user('', 'pass1', self.user_data))

    def test_authenticate_empty_password(self):
        self.assertFalse(authenticate_user('user1', '', self.user_data))

    def test_authenticate_empty_username_and_password(self):
        self.assertFalse(authenticate_user('', '', self.user_data))

    def test_authenticate_empty_user_data(self):
        self.assertFalse(authenticate_user('user1', 'pass1', []))

if __name__ == '__main__':
    unittest.main()