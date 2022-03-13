from ..models import UserProfile


class ActivateUserUtils:
    @staticmethod
    def activate_user(user: UserProfile) -> None:
        user.is_active = True
        user.save()

        return None
