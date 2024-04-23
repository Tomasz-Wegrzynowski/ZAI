from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import Film, ExtraInfo, Ocena, Aktor
from .serializers import FilmModelSerializer, ExtraInfoSerializer, OcenaSerializer, AktorSerializer, UserSerializer
from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions
from .permissions import IsOwnerOrReadOnly

from .serializers import statRezyser, statOceny
from django.db.models import Count, Q, Max, Min
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Użytkownicy': reverse('ListaUzytkownikow', request=request, format=format),
        'Wszystkie filmy': reverse('ListaFilmow', request=request, format=format),
        'Informacje dodatkowe': reverse('InformacjeDodatkowe', request=request, format=format),
        'Wszystkie oceny': reverse('Recenzje', request=request, format=format),
        'Wszyscy aktorzy': reverse('Aktorzy', request=request, format=format),
        'Statystyki_rezyser_liczba_filmow': reverse('statRezyserLiczbaFilmow', request=request, format=format),
        'Statystyki_filmy_liczba_ocen': reverse('statFilmyLiczbaOcen', request=request, format=format),
        'Statystyki_filmy_bez_ocen': reverse('statFilmyBezOcen', request=request, format=format),
        'Statystyki_filmy_dobre_slabe': reverse('statFilmyKategorieDobrySlaby', request=request, format=format),
        'Statystyki_filmy_gwiazdki_max_min': reverse('statFilmyGwiazdkiMaxMin', request=request, format=format),

    })



class FilmCreateList(generics.ListCreateAPIView):
    queryset = Film.objects.all().order_by('-rok','tytul')
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['tytul', 'opis', 'rok']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Film.objects.all().order_by('-rok','tytul')
        tytul = self.request.query_params.get('tytul')
        id = self.request.query_params.get('id')
        if tytul is not None:
            queryset = queryset.filter(tytul__startswith=tytul)
        if id is not None:
            queryset = queryset.filter(id__exact=id)
        return queryset


class FilmRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ExtraInfoCreateList(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class ExtraInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class OcenaCreateList(generics.ListCreateAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class OcenaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class AktorCreateList(generics.ListCreateAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class AktorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class UserCreateList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class statRezyserLiczbaFilmow(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statRezyser
    rezyserOK = set([r.rezyser for r in ExtraInfo.objects.filter(rezyser__isnull=False)])
    rf = []

    for r in rezyserOK:
        rf.append([r,Film.objects.filter(extrainfo__rezyser__exact=r).count()])

    rf.sort(key=lambda a: a[1], reverse=True)
    queryset = rf


class statFilmyLiczbaOcen(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statOceny
    filmy = Film.objects.filter(ocena__id__isnull=False).annotate(l_ocen=Count("ocena__id")).order_by("-l_ocen")
    fo = []

    for f in filmy:
        fo.append([f.tytul, f.l_ocen])

    fo.sort(key=lambda a: a[1], reverse=True)
    queryset = fo


class statFilmyKategorieDobrySlaby(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statOceny
    dobry = Count("ocena__id", filter=Q(ocena__gwiazdki__gt=5))
    slaby = Count("ocena__id", filter=Q(ocena__gwiazdki__lte=5))
    filmy = Film.objects.filter(ocena__id__isnull=False).annotate(dobry=dobry).annotate(slaby=slaby)
    fk = []

    for f in filmy:
        fk.append([f.tytul, f.dobry, f.slaby])

    queryset = fk


class statFilmyGwiazdkiMaxMin(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statOceny
    gmax = Max("ocena__gwiazdki")
    gmin = Min("ocena__gwiazdki")
    filmy = Film.objects.filter(ocena__id__isnull=False).annotate(gmax=gmax).annotate(gmin=gmin)
    fk = []

    for f in filmy:
        fk.append([f.tytul, f.gmax, f.gmin])

    fk.sort(key=lambda a: a[1], reverse=True)
    queryset = fk


class statFilmyBezOcen(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FilmModelSerializer
    queryset = Film.objects.filter(ocena__id__isnull=True)