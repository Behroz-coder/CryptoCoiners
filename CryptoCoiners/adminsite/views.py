from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect,redirect
from cryptocoinersite.models import Coin,Extend,CoinVoter,Banner
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request, 'adminsite/home.html' )
def allcoin(request):
    allcoin = Coin.objects.all()
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})
def promoted(request):
    allcoin = Coin.objects.filter(class_type='promoted')
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})
def today(request):
    allcoin = Coin.objects.filter(class_type='todayhot')
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})
def newcoins(request):
    allcoin = Coin.objects.filter(class_type='new')
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})
def alltimebest(request):
    allcoin = Coin.objects.filter(class_type='alltimebest')
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})
def presal(request):
    allcoin = Coin.objects.filter(class_type='presale')
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})


def newcoin(request):
    allcoin = Coin.objects.filter(coin_status=False)
    return render(request, 'adminsite/coin.html'  ,{'allcoin':allcoin})
def users(request):
    alluser = Extend.objects.filter(user_type='user')
    return render(request, 'adminsite/user.html'  ,{'alluser':alluser})
def adds(request):
    banner = Banner.objects.all()
    return render(request, 'adminsite/banner.html'  ,{'banner':banner})


def status(request, id):
    coin = Coin.objects.get(id=id)
    coin_status = coin.coin_status
    if coin_status:
        coin.coin_status = False
    else:
        coin.coin_status = True
    coin.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    #return redirect('/jobs/')
def delete(request, id):
    coin = Coin.objects.get(id=id)
    coin.delete()
    messages.success(request, "Your coin is deleted successfully.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def udelete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, "User is deleted successfully.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def update(request, id):
    if request.method == "POST":
        coin = Coin.objects.get(id=id)

        # Get the post parameters
        name = request.POST['name']
        symbol = request.POST['symbol']
        description = request.POST['description']
        marketCap = request.POST['marketCap']
        price = request.POST['price']
        # launchDate = request.POST['launchDate']
        website = request.POST['website']
        telegram = request.POST['telegram']
        twitter = request.POST['twitter']
        discord = request.POST['discord']
        reddit = request.POST['reddit']
        logo = request.POST['logo']
        additionalInfo = request.POST['additionalInfo']
        classtype = request.POST['ddl']


        coin.coin_name = name
        coin.coin_symbol = symbol
        coin.coin_discription = description
        coin.market_cap = marketCap
        coin.price = price
        coin.website = website
        coin.telegram = telegram
        coin.twitter = twitter
        coin.discord = discord
        coin.reddit = reddit
        coin.logo = logo
        coin.additional_info = additionalInfo 
        coin.class_type = classtype
       
        coin.save()

        # job_discription = request.POST['job_discription']
        
        # # Create the job
        # ujob = Jobs.objects.get(id=id)
        # ujob.job_title = job_title
        # ujob.job_discription = job_discription
        # ujob.save()
        # print('dd= ',classtype)
        
        messages.success(request, "Your Coin is updated successfully.")
        return redirect('/allcoin')
        #return render(request, 'company/jobs.html')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
       
    # user = User.objects.get(username=request.user.username)
    coin = Coin.objects.get( id=id)
    #print(ujob)
    context = {'coin':coin}
    #print(alljobs)
    return render(request, 'cryptocoinersite/addcoin.html', context)
