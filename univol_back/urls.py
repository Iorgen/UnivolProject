"""univol_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views
from api_volunteers_search_supporter import views as external_api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('univol.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', user_views.register, name='register'),
    path('accounts/register/volunteer', user_views.volunteer_register, name='volunteer_signup'),
    path('accounts/register/organizator', user_views.organizator_register, name='organizator_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('fetch_from_vk/', external_api_views.get_vk_prediction_page, name='vk_settings_predictions'),
    path('fetch_from_vk/predict/', external_api_views.get_prediction_by_keyword_and_city, name='predict_vk'),

    # ----------------------
    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
    url(r'^rest-auth/', include('rest_api.urls')),
    url(r'^rest-auth/registration/', include('rest_api.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    url(r'^docs/$', get_swagger_view(title='API Docs'), name='api_docs'),

    # ---------------------------------------------------------------
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),
    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
