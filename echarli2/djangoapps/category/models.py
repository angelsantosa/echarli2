from django.db import models
from django.utils import timezone
# Create your models here or die ;).

class Category(models.Model):
    """DocString
    """

    class Meta(object):
        app_label = "category"
        db_table = "course_category"
        verbose_name_plural = "categories"

    category = models.CharField(max_length=255, unique=True,
                                help_text='Nombre de la categoria')

    icon = models.CharField(max_length=255,
                            help_text='Nombre del icono que identifica la categoría')

    created_at = models.DateTimeField(default=timezone.now,
                                      help_text='Fecha de creación del registro')

    modified_at = models.DateTimeField(default=timezone.now,
                                       help_text='Fecha de actualización del registro')

    @property
    def get_subcategory_count(self):
        """
        Convenience method that returns a string indicating
        the status of receipt id document.
        """
        return 100

    def __unicode__(self):
        return "%s" % self.category

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    """DocString
    """

    class Meta(object):
        app_label = "category"
        db_table = "course_subcategory"
        verbose_name_plural = "subcategories"
        unique_together = ('subcategory', 'category')

    subcategory = models.CharField(max_length=255,
                                   help_text='Nombre de la subcategoria')

    category = models.ForeignKey(Category, db_index=True, related_name='subcategory',
                                 help_text='Relacionar la subcategoria con la categoria principal')

    created_at = models.DateTimeField(default=timezone.now,
                                      help_text='Fecha de creación del registro')

    modified_at = models.DateTimeField(default=timezone.now,
                                       help_text='Fecha de actualización del registro')

    def __unicode__(self):
        return "%s" % self.subcategory


    def __str__(self):
        return self.subcategory
