from django.shortcuts import render
from rest_framework import viewsets
from .models import Quote
from .serializer import QuoteSerializer

# Create your views here.


class QuoteViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
