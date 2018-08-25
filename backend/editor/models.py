from django.db import models
from adminsortable.models import SortableMixin


class Quiz(models.Model):
    name = models.CharField(max_length=127, null=False)

    def __str__(self):
        return self.name or super().__str__()


class Question(SortableMixin, models.Model):
    class Meta:
        ordering = ['order']

    quiz = models.ForeignKey(Quiz, null=False, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    order = models.PositiveSmallIntegerField(db_index=True, editable=False)

    def __str__(self):
        return (self.text or '')[:15]


class Answer(SortableMixin, models.Model):
    class Meta:
        ordering = ['order']

    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=63, null=False)
    order = models.PositiveSmallIntegerField(db_index=True, editable=False)

    def __str__(self):
        return self.text or super().__str__()
