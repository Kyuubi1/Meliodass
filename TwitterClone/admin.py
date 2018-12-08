from django.contrib import admin
from  .models import Account, Post, Comment,Like
# Register your models here.


class Admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'sex', 'address', 'phone',  'is_active', 'is_staff', )


admin.site.register(Account, Admin)

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Like)