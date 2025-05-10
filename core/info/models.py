from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# Create your models here.

class Row(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class RackType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Rack(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(RackType, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.row}-{self.name}'

class DeviceType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Device(models.Model):
    name = models.CharField(max_length=255)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    series = models.CharField(max_length=255, null=True, blank=True)
    rack = models.ForeignKey(Rack, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.rack.row}-{self.rack.name}-{self.device_type}-{self.name}'

class Interface(models.Model):
    name = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def get_pathes(self):
        pathes = []
        for path in Path.objects.all():
            path_terminals = path.get_terminals()
            if self in path_terminals:
                pathes.append(path)

        return pathes


    def __str__(self) -> str:
        return f'{self.device}-{self.name}'

class Link(models.Model):
    terminals = models.ManyToManyField(Interface)
    path_position = models.IntegerField(default=1)

    def __str__(self) -> str:
        return ' | '.join(str(terminal) for terminal in self.terminals.all())

@receiver(m2m_changed, sender=Link.terminals.through)
def handle_terminals_change(sender, instance, action, **kwargs):
    if action == 'post_add':
        # فقط وقتی ترمینال‌ها اضافه شدن
        pathes = []
        for path in Path.objects.all():
            path_terminals = path.get_terminals()
            for terminal in instance.terminals.all():
                if terminal in path_terminals:
                    pathes.append(path)
                    break
            if len(pathes) == 2:
                break

        if len(pathes) == 0:
            print('00000000000000000000000000000000000000')
            new_path = Path.objects.create()
            new_path.links.add(instance)
        elif len(pathes) == 1:
            print('111111111111111111111111111111111')
            pathes[0].links.add(instance)
        elif len(pathes) == 2:
            print('22222222222222222222222222222222')
            for link in pathes[1].links.all():
                pathes[0].links.add(link)
            pathes[1].delete()




class Path(models.Model):
    links = models.ManyToManyField(Link, blank=True)

    def get_terminals(self):
        path_terminals = set()
        for link in self.links.all():
            for terminal in link.terminals.all():
                path_terminals.add(terminal)
        return path_terminals

    def __str__(self) -> str:

        return ' || '.join(str(link) for link in self.links.all())

