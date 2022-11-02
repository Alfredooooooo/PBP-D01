from django.test import TestCase, Client
from django.urls import resolve
from event.models import Event
from model_bakery import baker
from django.contrib.auth.models import User

class ForumAppTest(TestCase):
    def login(self):
        self.username = 'vados'
        self.password = 'amogus123'
        user = User.objects.create_user(username=self.username)
        user.set_password(self.password)
        user.save()
        client = Client()
        client.login(username=self.username, password=self.password)
        self.user = user
        self.client = client

    def setUp(self):
        self.login()
        event = baker.make(Event, user=self.user)
        event.save()

    def test_forum(self):
        response = self.client.get('/forum/1/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/forum/json/1/')
        self.assertEqual(response.status_code, 200)
        
        data = {
            'comment_text': 'uwu',
        }
        response = self.client.post('/forum/add/1/0/', data)
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/forum/add/1/1/', data)
        self.assertEqual(response.status_code, 201)

        self.client.get('/forum/add/1/0/', data)
        
        response = self.client.post('/forum/delete/1/')
        self.assertEqual(response.status_code, 200)

        self.client.get('/forum/delete/1/')