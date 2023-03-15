from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.functions import datetime


from .validators import validate_start_date


class Group(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='name',
        db_column='name',
        validators=[MinLengthValidator(2, '"name" field value less than two symbols')]
    )
    description = models.TextField(
        max_length=500,
        verbose_name='description',
        db_column='description',
        validators=[MinLengthValidator(2, '"description" field value less than two symbols')]
    )
    start = models.DateField(default=datetime.datetime.utcnow, validators=[validate_start_date])
    end = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    create_datetime = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Group name: {self.name}'

    class Meta:
        db_table = 'groups'
