from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
# from vib.models import Extend
# Create your views here.
def index(index):
    return render(index, 'cryptocoinersite/home.html')
def addcoin(request):
    return render(request, 'cryptocoinersite/addcoin.html')
 
def ulogin(request):
    if request.method == "POST":
        # Get the post parameters
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)  
        # if user is not None:
        #     accounttype = Extend.objects.get(user=user)
        #     type = accounttype.user_type
        #     login(request  , user)
        #     if(type=="Candidate"):
        #         request.session['Utype']=type
        #         return redirect('/user/home1/')
                #return render(request, 'user/home.html')
            # if(type=="Company"):
            #     request.session['Utype']=type
            #     return redirect('/company/dashboard1/')
                #return render(request, 'company/dashboard.html')
        pass
    else:
            # messages.error(request, "Invalid credentials! Please try again")
        return render(request, "cryptocoinersite/login.html")
 
def signup(request):
    # if request.method == "POST":
    #     # Get the post parameters
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     cpassword = request.POST['cpassword']

    #     checkemail = User.objects.filter(email=email)
    #     checkuser = User.objects.filter(username=username)
    #     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #     if len(checkemail)>0:
    #         messages.error(request, "Email is already exits.")
    #         return render(request, 'vib/signup.html')
    #     if len(checkuser)>0:
    #         messages.error(request, "User Name is already exits.")
    #         return render(request, 'vib/signup.html')
        
    #     # muser = User.objects.all()
    #     # for itme in muser:
    #     #     if(itme.email==email):
    #     #         messages.error(request, "Email is already exits.")
    #     #         return render(request, 'vib/signup.html')
    #     #         break

    #     # try:
    #     #     uemail = User.objects.get(email=request.POST['email'])

    #     # except User.DoesNotExist as e:
    #     #     messages.error(request, "Email is already exits.")
            

    #     if len(username) > 10:
    #         messages.error(request, " Your user name must be under 10 characters")
    #         return render(request, 'vib/signup.html')

    #     if not username.isalnum():
    #         messages.error(request, " User name should only contain letters and numbers")
    #         return render(request, 'vib/signup.html')
    #     if password != cpassword:
    #         messages.error(request, " Passwords do not match")
    #         return render(request, 'vib/signup.html')
        
    #     if(re.search(regex,email)):   
    #        print("Valid Email")   
    #     else:   
    #        messages.error(request, " invalid email")
    #        return render(request, 'vib/signup.html') 
         
    #     # Create the user
    #     user = User.objects.create_user(username, email, password)
    #     print(user)
    #     user_type = request.POST['user_type']
    #     if user_type == "Company":
    #         company_name =request.POST['companyName']
    #         userType = Extend(user_type = user_type , user=user, company_name=company_name)
    #     else:
    #         userType = Extend(user_type = user_type , user=user)
    #     userType.save()
    #     user.save()
        
    #     messages.success(request, "You have succesfully Registerd.")
    #     return render(request, 'vib/signup.html')
    return render(request, 'cryptocoinersite/registration.html')

