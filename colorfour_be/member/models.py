from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True)  # member, merchant, admin
    subscription_plan = models.ForeignKey("SubscriptionPlan", on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.username == "":
            self.username = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role_name


class SubscriptionPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return self.plan_name


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(max_length=20, default="zh-TW")
    theme = models.CharField(max_length=20, default="light")  # light, dark
    notification_linebot = models.BooleanField(default=True)
    preferred_outfit_recommendation = models.CharField(
        max_length=50, default="smart"
    )  # smart or preference

    def __str__(self):
        return f"Preferences of {self.user.email}"


class UserInteractionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    actions = models.CharField(max_length=50)  # post, like, comment, follow, unfollow
    target_id = models.IntegerField()
    target_type = models.CharField(max_length=50)  # post, comment, user, etc.
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.actions} on {self.target_type} - {self.timestamp}"


class UserAuthProvider(models.Model):
    """
    模型描述：記錄用戶與第三方提供者（如 Google、Line）之間的綁定關係
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="auth_providers"
    )
    provider = models.CharField(max_length=50)  # google, line
    provider_id = models.CharField(max_length=255, unique=True)  # 確保唯一性
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now)

    class Meta:
        # 設置 user 和 provider 的唯一約束，確保同一用戶不會重複綁定同一提供者
        constraints = [
            models.UniqueConstraint(
                fields=["user", "provider"], name="unique_user_provider"
            )
        ]
        verbose_name = "User Authentication Provider"
        verbose_name_plural = "User Authentication Providers"

    def __str__(self):
        return f"{self.provider.capitalize()} account of {self.user.email}"
