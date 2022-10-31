from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer

from django.db.models import Q

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter


    def get_queryset(self):
        user = self.request.user
        print(user)
        if self.request.user and self.request.user.is_authenticated:
            return Advertisement.objects.filter(~Q(status='DRAFT') | (Q(status='DRAFT') & Q(creator=user)))
        else:
            return Advertisement.objects.filter(~Q(status='DRAFT'))

    def get_permissions(self):
        """Получение прав для действий."""

        # Создавать могут только авторизованные пользователи.
        if self.action in ["create"]:
            return [IsAuthenticated(),]
        # Обновлять и удалять объявление может только автор этого объявления.
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly(),]
        return []

