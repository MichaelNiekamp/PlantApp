from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Plant, Event

class PlantyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", age="21", current_plants="21", rank="5", password="secret")
        cls.plant = Plant.objects.create(
            name="Phil", type="pepper", description="First born pepper plant", date_planted="2022-12-02", author=cls.user,)   
        cls.event = Event.objects.create(
            plant_id=cls.plant, event_title="test event", height="3", date="2022-12-02")
        
    def test_plant_model(self):
        self.assertEqual(self.plant.author.username, "testuser")
        self.assertEqual(self.plant.name, "Phil")
        self.assertEqual(self.plant.type, "pepper")
        self.assertEqual(self.plant.description, "First born pepper plant")
        self.assertEqual(self.plant.date_planted, "2022-12-02")        
        self.assertEqual(str(self.plant), "Phil")
        self.assertEqual(self.plant.get_absolute_url(), "/planty/1/")

    def test_event_model(self):
        self.assertEqual(self.event.event_title, "test event")
        self.assertEqual(self.event.height, "3")
        self.assertEqual(str(self.event), "Phil")
        self.assertEqual(self.event.get_absolute_url(), "/planty/event/1/")

    def test_url_exists_at_correct_location_plant_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_plant_detailview(self):
        response = self.client.get("/planty/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_plant_createview(self):
        response = self.client.get("/planty/new/") 
        self.assertEqual(response.status_code, 200)   

    def test_url_exists_at_correct_location_event_detailview(self):
        response = self.client.get("/planty/event/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_event_createview(self):
        response = self.client.get("/planty/event/new/") 
        self.assertEqual(response.status_code, 200) 

    def test_plant_detailview(self):
        response = self.client.get(reverse("plant_detail",kwargs={"pk":self.plant.pk}))
        no_response = self.client.get("/planty/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Phil")
        self.assertTemplateUsed(response, "plant_detail.html")

    def test_plant_createview(self):
        response = self.client.post(reverse("plant_new"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertTemplateUsed(response, "plant_new.html")

    def test_plant_updateview(self):
        response = self.client.post(reverse("plant_edit", kwargs={"pk":self.plant.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertTemplateUsed(response, "plant_edit.html")

    def test_plant_deleteview(self):
        response = self.client.post(reverse("plant_delete", args="1"))
        self.assertEqual(response.status_code, 302)
        
    def test_event_detailview(self):
        response = self.client.get(reverse("event_detail",kwargs={"pk":self.event.pk}))
        no_response = self.client.get("/planty/event/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test event")
        self.assertTemplateUsed(response, "event_detail.html")
    
    def test_event_createview(self):
        response = self.client.post(reverse("event_new"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertTemplateUsed(response, "event_new.html")

    def test_event_updateview(self):
        response = self.client.post(reverse("event_edit", kwargs={"pk":self.plant.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertTemplateUsed(response, "event_edit.html")

    def test_event_deleteview(self):
        response = self.client.post(reverse("event_delete", args="1"))
        self.assertEqual(response.status_code, 302)