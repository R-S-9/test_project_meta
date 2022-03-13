from typing import Optional
import json

from ..hash_password.utils import HashPassword
from ..models import UserManager, UserProfile


class RegistrationDao:
    @staticmethod
    def create_user(user_json: json) -> Optional[UserManager]:
        return UserProfile.objects.get_or_create(
            full_name=user_json.full_name,
            email=user_json.email,
            password=HashPassword.get_hashed_password(
                user_json.password
            )
        )[0]


class UserDao:
    @staticmethod
    def get_user_id_by_email(email) -> Optional[UserProfile]:
        return UserProfile.objects.get_or_none(email=email)
