import asyncio
import unittest
from api.user_REST_controller import get_user_email
import pytest
from fastapi import HTTPException, status
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

    
    def test_get_user_email(self):
        test_email = "john@example.com"
        expected_response = {
                "username": "john_doe",
                "email": "john@example.com",
                "full_name": "John Doe",
                "playlist": [
                    {
                        "name": "My Favorites",
                        "likes": 100,
                        "news_list": None
                    }
                ]
            }
        

        response = asyncio.run(get_user_email(test_email))
        response = response.dict()

        assert response == expected_response

    def test_get_user_email_raises_exception(client):
        test_email = "nonexistent@example.com" 
        with pytest.raises(HTTPException) as exc_info:
            response = asyncio.run(get_user_email(test_email))
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
        assert exc_info.value.detail == "User does not exist"

if __name__ == '__main__':
    unittest.main()
