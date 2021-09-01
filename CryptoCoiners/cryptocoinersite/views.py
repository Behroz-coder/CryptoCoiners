from django.http import request, response
from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from cryptocoinersite.models import Extend , Coin , CoinVoter, Banner
from django.contrib import messages
import re
import requests
import json
from django.shortcuts import redirect, HttpResponseRedirect
from pycoingecko import CoinGeckoAPI
from django.core.files.storage import FileSystemStorage


def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        addimage= Banner(image=upload)
        addimage.save()
        print(upload)
        # file = fss.save(upload.name, upload)
        # file_url = fss.url(file)
        return redirect('/adds')
    return render(request, 'adminsite/upload.html')


# Create your views here.
def index(index):
    promote = Coin.objects.filter(class_type='promoted',coin_status=True)
    todayhot = Coin.objects.filter(class_type='todayhot',coin_status=True)
    banners = Banner.objects.all()
   
    
   
    coinvote=''
    if(index.user.username ): 
        # print('d',index.user.id) 
        user = User.objects.get(username=index.user.username)
        coinvote = CoinVoter.objects.filter(user=user)
        # join = Coin.objects.annotate(j=CoinVoter()) 
        # print(join)
        # print(allcoin)
    return render(index, 'cryptocoinersite/home.html' , {'promote':promote,'coinvote':coinvote , 'coins':todayhot ,'banners':banners}) 
    
def new(index):
    banners = Banner.objects.all()
    promote = Coin.objects.filter(class_type='promoted',coin_status=True)
    new = Coin.objects.filter( class_type='new',coin_status=True)
    coinvote=''
    if(index.user.username ): 
        # print('d',index.user.id) 
        user = User.objects.get(username=index.user.username)
        coinvote = CoinVoter.objects.filter(user=user)
        # join = Coin.objects.annotate(j=CoinVoter()) 
        print(coinvote) 
        # print(allcoin)
    return render(index, 'cryptocoinersite/home.html' , {'promote':promote,'coinvote':coinvote , 'coins':new,'banners':banners}) 
    
def all(index):
    banners = Banner.objects.all()
    promote = Coin.objects.filter(class_type='promoted',coin_status=True)
    alltimebest = Coin.objects.filter(class_type='alltimebest',coin_status=True)
    coinvote=''
    if(index.user.username ): 
        # print('d',index.user.id) 
        user = User.objects.get(username=index.user.username)
        coinvote = CoinVoter.objects.filter(user=user)
        # join = Coin.objects.annotate(j=CoinVoter()) 
        # print(join)
        # print(allcoin)
    return render(index, 'cryptocoinersite/home.html' , {'banners':banners, 'promote':promote,'coinvote':coinvote , 'coins':alltimebest}) 
    
def presale(index):
    banners = Banner.objects.all()
    promote = Coin.objects.filter(class_type='promoted',coin_status=True)
    presale = Coin.objects.filter(class_type='presale',coin_status=True)
    coinvote=''
    if(index.user.username ): 
        # print('d',index.user.id) 
        user = User.objects.get(username=index.user.username)
        coinvote = CoinVoter.objects.filter(user=user)
        # join = Coin.objects.annotate(j=CoinVoter()) 
        # print(join)
        # print(allcoin)
    return render(index, 'cryptocoinersite/home.html' , {'banners':banners, 'promote':promote,'coinvote':coinvote , 'coins':presale}) 
    
def myvote(request):
    allcoin = Coin.objects.all()
    coinvote=''
    if(request.user.username ): 
        # print('d',request.user.id) 
        user = User.objects.get(username=request.user.username)
        coinvote = CoinVoter.objects.filter(user=user)
        # join = Coin.objects.annotate(j=CoinVoter()) 
        # print(join)
        # print(allcoin)
    return render(request, 'cryptocoinersite/myvote.html' , {'allcoin':allcoin,'coinvote':coinvote}) 
    
def disclaimer(request):
    return render(request, 'cryptocoinersite/disclaimer.html' )

def promote(request):
    return render(request, 'cryptocoinersite/promote.html' )

def coin(request,id):
    
    coin = Coin.objects.get(id = id)
    if request.method == "POST" and "vote" in request.POST:
        user = User.objects.get(username=request.user.username)
        
        addvote = CoinVoter(user=user,coinid=coin)
        addvote.save()
        coin.vote = coin.vote + 1
    #    print('vote = ',coin.vote)
        coin.save()
       
    coinvote=''
    if(request.user.username ): 
        # print('d',request.user.id) 
        user = User.objects.get(username=request.user.username)
        if(CoinVoter.objects.filter(coinid=coin,user=user)):
            coinvote = CoinVoter.objects.get(coinid=coin,user=user)
        

    
    return render(request, 'cryptocoinersite/coinpage.html',{'coin':coin,'coinvote':coinvote} )

def privacy(request):
    return render(request, 'cryptocoinersite/privacy.html' )

def terms(request):
    return render(request, 'cryptocoinersite/terms.html' )

def addcoin(request):
    if request.method == "POST":
        # Get the post parameters
        if(request.user.username):
            print(request.user.username)
            user = User.objects.get(username=request.user.username)
        else:
            user = ''
        # user = User.objects.get(username=request.user.username)
        te='' 
        coin_id = request.POST['coinid']
        description = request.POST['description']
        website = request.POST['website']
        telegram = request.POST['telegram']
        twitter = request.POST['twitter']
        discord = request.POST['discord']
        reddit = request.POST['reddit']
        logo = request.POST['logo']
        additionalInfo = request.POST['additionalInfo']
        launchDate = request.POST['launchDate']
        t = requests.get("https://api.coingecko.com/api/v3/coins/"+coin_id+"?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true").text
        te = json.loads(t)
        
        coin_id=''
        coin_name=''
        coin_symbol=''
        coin_dis=''
        market_cap=''
        price=''
        h1=''
        h24=''
        launch_date=''
        image=''

        if('error' in te):
            messages.success(request, "Your Coin Not found.")
            return redirect('/addcoin')
        else:
            pass 
            coin_id = te['id']
            coin_name = te['name']
            coin_symbol = te['symbol']
            coin_dis = te['description']['en']
            price = te['market_data']['current_price']['usd']
            market_cap = te['market_data']['market_cap']['usd']
            h1 = te['market_data']['price_change_percentage_1h_in_currency']['usd']
            h24 = te['market_data']['price_change_percentage_24h']
            image = te['image']['large']
            # print(h24) 
            addcoin = Coin(coin_id=coin_id,
            coin_name=coin_name,
            coin_symbol=coin_symbol,
            coin_dis=coin_dis,
            price=price,
            market_cap=market_cap,
            h1=h1,
            h24=h24,
            image=image,
            coin_discription = description, 
            launch_date = launchDate,
            website = website,
            telegram = telegram,
            twitter = twitter,
            discord = discord,
            reddit = reddit,
            logo = logo,
            additional_info = additionalInfo,
            vote = 0,
            user = user,
            class_type = 'none',
            )
            addcoin.save()
        
        # name = request.POST['name']
        # symbol = request.POST['symbol']
        
        # marketCap = request.POST['marketCap']
        # price = request.POST['price']
        
        
       
        # addcoin = Coin(coin_name = name, 
        # coin_symbol = symbol, 
        
        # market_cap = marketCap, 
        # price = price,
        
        
        
        # )
        # addcoin.save()
        # print(name)
         
        messages.success(request, "Your Coin is added successfully Please wait for approrvel.")
        return redirect('/addcoin')


    return render(request, 'cryptocoinersite/addcoin.html')
 
def ulogin(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  
        if user is not None:
            accounttype = Extend.objects.get(user=user)
            type = accounttype.user_type
            login(request  , user)
            if(type=="user"):
                request.session['Utype']=type
                return redirect('/')
                # return render(request, 'cryptocoinersite/home.html')
            if(type=="admin"):
                request.session['Utype']=type
                return redirect('/')
                # return render(request, 'company/dashboard.html')
        
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "cryptocoinersite/login.html")
    return render(request, "cryptocoinersite/login.html")
def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'cryptocoinersite/registration.html')
        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'cryptocoinersite/registration.html')
         
        # muser = User.objects.all()
        # for itme in muser:
        #     if(itme.email==email):
        #         messages.error(request, "Email is already exits.")
        #         return render(request, 'vib/signup.html')
        #         break

        # try:
        #     uemail = User.objects.get(email=request.POST['email'])

        # except User.DoesNotExist as e:
        #     messages.error(request, "Email is already exits.")
            

        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'cryptocoinersite/registration.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'cryptocoinersite/registration.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'cryptocoinersite/registration.html')
        
        if(re.search(regex,email)):   
           print("Valid Email")   
        else:   
           messages.error(request, " invalid email")
           return render(request, 'cryptocoinersite/registration.html') 
         
        # Create the user
        user = User.objects.create_user(username, email, password)
        print(user)
        user_type = 'user'
        # if user_type == "Company":
        #     company_name =request.POST['companyName']
        #     userType = Extend(user_type = user_type , user=user, company_name=company_name)
        # else:
        #     userType = Extend(user_type = user_type , user=user)
        userType = Extend(user_type = user_type , user=user)
        userType.save()
        user.save()
        
        messages.success(request, "You have succesfully Registerd.")
        return render(request, 'cryptocoinersite/registration.html')
    return render(request, 'cryptocoinersite/registration.html')

def ulogout(request):
    logout(request)
    try:
        del request.session['Utype']
    except KeyError:
        pass
    return redirect('/')