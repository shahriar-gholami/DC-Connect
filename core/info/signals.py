from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Link, Path

@receiver(pre_delete, sender=Link)
def handle_link_deletion(sender, instance, **kwargs):
    print('Deleting Link:', instance)

    paths = Path.objects.filter(links=instance)

    for path in paths:
        ordered_links = list(path.links.order_by('path_position'))

        index = ordered_links.index(instance)

        if index == 0:
            for i in range(1, len(ordered_links)):
                l = ordered_links[i]
                l.path_position -= 1
                l.save()

            path.links.remove(instance)

        elif index == len(ordered_links) - 1:
            path.links.remove(instance)

        else:
            before_links = ordered_links[:index]
            after_links = ordered_links[index+1:]

            path.links.set(before_links)
            for idx, link in enumerate(before_links):
                link.path_position = idx + 1
                link.save()

            if after_links:
                new_path = Path.objects.create()
                for idx, link in enumerate(after_links):
                    link.path_position = idx + 1
                    link.save()
                    new_path.links.add(link)
