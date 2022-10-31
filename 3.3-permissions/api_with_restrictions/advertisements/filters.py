from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    status = filters.CharFilter()
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at', 'updated_at']
