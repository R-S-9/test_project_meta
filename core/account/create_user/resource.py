from django.shortcuts import render
from pydantic import ValidationError

from django.http import JsonResponse
from django.views import View

from .dao import RegistrationDao, UserDao
from .validator import RegistrationValidator

from ..mailer.utils import Mailer


class Registration(View):
    """Класс регистрации"""
    @staticmethod
    def post(request):
        try:
            validation_json = RegistrationValidator.parse_raw(request.body)
        except ValidationError as _ex:
            return JsonResponse(
                data={"error": f"validation error params: {_ex}"}, status=204
            )

        try:
            data = RegistrationDao.create_user(validation_json)
        except Exception:
            data = UserDao.get_user_id_by_email(validation_json.email)

        Mailer.send_mail(validation_json.email, data.id)

        return render(
            request=request,
            template_name='index.html',
            context={"data": "Отправлено"}
        )
