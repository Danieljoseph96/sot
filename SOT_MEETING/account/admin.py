from django.contrib import admin

from .models import LocalityWise, UserProfile, UserReg


@admin.register(UserReg)
class UserRegAdmin(admin.ModelAdmin):
	list_display = ("sl_no", "name", "locality", "state", "received_amount", "total_amount", "balance_amount")
	search_fields = ("name", "locality", "state", "language", "bus_no")
	list_filter = ("state", "locality", "language")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "user_type")


@admin.register(LocalityWise)
class LocalityWiseAdmin(admin.ModelAdmin):
	list_display = ("locality", "state", "persons_count", "total_paid", "total_balance", "payment_method", "updated_at")
	search_fields = ("locality", "state", "language")
	list_filter = ("state", "payment_method")

