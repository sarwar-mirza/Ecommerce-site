from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_view
from .forms import UserLoginForm, UserChangePasswordForm, UserPasswordResetForm, UserSetPasswordConfirm


urlpatterns = [
    path('', views.ProductHomeView.as_view(), name='home'),

    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('baseball/', views.baseball, name='baseball'),
    path('baseballdata/<slug:data>/', views.baseball, name='baseballdata'),

    path('football/', views.football, name='football'),
    path('footballdata/<slug:data>/', views.football, name='footballdata'),

    path('cricket/', views.cricket, name='cricket'),
    path('cricketdata/<slug:data>/', views.cricket, name='cricketdata'),

    path('allproduct/', views.allproduct, name='allproduct'),

    
    path('registration/', views.RegistrationFormView.as_view(), name='registration'),

    path('accounts/login/', auth_view.LoginView.as_view(authentication_form = UserLoginForm, template_name ="app/login.html"), name='login'),

    path('profile/', views.UserProfileView.as_view(), name='profile'),

    path('address/', views.AddressView.as_view(), name='address'),

    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),   # Logout


    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name = 'app/changepassword.html', form_class = UserChangePasswordForm, success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name = 'app/changepassworddone.html'), name='changepassworddone'),
    

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class = UserPasswordResetForm), name='passwor_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html', form_class=UserSetPasswordConfirm, success_url='/password-reset-complete/'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'), name='password_reset_conmplete'),
  

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


