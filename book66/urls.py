from . import views
from django.urls import path
from .views import user_login,register,add_book,add_description,logout,hooked,horror,home,about,alchemist,authenticate,avatar,img

urlpatterns = [
    path('home/',views.home,name='home'), 
    path('add-description/<int:book_id>/', views.add_description, name='add_description'),
    path('change_email/', views.change_email, name='change_email'),
    path('add-book/', views.add_book, name='add_book'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category_page'),
    path('img/', views.img, name='img'),
    path('comics/', views.comics, name='comics'),#comics
    path('avatar/', views.avatar, name='avatar'),
    path('punch/', views.punch, name='punch'),
    path('big/', views.big, name='big'),
    path('jjk/', views.jjk, name='jjk'),
    #horror
    path('draeula/', views.draeula, name='draeula'),
    path('ghosts/', views.ghosts, name='ghosts'),
    path('playthings/', views.playthings, name='playthings'),
    path('that_things/', views.that_things, name='that_things'),
    path('horror/', views.horror, name='horror'),
    #psychology
    path('dark/', views.dark, name='dark'),
    path('behave/', views.behave, name='behave'),
    path('hooked/', views.hooked, name='hooked'),
    path('psycho_enterance_exam/', views.psycho_enterance_exam, name='psycho_enterance_exam'),
    path('psychology/', views.psychology, name='psychology'),
    #sci-fi
    path('samsara/', views.samsara, name='samara'),
    path('wrilane/', views.wrilane, name='wrilane'),
    path('alchemist/', views.alchemist, name='alchemist'),
    path('silent/', views.silent, name='silent'),
    path('sci_fi/', views.sci_fi, name='sci_fi'),
    path('login/', views.user_login, name='login'),
    #buy
    path('buy/<int:book_id>/', views.buy, name='buy'),
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('sellers-dashboard/', views.sellers_dashboard, name='sellers_dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
]

