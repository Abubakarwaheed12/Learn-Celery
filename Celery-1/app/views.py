from django.shortcuts import render , HttpResponse
from app.tasks import send_review_email
from django.contrib.auth import get_user_model
# Create your views here.



def home(request):

    # user = get_user_model()
    # print('User  :  '  , user )
    
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            message = request.POST.get('message')
            print('email' , email , 'message' , message)

            
            recipient_list = [email ]
            send_review_email.delay(message , recipient_list )

            context = {'msg':'Thank For Your Review!!!'}
            

            return render(request , 'index.html' , context)        

    except Exception as e:
        print(e)

    return render(request , 'index.html')