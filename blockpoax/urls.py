from django.contrib import admin
from django.urls import path, include

from public import views as public
from userauth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public.home, name='home'),
    path('contact', public.contact, name='contact'),
    path('resend-email', public.resendEmail, name='resend-email'),
    path('verify-email/<token>', public.verify, name='verify-email'),
    path('privacy-policy', public.privacyPolicy, name='privacy-policy'),
    path('terms-and-conditions', public.tandc, name='tandc'),
    path('refund-policy', public.refundPolicy, name='refund-policy'),
    path('our-services', public.ourServices, name='our-services'),
    path('disclaimer', public.disclaimer, name='disclaimer'),
    path('about-us', public.aboutUs, name='about-us'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login', auth.login, name='login'),
    path('register', auth.register, name='register'),
    path('logout', auth.logout, name='logout'),
    path('api/', include('api.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('email-not-verified', auth.emailNotVerified, name="email-not-verified"),
]

handler404 = 'public.views.handler404'
handler500 = 'public.views.handler500'