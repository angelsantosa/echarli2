# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.translation import ugettext_noop
from datetime import datetime
from pytz import UTC


@python_2_unicode_compatible
class User(AbstractUser):

    # Las opciones que describen el estado del archivo
    APPROVED = 'AP'
    FILE_MISSING = 'FM'
    APPROVINGLY = 'AY'
    RELOAD = 'RE'
    SUGGESTED = 'SU'
    LOADDED = 'LO'
    DOCUMENT_STATUS_CHOICES = (
        (APPROVED, ugettext_noop('Approved')),
        (FILE_MISSING, ugettext_noop('File Missing')),
        (APPROVINGLY, ugettext_noop('Approvingly')),
        (RELOAD, ugettext_noop('Reload')),
        (SUGGESTED, ugettext_noop('Suggested')),
        (LOADDED, ugettext_noop('Loadded'))
    )

    # Las opciones que describen el estado del perfil
    APPRENTICE = 'A'
    CANDIDATE = 'C'
    MENTOR = 'M'
    PROFILE_STATUS_CHOICES = (
        (APPRENTICE, ugettext_noop('Apprentice')),
        (CANDIDATE, ugettext_noop('Mentor Candidate')),
        (MENTOR, ugettext_noop('Mentor'))
    )

    #user = models.OneToOneField(User, unique=True, db_index=True, related_name='mentor', help_text='Relacionar los datos de mentor con el usuario')

    user_profile_status = models.CharField(
        blank=True, null=True, max_length=1, db_index=True, default=APPRENTICE,
        choices=PROFILE_STATUS_CHOICES,
        help_text='Estado del perfíl de usuario'
    )

    # Fields from student's model
    # RFC
    rfc = models.CharField(
        blank=True, null=True, max_length=13,
        help_text='Registro Federal de Contribuyentes'
    )

    # Telefono principal
    phone = models.CharField(max_length=75, blank=True,
                         help_text='Teléfono de contacto del usuario')

    # Telefono celular
    mobile = models.CharField(max_length=75, blank=True,
                         help_text='Celular de contacto del usuario')

    # Fecha de nacimiento
    birthday = models.DateTimeField(default=timezone.now, blank=True, null=True,
                                         help_text='Fecha de nacimiento del usuario')
    GENDER_CHOICES = (
        ('m', ugettext_noop('Male')),
        ('f', ugettext_noop('Female')),
        # Translators: 'Other' refers to the student's gender
        # ('o', ugettext_noop('Other/Prefer Not to Say'))
    )
    gender = models.CharField(
        blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
    )

    about_me = models.CharField(
        blank=True, null=True, max_length=512,
        help_text='Acerca del usuario, descripción de la persona'
    )

    country = models.CharField(max_length=250, blank=True,
                                    help_text='Nombre del país residencia del mentor')
    state = models.CharField(max_length=250, blank=True,
                                  help_text='Estado de residencia del mentor')
    address = models.CharField(max_length=250, blank=True,
                                         help_text='Campo para datos de dirección')
    postal_code = models.CharField(max_length=250, blank=True,
                                   help_text='Código postal de residencia del mentor')
    outdoor_number = models.CharField(max_length=250, blank=True,
                                      help_text='Número exterior de residencia del mentor')
    internal_number = models.CharField(max_length=250, blank=True,
                                       help_text='Número interior de residencia del mentor')

    location_latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True,
                                            help_text='Almacena la latitud en la ubicación del mentor')
    location_longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True,
                                             help_text='Almacena la longitud en la ubicación del mentor')

    lang_key = models.CharField(max_length=2, blank=True, default='en',
                                help_text='Idioma del usuario')

    created_at = models.DateTimeField(default=timezone.now,
                                      help_text='Fecha de creación del registro')
    modified_at = models.DateTimeField(default=timezone.now,
                                       help_text='Fecha de actualización del registro')

    @property
    def has_receipt_id(self):
        """
        Convenience method that returns a boolean indicating whether or not
        this mentor has uploaded a receipt id document.
        """
        return self.receipt_id_uploaded_at is not None

    @property
    def get_receipt_id_status(self):
        """
        Convenience method that returns a string indicating
        the status of receipt id document.
        """
        return self.get_document_status_choice(self.receipt_id_status)

    @property
    def has_receipt_address(self):
        """
        Convenience method that returns a boolean indicating whether or not
        this mentor has uploaded a receipt address document.
        """
        return self.receipt_address_uploaded_at is not None

    @property
    def get_receipt_address_status(self):
        """
        Convenience method that returns a string indicating
        the status of receipt address document.
        """
        return self.get_document_status_choice(self.receipt_address_status)

    @property
    def has_receipt_penal(self):
        """
        Convenience method that returns a boolean indicating whether or not
        this mentor has uploaded a receipt penal document.
        """
        return self.receipt_penal_uploaded_at is not None

    @property
    def get_receipt_penal_status(self):
        """
        Convenience method that returns a string indicating
        the status of receipt penal document.
        """
        return self.get_document_status_choice(self.receipt_penal_status)

    @property
    def has_receipt_knowledge(self):
        """
        Convenience method that returns a boolean indicating whether or not
        this mentor has uploaded a receipt knowledge document.
        """
        return self.receipt_knowledge_uploaded_at is not None

    @property
    def get_receipt_knowledge_status(self):
        """
        Convenience method that returns a string indicating
        the status of receipt knowledge document.
        """
        return self.get_document_status_choice(self.receipt_knowledge_status)

    @property
    def has_receipt_diploma(self):
        """
        Convenience method that returns a boolean indicating whether or not
        this mentor has uploaded a receipt passport document.
        """
        return self.receipt_diploma_uploaded_at is not None

    @property
    def get_receipt_diploma_status(self):
        """
        Convenience method that returns a string indicating
        the status of receipt passport document.
        """
        return self.get_document_status_choice(self.receipt_diploma_status)

    @property
    def is_aprentice(self):
        """
        Convenience method that returns a boolean indicating
        the user is Aprentice.
        """
        return self.user_profile_status == self.APPRENTICE

    @property
    def is_mentor(self):
        """
        Convenience method that returns a boolean indicating
        the user is Mentor.
        """
        return self.user_profile_status == self.MENTOR

    @property
    def has_validated_email(self):
        """
        Convenience method that returns a boolean indicating
        the validation of email
        """
        return self.receipt_diploma_uploaded_at is not None

    @property
    def has_validated_email(self):
        """
        Convenience method that returns a boolean indicating
        the validation of email
        """
        return self.user.email_user is not None

    @property
    def has_validated_phone(self):
        """
        Convenience method that returns a boolean indicating
        the validation of phone
        """
        return self.phone is not None

    @property
    def has_validated_documents(self):
        """
        Convenience method that returns a boolean indicating
        the validation of identity documents
        """
        # Se han recibido todos los documentos
        validated = self.has_receipt_id and self.has_receipt_address and self.has_receipt_penal
        if validated:
            # Los documentos estan aprobados
            validated &= self.get_receipt_id_status == self.APPROVED
            validated &= self.get_receipt_address_status == self.APPROVED
            validated &= self.get_receipt_penal_status == self.APPROVED
        return validated

    @property
    def has_validated_certificates(self):
        """
        Convenience method that returns a boolean indicating
        the validation of knowledge documents
        """
        # Se ha recibido alguno de los documentos de conocimientos
        validated = self.has_receipt_knowledge or self.has_receipt_diploma
        return validated

    def get_document_status_choice(self, choice):
        return dict(self.DOCUMENT_STATUS_CHOICES).get(choice)

    def get_user_status_profile(self, choice):
        return dict(self.PROFILE_STATUS_CHOICES).get(choice)

    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
