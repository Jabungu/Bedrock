from django.urls import path     
from . import views

urlpatterns = [
    path('', views.maps),
    path('poll', views.poll),
    path('register', views.registration),
    path('login', views.login),
    path('passwordReset', views.passwordReset),
    path('pwResetEmail', views.pwResetEmail),
    path('sendResetEmail', views.emailSent),
    path('pollAnswers', views.submitAnswers),
    path('addUser', views.addUser),
    path('updated', views.pollSuccess),
    path('loggingIn', views.authentication),
    path('verified', views.verified),
    path('about', views.about),
    path('comment', views.comment),
    path('editComment/<int:id>', views.editComment),
    path('starComment/<int:id>', views.starComment),
    path('unstarComment/<int:id>', views.starComment),
    path('trashComment/<int:id>', views.deleteComment),
    path('sendConnectionRequest/<int:id>', views.addConnection),
    path('likeComment/<int:id>', views.likeComment),
    path('docs', views.docs),
    path('profile/<int:id>,' views.profile)
    
] 
