from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone

from course.models import Course, CourseSchedule, CourseResource
from category.models import Category, SubCategory

from category.serializers import CategorySerializer
from django.utils.translation import ugettext as _

# Create your views here.
class SearchView(TemplateView):
    template_name = 'search/search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        # Generar las categorias y subcategorias para el selector
        categories = []
        for category in Category.objects.all():
            subcategories = []
            for subcategory in category.subcategory.all():
                subcategories.append([subcategory.id, _(subcategory.subcategory)])
            new_category = [_(category.category), category.id, category.icon, subcategories]
            categories.append(new_category)

        context['fields'] = {
            'categories': {
                'options': categories
            }, 'course_type': {
                'options': [(choice[0], _(choice[1])) for choice in Course.COURSE_TYPE_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'course_level': {
                'options': [(choice[0], _(choice[1])) for choice in Course.COURSE_LEVEL_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'location_mode': {
                'options': [(choice[0], _(choice[1])) for choice in Course.LOCATION_MODE_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'location_type': {
                'options': [(choice[0], _(choice[1])) for choice in Course.LOCATION_TYPE_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'payment_type': {
                'options': [(choice[0], _(choice[1])) for choice in Course.PAYMENT_TYPE_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'discount_type': {
                'options': [(choice[0], _(choice[1])) for choice in Course.DISCOUNT_TYPE_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'price_currency': {
                'options': [(choice[0], _(choice[1])) for choice in Course.PRICE_CURRENCY_CHOICES],  # pylint: disable=translation-of-non-string
            }, 'days_of_week': {
                'options': [(choice[0], _(choice[1])) for choice in CourseSchedule.DAYS_OF_WEEK],  # pylint: disable=translation-of-non-string
            }, 'course_language': {
                'options': [(choice[0], _(choice[1])) for choice in Course.LANGUAGE_TYPE_CHOICES],  # pylint: disable=translation-of-non-string
            }
        }

        return context
