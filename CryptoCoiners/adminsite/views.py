from django.shortcuts import render,HttpResponseRedirect,redirect
from cryptocoinersite.models import Coin,Extend,CoinVoter,Banner
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request, 'adminsite/home.html' )
def allcoin(request):
    allcoin = Coin.objects.all()
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

def update(request, id):
    if request.method == "POST":
        # Get the post parameters
        # job_title = request.POST['job_title']
        # job_discription = request.POST['job_discription']
        
        # # Create the job
        # ujob = Jobs.objects.get(id=id)
        # ujob.job_title = job_title
        # ujob.job_discription = job_discription
        # ujob.save()
        print('ok')
        
        # messages.success(request, "Your job is updated successfully.")
        return redirect('/allcoin')
        #return render(request, 'company/jobs.html')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
       
    # user = User.objects.get(username=request.user.username)
    coin = Coin.objects.get( id=id)
    #print(ujob)
    context = {'coin':coin}
    #print(alljobs)
    return render(request, 'cryptocoinersite/addcoin.html', context)
