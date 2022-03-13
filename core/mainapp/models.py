from django.db import models


# Функция get_or_none для Django
class MyQuerySet(models.QuerySet):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class TopicTesting(models.Model):
    topic_name = models.CharField(
        verbose_name="Названия темы",
        max_length=50,
        blank=False,
    )

    objects = MyQuerySet.as_manager()

    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name = "Тема тестирования"
        verbose_name_plural = "Темы тестирования"


class Question(models.Model):
    title = models.CharField(
        verbose_name="Вопрос",
        max_length=1000,
        blank=False,
    )

    test_solved = models.BooleanField(
        default=False,
        verbose_name="тест решен (для пользователя)"
    )

    question_topic = models.ForeignKey(
        TopicTesting,
        verbose_name='Вопрос по теме',
        on_delete=models.CASCADE
    )

    objects = MyQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос темы"
        verbose_name_plural = "Вопросы по темам"


class Choice(models.Model):
    wrong_choice = models.CharField(
        verbose_name="Неверный ответ",
        max_length=1000,
        blank=False,
    )
    right_choice = models.CharField(
        verbose_name="Верный ответ",
        max_length=1000,
        blank=False,
    )

    question = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE
    )

    objects = MyQuerySet.as_manager()

    class Meta:
        verbose_name = "Вариант ответов"
        verbose_name_plural = "Варианты ответов"


class Answer(models.Model):
    # user = models.ForeignKey
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    objects = MyQuerySet.as_manager()

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
