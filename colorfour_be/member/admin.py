from django.contrib import admin
from .models import User, Role, SubscriptionPlan, UserPreferences, UserInteractionHistory

class UserAdmin(admin.ModelAdmin):
	list_display = ("email", "username", "role", "subscription_plan", "date_joined", "last_login", "is_active")
	search_fields = ("email", "username")
	list_filter = ("role", "subscription_plan", "is_active")
	ordering = ("-date_joined",)


class RoleAdmin(admin.ModelAdmin):
	list_display = ("role_name", "description")
	search_fields = ("role_name",)


class SubscriptionPlanAdmin(admin.ModelAdmin):
	list_display = ("plan_name", "price", "features")
	search_fields = ("plan_name",)
	list_filter = ("price",)


class UserPreferencesAdmin(admin.ModelAdmin):
	list_display = ("user", "preferred_language",	"theme", "notification_linebot", "preferred_outfit_recommendation")
	search_fields = ("user__email", "preferred_language")
	list_filter = ("theme", "notification_linebot")


class UserInteractionHistoryAdmin(admin.ModelAdmin):
	list_display = ("user", "actions", "target_id", "target_type", "timestamp")
	search_fields = ("user__email", "actions", "target_type")
	list_filter = ("actions", "target_type", "timestamp")


admin.site.register((User, Role, SubscriptionPlan, UserPreferences,	UserInteractionHistory))