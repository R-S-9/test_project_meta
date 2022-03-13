import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from pydantic import ValidationError

from .dao import ActivateUserDao
from .utils import ActivateUserUtils
from .validator import ActivateValidator
from ..redis_key.utils import CreateRedisKey


class ActivateUser(View):
    """Класс активации пользователя через почту"""
    @staticmethod
    def get(request, uuid):
        red = CreateRedisKey()

        try:
            validation_json = ActivateValidator.parse_raw(
                json.dumps({"redis_uuid": red.get(uuid).decode('UTF-8')})
            )
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        user = ActivateUserDao.get_user_by_id(validation_json.redis_uuid)

        if not user:
            return

        ActivateUserUtils.activate_user(user)

        return render(request=request, template_name='index.html', context={})
