from django import template
from extra.models import Comment, LikeComment

register = template.Library()


@register.simple_tag
def like_color(comment_id, user):
    comment_obj = Comment.objects.get(id=comment_id)
    obj_list = comment_obj.likecomment.all()
    if obj_list.filter(like=True, user__id=user.id).exists():
        return True