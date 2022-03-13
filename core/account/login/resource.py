from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from pydantic import ValidationError

from .dao import LoginDao
from .validator import LoginValidator
from ..hash_password.utils import HashPassword


class Login(View):
    @staticmethod
    def post(request):
        try:
            validation_json = LoginValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        user = LoginDao.get_user_by_email(validation_json.email)

        if not all([
            user, HashPassword.check_password(
                validation_json.password, user.password
            )
        ]):
            return 'Пароль не подходит'

        return render(request=request, template_name='index.html', context={})
