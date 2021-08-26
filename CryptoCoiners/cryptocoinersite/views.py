from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from cryptocoinersite.models import Extend , Coin
from django.contrib import messages
import re
from django.shortcuts import redirect, HttpResponseRedirect




# Create your views here.
def index(index):
    allcoin = Coin.objects.all()
    return render(index, 'cryptocoinersite/home.html' , {'allcoin':allcoin})
    
def disclaimer(request):
    return render(request, 'cryptocoinersite/disclaimer.html' )

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
        name = request.POST['name']
        symbol = request.POST['symbol']
        description = request.POST['description']
        marketCap = request.POST['marketCap']
        price = request.POST['price']
        launchDate = request.POST['launchDate']
        website = request.POST['website']
        telegram = request.POST['telegram']
        twitter = request.POST['twitter']
        discord = request.POST['discord']
        reddit = request.POST['reddit']
        logo = request.POST['logo']
        additionalInfo = request.POST['additionalInfo']
        # question = request.POST['question']
        # answer = request.POST['answer']
        # timeddl = 1
        # # Create the job
        # user = User.objects.get(username=request.user.username)
        # job = Jobs.objects.get(job_title=job_title)
       
        addcoin = Coin(coin_name = name, coin_symbol = symbol, coin_discription = description, 
        market_cap = marketCap, 
        price = price,
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
        
        
        )
        addcoin.save()
        print(name)
         
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