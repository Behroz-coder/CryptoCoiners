from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Extend(models.Model):
    id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length= 15)
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user, self.user_type)
    
class Coin(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    user = models.CharField(max_length=20)
    coin_id = models.CharField(max_length=200)
    coin_name = models.CharField(max_length=200)
    coin_symbol = models.CharField(max_length=200)
    coin_discription = models.CharField(max_length=800)
    coin_dis = models.CharField(max_length=800)
    market_cap = models.CharField(max_length=200)
    h1 = models.CharField(max_length=200)
    h24 = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    launch_date = models.DateField((""), auto_now=False, auto_now_add=False)
  
    website = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    discord = models.CharField(max_length=200)
    reddit = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    additional_info = models.CharField(max_length=800)
    vote = models.IntegerField(default=0) 
    image = models.CharField(max_length=900)

    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    class_type = models.CharField(max_length= 100)
    coin_status =models.BooleanField(default=False)
    
    def __str__(self):
        return "%s %s" % (self.coin_name, self.coin_symbol)

class CoinVoter(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    coinid = models.ForeignKey(Coin, on_delete=models.CASCADE ,null=True)
    

    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    coin_status =models.BooleanField(default=False)
    
    def __str__(self):
        return "%s %s" % (self.user, self.coinid)


class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    image1 = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img',default="")
    
   

    def __str__(self):
        return "%s" % (self.image)


