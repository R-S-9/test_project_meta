from typing import Optional

from ..models import UserProfile


class LoginDao:
    @staticmethod
    def get_user_by_email(email) -> Optional[UserProfile]:
        return UserProfile.objects.get_or_none(email=email)
