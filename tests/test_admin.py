from django.test import TestCase
from django.contrib.admin import site

from sample.models import Continent, City, Geo
from sample.admin import ContinentAdmin, CityAdmin, GeoAdmin


class MockRequest:
    pass


class MockSuperUser:
    def has_perm(self, perm):
        return True


request = MockRequest()
request.user = MockSuperUser()


class TranslatableAdminMixinTest(TestCase):
    """Tests for `TranslatableAdminMixin`."""

    def test_handle_translation_inlines_none(self):
        admin = CityAdmin(City, site)
        inlines = admin.get_inline_instances(request, obj=None)
        self.assertListEqual(
            inlines[0].form.base_fields['field'].choices,
            [(None, '---------'), ('name', 'name'), ('denonym', 'denonym')]
        )

    def test_handle_translation_inlines_empty(self):
        admin = GeoAdmin(Geo, site)
        inlines = admin.get_inline_instances(request, obj=None)
        self.assertListEqual(
            inlines,
            []
        )

    def test_handle_translation_inlines_explicit(self):
        admin = ContinentAdmin(Continent, site)
        inlines = admin.get_inline_instances(request, obj=None)
        self.assertEqual(
            inlines[0].form.base_fields['field'].choices,
            [(None, '---------'), ('name', 'name'), ('denonym', 'denonym')]
        )
