from django.contrib import admin

from .models import Post, Likes


class PostAdmin(admin.ModelAdmin):
    
    def like_count(self, obj):
        return Likes.objects.filter(liked_post=obj).count()

    like_count.short_description = 'Count of likes'

    model = Post
    list_display = ('id', 'pub_date', 'author', 'like_count',)
    list_filter = ('pub_date',)
    readonly_fields = ('like_count', )


class LikeAdmin(admin.ModelAdmin):
    model = Likes
    list_display = ('who_like_it', 'like_time', 'liked_post_id',)
    fields = ('who_like_it', 'like_time', 'liked_post',)
    list_filter = ('like_time',)


admin.site.register(Post, PostAdmin)
admin.site.register(Likes, LikeAdmin)
