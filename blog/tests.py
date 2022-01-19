from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.text

        self.assertEqual(title, 'BLOG')

        navbar = soup.find('div', id='navbar')
        self.assertIn('Blog', navbar.text)
        self.assertIn('About me', navbar.text)

        self.assertEqual(Post.objects.count(), 0)
        print(Post.objects.count(),'개입니다')
        self.assertIn('아직 게시물이 없습니다', soup.body.text)
        user = User.objects.create(username='admin', password='123')
        post = Post.objects.create(
            title='TEST_title',
            content = '본문',
            created = timezone.now(),
            author =user
        )
        # 0보다 크다
        self.assertGreater(Post.objects.count(), 0)
        print('이젠', Post.objects.count(), '개입니다')
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        body = soup.body
        title = soup.title.text
        # self.assertIn('아직 게시물이 없습니다', body.text)
        self.assertIn(post.title, body.text)

    def test_post_detail(self):
        self.assertEqual(Post.objects.count(), 0)

