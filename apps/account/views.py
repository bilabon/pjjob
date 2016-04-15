import datetime
from datetime import timedelta
from django.views.generic import TemplateView
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView


from account.models import Account
from account.serializers import AccountSerializer


class HomeView(TemplateView):
    template_name = 'home.html'


class AccountRangeList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @staticmethod
    def get_range_dates(start, end):
        filter_range = (
            datetime.datetime.combine(start, datetime.time.min),
            datetime.datetime.combine(end, datetime.time.max)
        )
        return filter_range

    def filter_queryset(self, queryset):
        queryset = super(AccountRangeList, self).filter_queryset(queryset)

        start = self.request.GET.get('start')
        end = self.request.GET.get('end')

        if not all([start, end]):
            end = datetime.datetime.now().date()
            start = end - timedelta(days=30)
        else:
            try:
                start = datetime.datetime.strptime(start, '%Y-%m-%d')
                end = datetime.datetime.strptime(end, '%Y-%m-%d')
            except ValueError:
                raise APIException("Wrong datetime format.")

        filter_range = self.get_range_dates(start, end)
        queryset = queryset.filter(
            user=self.request.user,
            timestamp__range=filter_range
        )
        return queryset
