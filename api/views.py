from django.contrib.auth.models import Group, User
from rest_framework import generics, mixins, permissions, viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response

from .models import Shorterlink
from .serializers import ShortlinkSerializer
from .permissions import IsAdminOrOwner


def build_url(request, link):
    sheme = request.scheme
    host = request.get_host()
    url = f"{sheme}://{host}/{link}"
    print(url)
    return url

@method_decorator(csrf_exempt, name='dispatch')
class ShorterlinkCreateAPIView(generics.CreateAPIView,):
    queryset = Shorterlink.objects.all()
    serializer_class = ShortlinkSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        link = request.data.get('link')
        try:
            existing_link = Shorterlink.objects.get(link=link)
            serializer = self.get_serializer(existing_link)
            # Cogemos los datos que hay dentro del serializer para cambiar uno de ellos
            data = serializer.data
            print(f"Data is {data}")
            data['short_link'] = build_url(request, data["short_link"])
            return Response(data, status=status.HTTP_201_CREATED)
        except Shorterlink.DoesNotExist:
            # Esto es interesante. Normalmente retornaríamos el super()... pero ahora, antes de retornarlo, modificamos un campo
            response = super().create(request, *args, **kwargs)
            response.data["short_link"] = build_url(
                request, response.data["short_link"])
            return response
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        serializer.save()
shorter_link_create_apiview = ShorterlinkCreateAPIView.as_view()

@method_decorator(csrf_exempt, name='dispatch')
class ShorterlinkListAPIView(generics.ListAPIView,):
    print("I am being called")
    queryset = Shorterlink.objects.all()
    serializer_class = ShortlinkSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        if not request.user.is_staff:
            return qs.filter(user=request.user)
        else:
            return qs


class ShorterlinkDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    lookup_field = "short_link"
    queryset = Shorterlink.objects.all()
    serializer_class = ShortlinkSerializer


class ShorterlinkUpdateView(generics.UpdateAPIView):
    lookup_field = "short_link"
    queryset = Shorterlink.objects.all()
    serializer_class = ShortlinkSerializer
    permission_classes = [IsAdminOrOwner]


class ShorterlinkDeleteView(generics.DestroyAPIView):
    lookup_field = "short_link"
    queryset = Shorterlink.objects.all()
    permission_classes = [IsAdminOrOwner]
