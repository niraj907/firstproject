from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect,  get_object_or_404
from .forms import contactForms
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import contactEnquiry
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
# def contact(request):
#     result = "" 
#     fn = contactForms()
#     data ={'form':fn} # dictionary to store data
#     try:
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         result = name + " " + email + " " + message
#         data = { 
#            'form': fn,
#             'output': result
#         }

#         url = '/about/?output={}'.format(result)
#         return redirect(url)
#     except:
#         pass    
#     return render(request, 'contact.html', data)

def contact(request):
     return render(request, 'contact.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')



# def saveEnquiry(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone', '')
#         websiteLink = request.POST.get('websiteLink', '')
#         message = request.POST.get('message')

#         contactEnquiry.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             websiteLink=websiteLink,
#             message=message
#         )
#         return redirect('contact')  # or show a success message

#     return render(request, 'contact.html')

from django.contrib import messages  # ✅ Make sure this is imported

def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        websiteLink = request.POST.get('websiteLink', '')
        message = request.POST.get('message')

        # Save to DB
        contactEnquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            websiteLink=websiteLink,
            message=message
        )

        # Send email
        try:
            subject = f"New Contact Enquiry from {name}"
            from_email = 'chaudhariiiniraj@gmail.com'
            to_email = 'np03cs4a220219@heraldcollege.edu.np'
            html_content = f"""
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Website Link:</strong> {websiteLink}</p>
                <p><strong>Message:</strong><br>{message}</p>
            """
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to_email])
            msg.content_subtype = "html"
            msg.send()

            # ✅ Success message added here
            messages.success(request, "Your enquiry was sent successfully!")

        except Exception as e:
            # ❌ Error message
            messages.error(request, f"Email not sent. Error: {e}")

        # ✅ Redirect to contact page after showing message
        return redirect('contact')

    return render(request, 'contact.html')



def test_email(request):
    print("Email view triggered")
    try:
        subject , from_email , to = 'Testing Email' , 'chaudhariiiniraj@gmail.com' , 'np03cs4a220219@heraldcollege.edu.np'
        html_content = '<p> This is a <strong> important </strong>message . </p>'
        msg = EmailMultiAlternatives(subject , html_content , from_email , [to])
        msg.content_subtype = "html"
        msg.send()
        return HttpResponse("Email Sent")
    except Exception as e:
        return HttpResponse(f"Error: {e}")




def about(request):
    # if request.method == "GET":
    #     output = request.GET.get('output')
    return render(request, 'about.html')

# def services(request):
#     servicesData = Service.objects.all().order_by('service_title')[:3]
    
#     data = {
#         'servicesData': servicesData
#     }
 
#     return render(request, 'services.html',data)

def services(request):
    servicesData = Service.objects.all().order_by('-service_title')[:3]
    print("Fetched services:", list(servicesData))
    return render(request, 'services.html', {'servicesData': servicesData})


# def blog(request): 
#     newsData = News.objects.all()
    
#     if request.method == "GET":
#         st = request.GET.get('newsname')
#         if st:
#             newsData = News.objects.filter(news_title__icontains=st)


# #     return render(request, 'blog.html', {'newsData': newsData}) 



# def blog(request):
#     st = request.GET.get('newsname')  # Search term
    # if st:
    #     newsData = News.objects.filter(news_title__icontains=st)
    # else:
    #     newsData = News.objects.all()

    # paginator = Paginator(newsData, 3)  # 3 news per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # context = {
    #     'page_obj': page_obj,
    #     'newsname': st or "",  # send search term to template
    # }
    # return render(request, 'blog.html', context)


# def newDeatils(request,news_slug):
#     newsData = News.objects.get(news_slug=news_slug)
#     return render(request, 'newDeatils.html',{'newsData': newsData})

# def newDeatils(request, news_slug):
#     newsData = get_object_or_404(News, news_slug=news_slug)
#     return render(request, 'newDeatils.html', {'newsData': newsData})

def submitForm(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        result = name + " " + email + " " + message
      
        data = { 
            'name': name,
            'email': email,
            'message': message,
            'output': result
        }
        return HttpResponse(result)
    except:
        return HttpResponse("Error processing form.")


def header(request):
    return render(request, 'header.html') 

def calculator(request):
    c =''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            operation = request.POST.get('operation')
            if operation == "+":
                c = n1 + n2;
            elif operation == "-":
                c = n1 - n2;
            elif operation == "*":
                c = n1 * n2 ;
            elif operation == "/":
                c = n1 / n2;    
            print(c)
    except:
        c = "Invalid operation"
    
    return render(request, 'calculator.html',{'c': c}) 

def index(request):
    return render(request, 'index.html') 



def marksheet(request):
    
    if request.method == "POST":
        S1 = eval(request.POST.get('subject1'))
        S2 = eval(request.POST.get('subject2'))
        S3 = eval(request.POST.get('subject3'))
        S4 = eval(request.POST.get('subject4'))
        S5 = eval(request.POST.get('subject5'))
        t = S1 + S2 + S3 + S3 + S4 + S5
        p = t * 100 / 500

        if p >= 90 and p <= 100:
            result = "Excellent Mark"
        elif p >= 80 and p < 90:
            result = "Distinction"
        elif p >= 70 and p < 80:
            result = "First Division"
        elif p >= 60 and p < 70:
            result = "Second Division"
        elif p >= 50 and p < 60:
            result = "Third Division"
        else:
            result = "Fail"


        return render(request, 'marksheet.html', {
            'total': t,
            'percentage': round(p, 2),
            'result': result,
        })

     
    return render(request, 'marksheet.html') 
 
