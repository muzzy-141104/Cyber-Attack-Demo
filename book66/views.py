from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from book66.models import CustomUser,Book,Author 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import re

def home(request):
    user_profile = request.user if request.user.is_authenticated else None
    return render(request, 'home.html', {'user_profile': user_profile})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            request.session['user_type'] = user.user_type
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
            return redirect('login')
    return render(request, 'login.html')


# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_type = request.POST.get('user_type')
#         m_password = make_password(password)
#         #filters      
#         # Validate username
#         if not is_valid_username(username):
#             messages.error(request, 'Invalid username format.')
#             return redirect('register')

#         # Validate email
#         try:
#             validate_email(email)
#         except ValidationError:
#             messages.error(request, 'Invalid email address.')
#             return redirect('register')

#         # Validate password
#         if not is_valid_password(password):
#             messages.error(request, 'Password must be at least 8 characters long.')
#             return redirect('register')

#         # Check if username or email already exists
#         if CustomUser.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists.')
#             return redirect('register')

#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists.')
#             return redirect('register')

#         # Create user
#         try:
#             user = CustomUser.objects.create(username=username, email=email, password=m_password, user_type=user_type)
#             login(request, user)
#             messages.success(request, 'User registered successfully!')
#             return redirect('home')
#         except Exception as e:
#             messages.error(request, 'An error occurred. Please try again.')
#             return redirect('register')

#     # If it's a GET request or form submission failed, render the registration form
#     return render(request, 'register.html')

# def is_valid_username(username):
#     # Allows only alphanumeric characters and underscores
#     return re.match(r'^\w+$', username) is not None

# def is_valid_password(password):
#     return len(password) >= 8

    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']
        m_password=make_password(password)


        # Check if the username or email is already in use
        if CustomUser.objects.filter(username=username).exists() or CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Username or email is already in use. Please choose another.')
            return redirect('register')

        # Create a new user
        user = CustomUser.objects.create(username=username, email=email, password=password, user_type=user_type)

        # Log the user in
        login(request, user)

        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('home')  # Redirect to the home page or wherever you want after successful registration

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_name = request.POST['author']
        publication_date = request.POST['publication_date']
        price = request.POST.get('price')
        author, created = Author.objects.get_or_create(name=author_name)

       
        book = Book.objects.create(
            title=title,
            author=author,
            publication_date=publication_date, 
            price=price  
            
        )

        return redirect('home')  
    else:
        return render(request, 'add_book.html')

def img(request):
    return render(request, 'img.html')

def add_description(request, book_id):
    book = Book.objects.get(pk=book_id)
    
    if request.method == 'POST':
        description = request.POST['description']
        book.description = description
        book.save()
        return redirect('home')
    else:
        return render(request, 'add_description.html', {'book': book})


#about page
def about(request):
    return render(request, 'about.html')
#category page
def category(request):
    return render(request, 'category.html')
#comics
def comics(request):    
    return render(request, 'comics.html')

def avatar(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'avatar.html',context)

def punch(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'punch.html',context)

def jjk(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'jjk.html',context)

def big(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'big.html',context)

#horror
def horror(request):
    return render(request, 'horror.html')

def draeula(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'draeula.html',context)

def ghosts(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'ghosts.html',context)

def playthings(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'playthings.html',context)

def that_things(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'that_things.html',context)

#psychology
def psychology(request):    
     return render(request, 'psychology.html')

def dark(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'dark.html',context)

def behave(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'behave.html',context)

def hooked(request):
    book=Book.objects.all()  
    context={'book':book}    
    return render(request, 'hooked.html',context)

def psycho_enterance_exam(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'psycho_enterance_exam.html',context)

#sc-fi
def sci_fi(request):     
    return render(request, 'sci_fi.html')

def samsara(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'samsara.html',context)

def wrilane(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'wrilane.html',context)

def alchemist(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'alchemist.html',context)

def silent(request):
    book=Book.objects.all()  
    context={'book':book}
    return render(request, 'silent.html',context)

def buy(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'buy.html', {'book': book})

@login_required(login_url='login')
def buyer_dashboard(request):
    user = request.user
    orders = user.orders.all()
    context = {
        'user': user,
        'orders': orders,    
    }
    return render(request, 'buyer_dashboard.html', context)

@login_required(login_url='login')
def sellers_dashboard(request):
    # Retrieve seller details based on the current user
    user=request.user
    books = Book.objects.all()  # Assuming Book is your model
    return render(request, 'sellers_dashboard.html',{'books': books })

@csrf_exempt
def change_email(request):
    if request.method == 'POST':
        user = request.user
        new_email = request.POST.get('new_email')
        if new_email:
            user.email = new_email
            user.save()
            messages.success(request, 'Email address updated successfully.')
            # No redirection
        else:
            messages.error(request, 'New email address not provided.')
        # Always return the same page
        return render(request, 'change_email.html')
    else:
        # Handle GET request appropriately, maybe render a form
        return render(request, 'change_email.html')
