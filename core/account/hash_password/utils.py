from typing import Optional

import bcrypt


class HashPassword:
    @staticmethod
    def get_hashed_password(plain_text_password: str) -> str:
        return bcrypt.hashpw(
            plain_text_password.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

    @staticmethod
    def check_password(plain_text_password: str, hashed_password: bytes) \
            -> bool:
        return bcrypt.checkpw(
            plain_text_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
