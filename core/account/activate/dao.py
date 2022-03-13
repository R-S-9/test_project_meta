from typing import Optional

from ..models import UserProfile


class ActivateUserDao:
    @staticmethod
    def get_user_by_id(user_id: str) -> Optional[UserProfile]:
        return UserProfile.objects.get_or_none(id=user_id)
