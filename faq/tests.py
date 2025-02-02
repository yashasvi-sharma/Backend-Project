import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FAQ
from django.core.cache import cache
from unittest.mock import patch
from django.core.management import call_command
from io import StringIO

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def faq_instance(db):
    return FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )

@pytest.mark.django_db
def test_faq_list(api_client, faq_instance):
    url = reverse('faq-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['question'] == faq_instance.question

@pytest.mark.django_db
def test_faq_detail(api_client, faq_instance):
    url = reverse('faq-detail', kwargs={'pk': faq_instance.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['question'] == faq_instance.question

@pytest.mark.django_db
@patch('google.cloud.translate_v2.Client.translate')
def test_faq_translation(mock_translate, api_client, faq_instance):
    mock_translate.return_value = {'translatedText': 'Django क्या है?'}
    url = reverse('faq-detail', kwargs={'pk': faq_instance.pk})
    response = api_client.get(f"{url}?lang=hi")
    assert response.status_code == status.HTTP_200_OK
    assert response.data['question'] == 'Django क्या है?'

@pytest.mark.django_db
def test_faq_caching(faq_instance):
    cache.clear()
    translated = faq_instance.get_translated_question('hi')
    assert translated != faq_instance.question
    cached = faq_instance.get_translated_question('hi')
    assert cached == translated

@pytest.mark.django_db
def test_faq_model_str(faq_instance):
    assert str(faq_instance) == faq_instance.question

@pytest.mark.django_db
def test_faq_creation(db):
    faq = FAQ.objects.create(
        question="What is Python?",
        answer="Python is a high-level programming language."
    )
    assert FAQ.objects.count() == 1
    assert faq.question == "What is Python?"

@pytest.mark.django_db
def test_pretranslate_faqs_command(faq_instance):
    out = StringIO()
    call_command('pretranslate_faqs', stdout=out)
    assert 'Successfully pre-translated FAQ:' in out.getvalue()
    assert 'All FAQs have been pre-translated' in out.getvalue()

