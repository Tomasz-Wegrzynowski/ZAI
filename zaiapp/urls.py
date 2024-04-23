"""
URL configuration for ZAI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


from .views import FilmCreateList, FilmRetrieveUpdateDestroy,  ExtraInfoCreateList, ExtraInfoRetrieveUpdateDestroy, \
    OcenaCreateList, OcenaRetrieveUpdateDestroy, AktorCreateList, AktorRetrieveUpdateDestroy, \
    UserCreateList, UserRetrieveUpdateDestroy, statRezyserLiczbaFilmow, statFilmyLiczbaOcen, statFilmyBezOcen, statFilmyKategorieDobrySlaby, statFilmyGwiazdkiMaxMin
from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_root, name='api-root'),
    path('filmy/', FilmCreateList.as_view(), name= 'FilmCreateList'),
    path('filmy/<int:pk>/', FilmRetrieveUpdateDestroy.as_view(), name= 'FilmRetrieveUpdateDestroy'),
    path('extrainfo/', ExtraInfoCreateList.as_view(), name='ExtraInfoCreateList'),
    path('extrainfo/<int:pk>/',ExtraInfoRetrieveUpdateDestroy.as_view(), name='ExtraInfoRetrieveUpdateDestroy'),
    path('ocena/', OcenaCreateList.as_view(), name='OcenaCreateList'),
    path('ocena/<int:pk>/',OcenaRetrieveUpdateDestroy.as_view(), name='OcenaRetrieveUpdateDestroy'),
    path('aktor/', AktorCreateList.as_view(), name='AktorCreateList'),
    path('aktor/<int:pk>/', AktorRetrieveUpdateDestroy.as_view(), name='AktorRetrieveUpdateDestroy'),
    path('user/', UserCreateList.as_view(), name='UserCreateList'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='UserRetrieveUpdateDestroy'),
    path('statRezyserLiczbaFilmow/', statRezyserLiczbaFilmow.as_view(), name='statRezyserLiczbaFilmow'),
    path('statFilmyLiczbaOcen/', statFilmyLiczbaOcen.as_view(), name='statFilmyLiczbaOcen'),
    path('statFilmyBezOcen/', statFilmyBezOcen.as_view(), name='statFilmyBezOcen'),
    path('statFilmyDobrySlaby/', statFilmyKategorieDobrySlaby.as_view(), name='statFilmyKategorieDobrySlaby'),
    path('statFilmyGwiazdkiMaxMin/', statFilmyGwiazdkiMaxMin.as_view(), name='statFilmyGwiazdkiMaxMin'),

]

