from .models import Category
from .models import Post
import math

# 좌측에 출력될 category와 우측에 출력될 category를 분리
def category(request):
    category_all_list = list(Category.objects.all())
    cnt = Category.objects.count()
    category_left = []
    category_right = []
    half = math.trunc(Category.objects.count()/2)
    # print('half값은 {}'.format(half))
    for i in range(half):
        # print('좌측 단계 i값은 {}'.format(i))
        category_left.append(category_all_list[i])
        category_left[i].cnt = Post.objects.filter(category=category_all_list[i]).count()
    for i in range(half, cnt):
        # print('우측 단계 i값은 {}'.format(i))
        category_right.append(category_all_list[i])
        category_right[i-half].cnt = Post.objects.filter(category=category_all_list[i]).count()
    return {
        'category_left':category_left,
        'category_right' : category_right,
        'post_without_category': Post.objects.filter(category=None).count()
    }