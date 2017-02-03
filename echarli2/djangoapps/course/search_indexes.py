from django.utils import timezone

from haystack import indexes
from .models import Course

class CourseIndex(indexes.ModelSearchIndex, indexes.Indexable):
    autocomplete = indexes.EdgeNgramField()
    coordinates = indexes.LocationField(model_attr="coordinates")
    category_id = indexes.IntegerField()
    date_start = indexes.DateTimeField(model_attr="date_start")
    date_end = indexes.DateTimeField(model_attr="date_end")

    class Meta:
        model = Course

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.course_name,
            obj.location_country.code,
            obj.location_address,
            obj.location_city,
            obj.location_postal_code,
            obj.location_state,
        ))

    def prepare_category_id(self, obj):
        return obj.category.id

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            created__lte=timezone.now()
        )
