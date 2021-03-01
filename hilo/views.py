from django.shortcuts import render, HttpResponse, redirect
from hilo.models import *
from django.contrib import messages
import bcrypt

def maps(request):
    context = {
        "data" : Poll.objects.all(),            
        "current_user": User.objects.get(userId= request.session['id']),
        "comment": Comment.objects.all().order_by('-created_at'),
        "Favorited": Favorite.objects.all()

    }
    return render(request, 'maps.html', context)
def poll(request):
    return render(request, 'poll.html')
def registration(request):
    return render(request, 'register.html')
def addUser(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        print("this is where userpic should be")
        print(request.POST.get('image'))
        newuser= User.objects.create(username = request.POST['username'], first_name = request.POST['firstName'], last_name = request.POST["lastName"], Email=request.POST["email"], password=pw_hash, Address_Line_1= request.POST['ad1'], Address_Line_2 = request.POST['ad2'], City = request.POST['city'], State = request.POST['state'], Zip = request.POST['zip'], Country = request.POST['country'], image=request.POST.get('image'))
        request.session['id'] = newuser.userId
        request.session['registered_user']= newuser.username
        return redirect("/poll")
def login(request):
    return render(request, 'login.html')
def passwordReset(request):
    return render(request, 'passwordReset.html')
def pwResetEmail(request):
    return render(request, 'pwResetEmail.html')
def emailSent(request):
    return render(request, 'emailSent.html')
def submitAnswers(request):
    pollAnswers = Poll.objects.create(user = User.objects.get(userId=request.session['id']), water = request.POST['water-working'], electricity = request.POST["elec-working"], electricity_provider=request.POST["elec-provider"], internet=request.POST['internet-working'], internet_provider=request.POST['internet-provider'])
    return redirect('/updated')
def pollSuccess(request):

    return render(request, 'pollSubmitted.html')
def authentication(request):
    user = User.objects.filter(username = request.POST['username'])
    errors = User.objects.login_validator(request.POST)
    if user:
        logged_user = user[0]
        print ("username found")
    else:
        print("username not found")
        return redirect('/login')   

    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session['id'] = logged_user.userId
        print("The user ID is below:")
        print (request.session["id"])
        return redirect('/verified')   
    else:
        password_incorrect = "Incorrect password. Please try again."
        print(password_incorrect)
        
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # HOMEWORK: Add password and username error message, add login with email capability
    return redirect('/login')
def verified(request):
    
    context= {
        "current_user": User.objects.get(userId= request.session['id']),
        "comment": Comment.objects.all()
    }
    return render(request, 'maps.html', context)
def about(request):
    return render(request,'about.html')
def comment(request):
    Comment.objects.create(user= User.objects.get(userId= request.session['id']), post = request.POST['comment'])
    return redirect('/')
def editComment(request):
    return redirect('/')
def starComment(request, id):
    commentid= id

    thecomment=Comment.objects.get(id=commentid)
    Favorite.objects.create(user_id=request.session['id'], comment_id=thecomment.id)
    
    return redirect('/')
def unstarComment(request):
    thecomment=Comment.objects.get(id=request.params.id)
    Favorite.objects.get(user=request.session['id'], comment= thecomment).delete()
    return redirect('/')
def deleteComment(request, id):
    thecommentid= id
    thecomment=Comment.objects.get(id=thecommentid)
    Comment.objects.get(id=thecomment.id).delete()
    return redirect('/')
def addConnection(request, id):
    thecomment=Comment.objects.get(id=id)
    to= thecomment.user
    Connection_request.objects.create(from_user= User.objects.get(userId=request.session['id']), to_user= to, status="p")
    return redirect('/')
def likeComment(request):
    thecomment=Comment.objects.get(id=request.params.id)
    Like.objects.create(user=thecomment.user, post=thecomment)
    return redirect('/')
def docs(request):  
    return render(request, 'docs.html')
def profile(request):
    return render(request, 'profile.html' )
