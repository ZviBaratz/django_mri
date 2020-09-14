from django_mri.models.session import Session
from django_mri.serializers import SessionSerializer
from django_mri.views.defaults import DefaultsMixin
from django_mri.views.pagination import StandardResultsSetPagination
from rest_framework import viewsets


class SessionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows scans to be viewed or edited.
    """

    pagination_class = StandardResultsSetPagination
    queryset = Session.objects.order_by("-time__date", "time__time")
    serializer_class = SessionSerializer
    ordering_fields = ("url", "subject", "comments", "time", "scan_set")