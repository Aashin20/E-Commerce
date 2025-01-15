from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.TextField(max_length=200)
    description=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='media')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return self.title