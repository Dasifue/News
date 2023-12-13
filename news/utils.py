from .models import Tag

def find_tags(tags: str) -> list[Tag]:
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
