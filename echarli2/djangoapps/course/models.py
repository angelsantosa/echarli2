from django.db import models

from django.utils.translation import ugettext_noop
from django_countries.fields import CountryField
from django.utils import timezone
from datetime import datetime
from pytz import UTC

from haystack.utils.geo import Point

from users.models import User
from category.models import SubCategory

# Create your models here or die ;)
class Course(models.Model):
    """Collected info for Publish Course
    """

    class Meta(object):
        app_label = "course"
        db_table = "course"
        verbose_name_plural = "courses"

    # Los estados en los que se puede encontrar la publicación del curso
    PUBLISHED = 0
    DRAFT = 1
    REMOVED = 2

    SPANISH = 'es'
    ENGLISH = 'en'
    GERMAN = 'de'

    LANGUAGE_TYPE_CHOICES = (
        (ENGLISH, ugettext_noop('English')),
        (SPANISH, ugettext_noop('Spanish')),
        (GERMAN, ugettext_noop('German')),
    )

    PUBLISH_COURSE_STATUS_CHOICES = (
        (PUBLISHED, ugettext_noop('Published')),
        (DRAFT, ugettext_noop('Draft')),
        (REMOVED, ugettext_noop('Removed')),
    )

    # Las opciones que describen el tipo de curso
    INDIVIDUAL_FACE = 0
    COLLECTIVE_FACE = 1
    VIA_REMOTE = 2
    ONLINE_VIDEO = 3

    COURSE_TYPE_CHOICES = (
        (INDIVIDUAL_FACE, ugettext_noop('Individual Face')),
        (COLLECTIVE_FACE, ugettext_noop('Collective Face')),
        (VIA_REMOTE, ugettext_noop('Via Remote')),
        (ONLINE_VIDEO, ugettext_noop('Online Video')),
    )
    COURSE_TYPE_LIVE_CHOICES = (
        (INDIVIDUAL_FACE, ugettext_noop('Individual Face')),
        (COLLECTIVE_FACE, ugettext_noop('Collective Face')),
    )

    # El nivel de aprendiz para el que esta dirigido el curso
    NEWBIE = 0
    NOVICE = 1
    ROOKIE = 2
    BEGGINER = 3
    TALENTED = 4
    SKILLED = 5
    INTERMEDIATE = 6
    SKILLFUL = 7
    PROFICIENT = 8
    EXPERIENCED = 9
    ADVANCED = 10
    SENIOR = 11
    EXPERT = 12

    COURSE_LEVEL_CHOICES = (
        (NOVICE, ugettext_noop('Novice')),
        (BEGGINER, ugettext_noop('Begginer')),
        (INTERMEDIATE, ugettext_noop('Intermediate')),
        (ADVANCED, ugettext_noop('Advanced')),
        (EXPERT, ugettext_noop('Expert')),
    )

    # Las opciones que describen el modo elegido de ubicación
    PROVIDED_BY_APPRENTICE = 0
    PROVIDED_BY_MENTOR = 1

    LOCATION_MODE_CHOICES = (
        (PROVIDED_BY_APPRENTICE, ugettext_noop('Provided by the apprentice')),
        (PROVIDED_BY_MENTOR, ugettext_noop('Provided by the mentor')),
    )

    # Las opciones que describen el tipo de ubicación elegido por el mentor
    PUBLIC_PLACE = 0
    OFFICE = 1
    HOUSE = 2
    COFFEE = 3

    LOCATION_TYPE_CHOICES = (
        (PUBLIC_PLACE, ugettext_noop('Public Place')),
        (HOUSE, ugettext_noop('House')),
        (OFFICE, ugettext_noop('Office')),
        (COFFEE, ugettext_noop('Coffee')),
    )

    # Las opciones de pago para la publación del curso
    PAYMENT_SESSION = 0
    PAYMENT_PROGRAM = 1
    PAYMENT_FREE = 2

    PAYMENT_TYPE_CHOICES = (
        (PAYMENT_SESSION, ugettext_noop('Payment session')),
        (PAYMENT_PROGRAM, ugettext_noop('Payment program')),
        (PAYMENT_FREE, ugettext_noop('Free')),
    )

    # Las opciones para descuentos para la publación del curso
    SPECIAL_OFFERS = 0
    DIRECT_DISCOUNT = 1
    DISCOUNT_BUYING_BULK = 2
    NONE = 3

    DISCOUNT_TYPE_CHOICES = (
        (SPECIAL_OFFERS, ugettext_noop('Special offers')),
        (DIRECT_DISCOUNT, ugettext_noop('Direct discount')),
        (DISCOUNT_BUYING_BULK, ugettext_noop('Discount for buying in bulk')),
        (NONE, ugettext_noop('None')),
    )

    # Las opciones que describen la moneda del precio del curso
    # lower case ISO currency codes
    USD = 'usd'
    MXN = 'mxn'

    PRICE_CURRENCY_CHOICES = (
        (USD, ugettext_noop('USD')),
        (MXN, ugettext_noop('MXN')),
    )

    # TODO: crear campo asociado al CourseKey
    # the course that this mode is attached to

    mentor = models.ForeignKey(
        User, db_index=True, related_name='mentor',
        help_text='Establecer el Mentor creador del curso'
    )

    course_name = models.CharField(
        max_length=250, blank=True, null=True, default='',
        help_text='Nombre de la publicación del curso'
    )

    course_description = models.TextField(
        blank=True, null=True,
        help_text='Descripción de la publicación del curso')

    publish_course_status = models.IntegerField(
        db_index=True, default=DRAFT,
        choices=PUBLISH_COURSE_STATUS_CHOICES,
        help_text='Establece el tipo de nivel para publicación del curso'
    )

    course_type = models.IntegerField(
        db_index=True, default=INDIVIDUAL_FACE,
        choices=COURSE_TYPE_CHOICES,
        help_text='Establece el tipo de curso para publicación del curso'
    )

    course_level = models.IntegerField(
        db_index=True, default=NOVICE,
        choices=COURSE_LEVEL_CHOICES,
        help_text='Establece el tipo de nivel para publicación del curso'
    )
    course_language = models.CharField(
        db_index=True, default=SPANISH,
        choices=LANGUAGE_TYPE_CHOICES,
        max_length=2,
        help_text='Establece el lenguaje en el que se presentara el curso'
    )

    location_mode = models.IntegerField(
        db_index=True, default=PROVIDED_BY_MENTOR,
        choices=LOCATION_MODE_CHOICES,
        help_text='Establece el modo de ubicación para publicación del curso'
    )

    location_type = models.IntegerField(
        db_index=True, default=PUBLIC_PLACE,
        choices=LOCATION_TYPE_CHOICES,
        help_text='Establece el tipo de ubicación para publicación del curso'
    )

    minimum_apprentices = models.IntegerField(
        blank=True, null=True,
        help_text='Número mínimo de aprendices'
    )
    maximum_apprentices = models.IntegerField(
        blank=True, null=True,
        help_text='Número máximo de aprendices'
    )

    date_start = models.DateTimeField(
        null=True, default=None,
        help_text='Fecha de inicio del curso'
    )
    date_end = models.DateTimeField(
        null=True, default=None,
        help_text='Fecha de fin del urso'
    )

    category = models.ForeignKey(
        SubCategory, blank=True, null=True, db_index=True,
        related_name='publish_course_subcategory',
        help_text='Establecer la SubCategoria del curso')

    location_country = CountryField(
        blank=True, null=True,
        help_text='Establecer el país de la ubicación de la publicación del curso'
    )
    location_address = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Campo para datos de ubicación calle'
    )
    location_postal_code = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Código postal de la ubicación'
    )
    location_outdoor_number = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Número exterior de la ubicación'
    )
    location_internal_number = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Número interior de la ubicación'
    )
    location_state = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Estado / Provinca de la ubicación'
    )
    location_city = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Ciudad de la ubicación'
    )

    location_latitude = models.FloatField(
        null=True,
        help_text='Almacena la latitud de la ubicación'
    )
    location_longitude = models.FloatField(
        null=True,
        help_text='Almacena la longitud de la ubicación'
    )

    payment_type = models.IntegerField(
        db_index=True, default=PAYMENT_PROGRAM,
        choices=PAYMENT_TYPE_CHOICES,
        help_text='Establece el tipo de pago para publicación del curso'
    )

    price_program = models.IntegerField(
        blank=True, null=True,
        help_text='Precio del programa de la publicación del curso'
    )
    price_session = models.IntegerField(
        blank=True, null=True,
        help_text='Precio de la sesión de la publicación del curso'
    )
    price_currency = models.CharField(
        max_length=8, db_index=True, default='',
        choices=PRICE_CURRENCY_CHOICES,
        help_text='Establece la moneda del precio para publicación del curso'
    )

    discount_type = models.IntegerField(
        db_index=True, default=NONE,
        choices=DISCOUNT_TYPE_CHOICES,
        help_text='Establece el tipo para descuentos para publicación del curso'
    )

    created = models.DateTimeField(default=timezone.now,
                                      help_text='Fecha de creación del registro')
    updated = models.DateTimeField(default=timezone.now,
                                       help_text='Fecha de actualización del registro')

    def __str__(self):
        return self.course_name

    @property
    def coordinates(self):
        return Point(self.location_longitude, self.location_latitude)

    # Agregar fotos se realiza con API

    # Agregar programa del curso con API

    # Agregar materiales del curso con API

class CourseSchedule(models.Model):
    """Collected info for Publish Course Schedule
    """

    class Meta(object):
        app_label = "course"
        db_table = "course_schedule"

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    DAYS_OF_WEEK = (
        (MONDAY, ugettext_noop('Monday')),
        (TUESDAY, ugettext_noop('Tuesday')),
        (WEDNESDAY, ugettext_noop('Wednesday')),
        (THURSDAY, ugettext_noop('Thursday')),
        (FRIDAY, ugettext_noop('Friday')),
        (SATURDAY, ugettext_noop('Saturday')),
        (SUNDAY, ugettext_noop('Sunday')),
    )

    course = models.ForeignKey(
        Course, db_index=True, related_name='publish_course_schedule',
        help_text='Establece la relación con el curso publicado'
    )

    day_of_week = models.IntegerField(
        db_index=True, default=MONDAY,
        choices=DAYS_OF_WEEK,
        help_text='Establece el horario de calendario para publicación del curso'
    )

    time_start = models.TimeField(
        verbose_name=ugettext_noop("Start")
    )

    time_end = models.TimeField(
        verbose_name=ugettext_noop("End")
    )

    uploaded_at = models.DateTimeField(
        null=True,
        help_text='Fecha en la que se crea el horario'
    )


class CourseResource(models.Model):
    """Collected info for Publish Course Resource
    """

    class Meta(object):
        app_label = "course"
        db_table = "course_resource"

    RESOURCE_PHOTO = 0
    RESOURCE_PROGRAM = 1
    RESOURCE_MATERIAL = 2

    COURSE_RESOURCE_TYPE = (
        (RESOURCE_PHOTO, ugettext_noop('Photo')),
        (RESOURCE_PROGRAM, ugettext_noop('Program Course')),
        (RESOURCE_MATERIAL, ugettext_noop('Material')),
    )

    course = models.ForeignKey(
        Course, db_index=True, related_name='publish_course_resource',
        help_text='Establecer el curso al que esta asociado el recurso'
    )

    name = models.CharField(
        max_length=250, default='empty',
        help_text='Es el nombre con el que esta asociado el recurso en el repositorio'
    )

    type = models.IntegerField(
        db_index=True, default=RESOURCE_MATERIAL,
        choices=COURSE_RESOURCE_TYPE,
        help_text='Determinar el tipo de recurso de cargado'
    )

    extension = models.CharField(
        blank=True, max_length=4,
        help_text='Extensión del recurso cargado'
    )

    uploaded_at = models.DateTimeField(
        null=True,
        help_text='Fecha en de carga del recurso'
    )
