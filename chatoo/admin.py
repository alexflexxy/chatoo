from django.contrib import admin
from django.contrib.auth.models import User
from .models import Chat, Profile, Pictures

# Register your models here.

# Create stacked inline for Profile
class ProfileInline(admin.StackedInline):
    model = Profile

# create a user admin based on the user model
class UserAdmin(admin.ModelAdmin): 
    model = User
    # Displayed fields
    fields = ["username", "email", "password"]
    # add ProfileInline as a member of inlines to your UserAdmin.
    inlines = [ProfileInline]

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user', 'created_at', 'body')

admin.site.unregister(User)
#admin.site.register(Chat)
admin.site.register(User, UserAdmin)
admin.site.register(Pictures)