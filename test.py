import os, sys, django
from django.contrib.auth.hashers import make_password

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.post.models import Post, Comment
from apps.member.models import Member


# m1 = Member.objects.create(email="diqkqkqk@gmail.com",
# password=make_password('0000'))
# m1.save()

member = Member.objects.get(pk=1)
print(member)

p = Post.objects.create(title="put 생성 시 DRF에서 바꾸려면 모든 데이터를 입력해야 바꿀 수 있다.",
    author=member,
    )
p.save()

# c = Comment.objects.create(author=member, post=post,
# body="사용자 쿼리셋 적용한 다음에 filter_backends 적용하는 메서드에요")
# c.save()

# member = Member.objects.get(pk=1)
# post = Post.objects.get(pk=1)

