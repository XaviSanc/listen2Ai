import unittest

from utils.mockups import fill_users_array


class Testing(unittest.TestCase):
# Test user creation
    def test_first_user_creation(self):
        users = fill_users_array()
        print(users[0])
        assert users[0].username == "john_doe"
        assert users[0].email == "john@example.com"
        assert users[0].full_name == "John Doe"
        assert len(users[0].playlist) == 1
        assert users[0].playlist[0].name == "My Favorites"
        assert users[0].playlist[0].likes == 100
        assert len(users[0].playlist[0].news_list) == 2
        assert users[0].playlist[0].news_list[0].name == "Breaking News"
        assert users[0].playlist[0].news_list[1].name == "In-depth Analysis"
    
    def test_len_users_(self):
        users = fill_users_array()
        assert len(users) == 5

  
if __name__ == '__main__':
    unittest.main()