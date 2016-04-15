from account.models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    '''Account model serializer'''
    transaction = serializers.SerializerMethodField()
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Account
        fields = ('timestamp', 'transaction', 'value')

    def get_transaction(self, obj):
        return obj.get_transaction_display()
