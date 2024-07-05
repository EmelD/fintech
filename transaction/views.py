from rest_framework import filters, permissions, viewsets

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['wallet_id']
    ordering_fields = ['amount', 'wallet_id']
    http_method_names = ['get']
