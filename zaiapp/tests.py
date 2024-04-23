from django.test import TestCase

from django.urls import path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from django.contrib.auth.models import User
from .views import FilmCreateList, FilmRetrieveUpdateDestroy, ExtraInfoCreateList, UserCreateList, UserRetrieveUpdateDestroy, statRezyserLiczbaFilmow
from .models import Film


class TestyURL(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('filmy/', FilmCreateList.as_view(), name= 'FilmCreateList'),
        path('filmy/<int:pk>/', FilmRetrieveUpdateDestroy.as_view(), name='FilmRetrieveUpdateDestroy'),
    ]

    def test_FilmCreateList(self):
        url = reverse('FilmCreateList')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_FilmRetrieveUpdateDestroy(self):
        url = reverse('FilmRetrieveUpdateDestroy', args=[1])
        Film.objects.create(tytul="Film testowy", rok=2024, opis="opis")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class Testy_Widokow(APITestCase):

    def test_FilmCreateList_List(self):
        url = reverse('FilmCreateList')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #def test_FilmCreateList_Create(self):
    #    self.client.login(username='admin', password='admin')
    #    url = reverse('FilmCreateList')
    #    film = {'tytul': 'Film testowy', 'rok': 2024, 'opis': 'opis'}
    #    response = self.client.post(url, film, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #    self.assertEqual(Film.objects.count(), 1)
    #    self.assertEqual(Film.objects.get().tytul, 'Film testowy')
    #    self.assertEqual(Film.objects.get().rok, 2024)
    #    self.assertEqual(Film.objects.get().opis, 'opis')

    def test_FilmRetrieveUpdateDestroy_Retrieve(self):
        Film.objects.create(tytul="Film testowy", rok=2024, opis="opis")
        url = reverse('FilmRetrieveUpdateDestroy', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Film.objects.count(), 1)
        self.assertEqual(Film.objects.get().tytul, 'Film testowy')

    #def test_FilmRetrieveUpdateDestroy_Update(self):
    #    self.client.login(username='admin', password='admin')
    #    Film.objects.create(tytul="Film testowy 2", rok=2024, opis="opis", owner=User.objects.get(id=1))
    #    url = reverse('FilmRetrieveUpdateDestroy', args=[1])
    #    film = {'tytul': 'Film testowy', 'rok': 2020, 'opis': 'opis opis'}
    #    response = self.client.put(url, film, format='json', )
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    self.assertEqual(Film.objects.count(), 1)
    #    self.assertEqual(Film.objects.get().rok, 2020)
    #    self.assertEqual(Film.objects.get().tytul, 'Film testowy')
    #    self.assertEqual(Film.objects.get().opis, 'opis opis')

    #def test_FilmRetrieveUpdateDestroy_Destroy(self):
    #    self.client.login(username='admin', password='admin')
    #    Film.objects.create(tytul="Film testowy", rok=2024, opis="opis", owner=User.objects.get(id=1))
    #    url = reverse('FilmRetrieveUpdateDestroy', args=[1])
    #    response = self.client.delete(url)
    #    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #    self.assertEqual(Film.objects.count(), 0)

    #def test_statRezyserLiczbaFilmow(self):
    #    self.client.login(username='admin', password='admin')
    #    url = reverse('statRezyserLiczbaFilmow')
    #    response = self.client.get(url, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)

