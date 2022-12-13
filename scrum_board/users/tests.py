from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import CustomUser


class CustomUserTests(TestCase):
    """Test custom user model."""
    def tearDown(self):
        CustomUser.objects.all().delete()
        super().tearDown()

    def test_create_user(self):
        users_count = CustomUser.objects.count()

        test_user = CustomUser(
            username='test',
            password='123',
            email='test@test.ru',
            status='DEVELOPER',
        )
        test_user.full_clean()
        test_user.save()

        self.assertEqual(CustomUser.objects.count(), users_count + 1)

    def test_unique_username(self):
        users_count = CustomUser.objects.count()

        test_user = CustomUser(
            username='test',
            password='123',
            email='test@test.ru',
            status='DEVELOPER',
        )
        test_user.full_clean()
        test_user.save()

        with self.assertRaises(ValidationError):
            test_user_2 = CustomUser(
                username='test',
                password='123',
                email='test_2@test.ru',
                status='DEVELOPER',
            )
            test_user_2.full_clean()
            test_user_2.save()

        self.assertEqual(CustomUser.objects.count(), users_count + 1)

    def test_unique_email(self):
        users_count = CustomUser.objects.count()

        test_user = CustomUser(
            username='test',
            password='123',
            email='test@test.ru',
            status='DEVELOPER',
        )
        test_user.full_clean()
        test_user.save()

        with self.assertRaises(ValidationError):
            test_user_2 = CustomUser(
                username='test_2',
                password='123',
                email='test@test.ru',
                status='DEVELOPER',
            )
            test_user_2.full_clean()
            test_user_2.save()

        self.assertEqual(CustomUser.objects.count(), users_count + 1)
