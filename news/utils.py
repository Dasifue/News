from django.shortcuts import redirect, get_object_or_404
from .models import Tag
from accounts.models import User

def find_tags(tags: str|None) -> list[Tag]:
    if tags is None:
        return []
    
    if tags.isspace():
        return []
    
    tags = tags.split(" ")

    results = []

    for tag_ in tags:
        tag_objs = Tag.objects.filter(name__iexact=tag_)
        if not tag_objs:
            if tag_.islower():
                tag_ = tag_.title()
            tag = Tag.objects.create(name=tag_)
        else:
            tag = tag_objs.first()

        results.append(tag)
    return results


def is_owner(model):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            user: User = request.user
            pk = kwargs.get("pk")
            if pk is None:
                try:
                    pk = args[0]
                except IndexError:
                    return redirect(request.META.get("HTTP_REFERER", "/"))

            article = get_object_or_404(model, pk=pk)
            if article.owner == user:
                return func(request, *args, **kwargs)
            else:
                return redirect(request.META.get("HTTP_REFERER", "/"))
            
        return wrapper
    return decorator
