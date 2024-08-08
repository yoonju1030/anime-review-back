from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, id, password, **kwargs):
        if not id:
            raise ValueError('Users must have an id')
        user = self.model(
            id=id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, id, password=None):
        user = self.create_user(
            id,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=30, unique=True, null=False, blank=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

	# 헬퍼 클래스 사용
    objects = UserManager()

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)

	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'id'
    # REQUIRED_FIELDS = ['id']

    def __str__(self):
        return self.id