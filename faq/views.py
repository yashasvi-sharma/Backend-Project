from rest_framework import viewsets
from django.views.generic import ListView
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQListView(ListView):
    model = FAQ
    template_name = 'faq/faq_list.html'
    context_object_name = 'faqs'

