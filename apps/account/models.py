from django.db import models
from django.conf import settings


class Account(models.Model):
    '''Account model'''

    TRANSACTION_CHOICES = (
        ('I', 'Income'),
        ('E', 'Expense'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    transaction = models.CharField(max_length=1, choices=TRANSACTION_CHOICES)
    value = models.DecimalField(max_digits=13, decimal_places=4)

    timestamp = models.DateTimeField(auto_now_add=True)
    # timestamp.editable = True

    def __str__(self):
        return '({}) {}: {}, {}'.format(
            self.user,
            self.get_transaction_display(),
            self.value,
            self.timestamp.strftime("%Y-%m-%d %H:%M"),
        )
