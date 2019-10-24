from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login-user',views.login_account, name = 'login_users'),
    path('logout-user',views.logout_account, name = 'logout_users'),
    path('homepage',views.homepage, name = 'home'),
    path('signup-user',views.signup, name = 'signup'),
    path('menu',views.menu, name = 'menu'),
    path('listprprty',views.viewproperties, name = 'listprprty'),
    path('addproperty',views.addproperty, name = 'addproperty'),
    path('showimage',views.showImage, name = 'showimage'),
    path('myproperties',views.myproperties, name = 'myproperties'),
    path('viewdetails',views.viewdetails, name = 'viewdetails'),
    path('<int:prop_id>/deactiveproperty',views.deactiveproperty, name = 'deactiveproperty'),
    path('<int:prop_id>/activeproperty',views.activeproperty, name = 'activeproperty'),
    # activeproperty
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)