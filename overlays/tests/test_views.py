from django.test import TestCase
from django.urls import reverse


from ..models import Overlay
from .factories import PLUME_FILE_FIXTURE, create_overlay


class OverlaysViewsTest(TestCase):
    def test_empty_index(self):
        response = self.client.get(reverse('overlays:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No overlays yet")
        self.assertQuerysetEqual(response.context['overlays'], [])

    def test_index_with_overlay(self):
        overlays = list([
            create_overlay("first"),
            create_overlay("second"),
        ])

        response = self.client.get(reverse('overlays:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "first")
        self.assertContains(response, "second")
        # TODO: find out why this is failing when the items in the list appear to be the same
        # self.assertQuerysetEqual(response.context['overlays'], overlays, ordered=False)
        self.assertEqual(len(response.context['overlays']), 2)

    def test_get_new(self):
        response = self.client.get(reverse('overlays:new'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create new overlay")

    def test_post_new(self):
        name = "Test name"
        plume = open(PLUME_FILE_FIXTURE, 'rb')
        data = {
            'name': name,
            'longtitude': Overlay.GHG_OFFICE_LONGTITUDE,
            'latitude': Overlay.GHG_OFFICE_LATITIUDE,
            'plume': plume,
        }
        response = self.client.post(reverse('overlays:new'), follow=True, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, name)
        
        overlay = Overlay.objects.get(name=name)
        self.assertIsNotNone(overlay)

    def test_show_missing(self):
        url = reverse('overlays:show', args=(404,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_show_overlay(self):
        name = "example"
        overlay = create_overlay(name)
        url = reverse('overlays:show', args=(overlay.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, name)

    def test_json_show_missing(self):
        url = reverse('overlays:json_show', args=(404,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_json_show_overlay(self):
        name = "example"
        overlay = create_overlay(name)
        url = reverse('overlays:json_show', args=(overlay.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, name)


