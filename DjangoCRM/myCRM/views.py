from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Record
from .forms import RecordForm


# Create your views here.
def homepage(request):
    records = Record.objects.all()
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have login successfully")
            return redirect('homepage')
        else:
            messages.error(request, 'No you have failed to login.')
            return redirect('homepage',)
    return render(request, 'home.html',  {'records':records})

def logginout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('homepage')

def SignupPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_mail = request.POST.get('user_mail')
        user_password = request.POST.get('password1')
        user_confirm_password = request.POST.get('password2')
        
        if user_password != user_confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'registers.html')
        else:
            my_user = User.objects.create_user(user_name, user_mail, user_password)
            my_user.save()
            messages.success(request, 'Succesfully Registered.')
            return redirect('homepage')

    return render(request, 'registers.html')

def customer_record(request,pk):
    if User.is_authenticated:
        customer_record  = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'Failed to find the account')
        return redirect('homepage')

def delete_record(request, pk):
        delete_rec = Record.objects.get(id=pk)
        delete_rec.delete()
        return redirect('homepage')

def add_record(request):
    if request.method == 'POST':
        u_first_name= request.POST.get('firstname')
        u_last_name = request.POST.get('lastname')
        u_mail = request.POST.get('usermail')
        u_phone = request.POST.get('PhoneNumber')
        u_city = request.POST.get('city')
        u_state = request.POST.get('state')
        
        record1 = Record(
            first_name= u_first_name,
            last_name = u_last_name,
            usermail = u_mail,
            phone = u_phone,
            city = u_city,
            state = u_state
        )
        record1.save()
        return redirect('SignupPage')
    return render(request, 'add_record.html')


def update_record(request, pk):
    if request.user.is_authenticated:
        c_record = get_object_or_404(Record, id=pk)
        if request.method == 'POST':
            form = RecordForm(request.POST, instance=c_record)
            if form.is_valid():
                form.save()
                return redirect('homepage')  # Redirect to the home page
        else:
            form = RecordForm(instance=c_record)
    else:
        form = None  # Handle the case when the user is not authenticated

    return render(request, 'update.html', {'form': form})
    

        