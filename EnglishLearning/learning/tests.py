from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Lesson, BookmarkedLesson

class AuthenticationTests(TestCase):
    def test_user_registration(self):
        response = self.client.post('/signup/', {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_valid_user(self):
        User.objects.create_user(username='testuser', password='TestPass123!')
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'TestPass123!'})
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_login_invalid_user(self):
        response = self.client.post('/login/', {'username': 'wronguser', 'password': 'WrongPass!'})
        self.assertContains(response, "Invalid credentials")


class RBACTests(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(username="student", password="TestPass123!")
        self.creator = User.objects.create_user(username="creator", password="TestPass123!")

        student_group, _ = Group.objects.get_or_create(name='Students')
        creator_group, _ = Group.objects.get_or_create(name='Content Creators')

        self.student.groups.add(student_group)
        self.creator.groups.add(creator_group)

    def test_student_access_creator_dashboard(self):
        self.client.login(username="student", password="TestPass123!")
        response = self.client.get('/dashboard/creator/')
        self.assertEqual(response.status_code, 302)  # Should redirect to student dashboard

    def test_creator_access_student_dashboard(self):
        self.client.login(username="creator", password="TestPass123!")
        response = self.client.get('/dashboard/student/')
        self.assertEqual(response.status_code, 302)  # Should redirect to creator dashboard


class LessonTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="creator", password="TestPass123!")
        self.client.login(username="creator", password="TestPass123!")
        self.lesson = Lesson.objects.create(title="Test Lesson", preview="Short preview", content="Lesson content", created_by=self.user)

    def test_create_lesson(self):
        response = self.client.post('/dashboard/creator/lesson/create/', {
            'title': 'New Lesson',
            'preview': 'Preview text',
            'content': 'Lesson content',
            'created_by': self.user.id
        })
        self.assertEqual(Lesson.objects.count(), 2)

    def test_edit_lesson(self):
        response = self.client.post(f'/dashboard/creator/lesson/edit/{self.lesson.id}/', {
            'title': 'Updated Lesson',
            'preview': 'Updated preview',
            'content': 'Updated content'
        })
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, "Updated Lesson")

    def test_delete_lesson(self):
        response = self.client.post(f'/dashboard/creator/lesson/delete/{self.lesson.id}/')
        self.assertEqual(Lesson.objects.count(), 0)


class BookmarkTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="student", password="TestPass123!")
        self.client.login(username="student", password="TestPass123!")
        self.lesson = Lesson.objects.create(title="Test Lesson", preview="Short preview", content="Lesson content", created_by=self.user)

    def test_bookmark_lesson(self):
        response = self.client.post(f'/lesson/{self.lesson.id}/bookmark/')
        self.assertTrue(BookmarkedLesson.objects.filter(user=self.user, lesson=self.lesson).exists())

    def test_remove_bookmark(self):
        BookmarkedLesson.objects.create(user=self.user, lesson=self.lesson)
        response = self.client.post(f'/lesson/{self.lesson.id}/bookmark/')
        self.assertFalse(BookmarkedLesson.objects.filter(user=self.user, lesson=self.lesson).exists())


class SearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="student", password="TestPass123!")
        self.client.login(username="student", password="TestPass123!")
        self.lesson1 = Lesson.objects.create(title="Python Basics", preview="Intro to Python", content="Content", created_by=self.user)
        self.lesson2 = Lesson.objects.create(title="Advanced Python", preview="Deep dive", content="Content", created_by=self.user)

    def test_search_lesson(self):
        response = self.client.get('/lesson_search/?q=Python')
        self.assertContains(response, "Python Basics")
        self.assertContains(response, "Advanced Python")

    def test_filter_by_tag(self):
        response = self.client.get('/lesson_search/?tags=1')  # Assuming tag ID is 1
        self.assertContains(response, "Python Basics")  # If tagged correctly

