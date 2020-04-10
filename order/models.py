from django.db import models

# Create your models here.


class OrderLog(models.Model):
    mem_id = models.IntegerField()
    sub_id = models.IntegerField()
    price = models.IntegerField()
    result = models.BooleanField()
    pay_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orderlogs'

    def __str__(self):
        return str(self.mem_id)
