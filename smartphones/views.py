from django.forms import model_to_dict
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Smartphone
from .permissions import AdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import SmartphoneSerializer
from .models import Category
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class SmartphoneAPIViewSet(ModelViewSet):
    # queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Smartphone.objects.all()[:3]

        return Smartphone.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        return Response({'cats': category.title})


class SmartphoneAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class SmartphoneAPIList(ListCreateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = SmartphoneAPIListPagination


class SmartphoneAPIUpdate(RetrieveUpdateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class SmartphoneAPIDestroy(RetrieveDestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    permission_classes = (AdminOrReadOnly,)


class SmartphoneAPIUpdate(UpdateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer


class SmartphoneAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer


class SmartphoneAPIView(APIView):
    # queryset = Smartphone.objects.all()
    # serializer_class = SmartphoneSerializer
    def get(self, request, *args, **kwargs):
        smartphones = Smartphone.objects.all()
        return Response({'posts': SmartphoneSerializer(smartphones, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer = SmartphoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Smartphone.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})

        serializer = SmartphoneSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
