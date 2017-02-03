import os
import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_noop
from users.models import User

# Create your models here.
def receipt_upload(instance, filename):
    """
    Delete the file if it already exist and returns the certificate template asset file path.

    :param instance: CertificateTemplateAsset object
    :param filename: file to upload
    :return path: path of asset file e.g. receipt_template_assets/1/filename
    """
    name = os.path.join('receipt_template_assets', str(instance.id), filename)
    fullname = os.path.join(settings.MEDIA_ROOT, name)
    if os.path.exists(fullname):
        os.remove(fullname)
    return name

class Mentor(models.Model):
    """DocString
    """

    class Meta(object):
        app_label = "mentor"
        db_table = "auth_userprofilementor"

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

    user = models.OneToOneField(User, unique=True, db_index=True, related_name='user',
                                help_text='Relacionar los datos de mentor con el usuario')

    user_profile_status = models.CharField(
        blank=True, null=True, max_length=1, db_index=True, default=APPRENTICE,
        choices=PROFILE_STATUS_CHOICES,
        help_text='Estado del perfíl de usuario'
    )

    phone = models.CharField(max_length=75, blank=True,
                             help_text='Teléfono de contacto del mentor')

    # Check upload
    receipt_id_extension = models.CharField(max_length=4, blank=True,
                                            help_text='Extensión del documento de identificación del mentor')
    receipt_id_uploaded_at = models.DateTimeField(null=True,
                                                  help_text='Fecha en de carga del documento de identificación')
    receipt_id_status = models.CharField(
        blank=True, null=True, max_length=2, db_index=True, default=FILE_MISSING,
        choices=DOCUMENT_STATUS_CHOICES,
        help_text='Estado del documento de identificación'
    )
    receipt_address_extension = models.CharField(max_length=4, blank=True,
                                                 help_text='Extensión del documento del domicilio del mentor')
    receipt_address_uploaded_at = models.DateTimeField(null=True,
                                                       help_text='Fecha de carga del documento de domicilio')
    receipt_address_status = models.CharField(
        blank=True, null=True, max_length=2, db_index=True, default=FILE_MISSING,
        choices=DOCUMENT_STATUS_CHOICES,
        help_text='Estado del documento de domicilio'
    )
    receipt_penal_extension = models.CharField(max_length=4, blank=True,
                                               help_text='Extensión del documento de no antecedentes penales')
    receipt_penal_uploaded_at = models.DateTimeField(null=True,
                                                     help_text='Fecha de carga documento de no antecedentes penales')
    receipt_penal_status = models.CharField(
        blank=True, null=True, max_length=2, db_index=True, default=FILE_MISSING,
        choices=DOCUMENT_STATUS_CHOICES,
        help_text='Estado del documento de no antecedentes penales'
    )
    receipt_knowledge_extension = models.CharField(max_length=4, blank=True,
                                                   help_text='Extensión del documento de conocimientos')
    receipt_knowledge_uploaded_at = models.DateTimeField(null=True,
                                                         help_text='Fecha de carga del documento de conocimientos')
    receipt_knowledge_status = models.CharField(
        blank=True, null=True, max_length=2, db_index=True, default=SUGGESTED,
        choices=DOCUMENT_STATUS_CHOICES,
        help_text='Estado del documento de conocimientos'
    )
    receipt_diploma_extension = models.CharField(max_length=4, blank=True,
                                                 help_text='Extensión del documento de diploma')
    receipt_diploma_uploaded_at = models.DateTimeField(null=True,
                                                       help_text='Fecha de carga del documento de diploma')
    receipt_diploma_status = models.CharField(
        blank=True, null=True, max_length=2, db_index=True, default=FILE_MISSING,
        choices=DOCUMENT_STATUS_CHOICES,
        help_text='Estado del documento de dimploma'
    )

    occupation = models.CharField(max_length=100, blank=True,
                                  help_text='Ocupación del mentor, profesión u oficio')
    educational_name = models.CharField(max_length=100, blank=True,
                                        help_text='Nombre de la institución educativa del mentor')
    work_name = models.CharField(max_length=250, blank=True,
                                 help_text='Nombre del llugar de trabajo')

    emergency_contact_name = models.CharField(max_length=250, blank=True,
                                              help_text='Nombre de contacto en caso de emergencia')
    emergency_contact_email = models.CharField(max_length=250, blank=True,
                                               help_text='Correo del contacto en caso de emergencia')
    emergency_contact_relationship = models.CharField(max_length=250, blank=True,
                                                      help_text='Relación con el contacto en caso de emergencia')
    emergency_contact_phone = models.CharField(max_length=250, blank=True,
                                               help_text='Teléfono del contacto en caso de emergencia')

    country_name = models.CharField(max_length=250, blank=True,
                                    help_text='Nombre del país residencia del mentor')
    state_name = models.CharField(max_length=250, blank=True,
                                  help_text='Estado de residencia del mentor')
    address_field_one = models.CharField(max_length=250, blank=True,
                                         help_text='Campo para datos de dirección')
    address_field_two = models.CharField(max_length=250, blank=True,
                                         help_text='Campo para datos de dirección extendido')
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
        return super(Mentor, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
