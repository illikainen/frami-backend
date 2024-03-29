from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


def get_deleted_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Appointment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    note = models.TextField(blank=True)
    patient = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.CASCADE,
    )
    staff = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.SET(get_deleted_user),
    )
    creator = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.SET(get_deleted_user),
    )


class AppointmentRequest(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    staff = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.SET(get_deleted_user),
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.CASCADE,
    )


class Prescription(models.Model):
    medication = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    refill = models.PositiveIntegerField(default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    note = models.TextField(blank=True)
    patient = models.ForeignKey(
        User,
        related_name='prescriptions',
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        User,
        related_name='prescribed',
        on_delete=models.SET(get_deleted_user),
    )


class PrescriptionRequest(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    prescription = models.OneToOneField(
        Prescription,
        related_name='refill_request',
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.CASCADE,
    )


class Question(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User,
        related_name='questions',
        on_delete=models.CASCADE,
    )


class Answer(models.Model):
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    unread = models.BooleanField(default=True)
    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        User,
        related_name='answers',
        on_delete=models.SET(get_deleted_user),
    )


class Result(models.Model):
    kind = models.CharField(max_length=255)
    result = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    unread = models.BooleanField(default=True)
    patient = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.SET(get_deleted_user),
    )


class Notification(models.Model):
    CHANGED = 'changed'
    CREATED = 'created'
    DELETED = 'deleted'

    uuid = models.UUIDField(editable=False)
    read = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    event = models.CharField(
        max_length=255,
        choices=[(x, x) for x in [CHANGED, CREATED, DELETED]],
    )
    target_name = models.CharField(max_length=255)
    target_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_type', 'target_id')


class UserNotification(Notification):
    user = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.CASCADE,
    )


class GroupNotification(Notification):
    group = models.ForeignKey(
        Group,
        related_name='+',
        on_delete=models.CASCADE,
    )
