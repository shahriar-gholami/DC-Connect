from django.db import models

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
        return f'{self.row}-{self.type}-{self.name}'

class DeviceType(models.Model):
    title = models.CharField

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

    def __str__(self) -> str:
        return f'{self.device}-{self.name}'

class Link(models.Model):
    terminals = models.ManyToManyField(Interface)
    path_position = models.IntegerField(default=1)

    def save(self, *args, **kwargs):

        from .models import Path  # جلوگیری از ImportError چرخشی
        selected_path = None
        
        for path in Path.objects.all():

            if path.get_end_interface() == self.source_int:
                path.links.add(self)
                print(f'به انتهای مسیر {path.id} اضافه شد')
                selected_path = path


class Path(models.Model):
    links = models.ManyToManyField(Link, blank=True)

    def get_start_interface(self):
        if not self.links.exists():
            return None
        first_link = self.links.first()
        path_terminals = []
        return first_link.source_int

    def get_end_interface(self):
        if not self.links.exists():
            return None
        last_link = self.links.last()
        return last_link.destination_int

    def can_append(self, link: Link):
        return self.get_end_interface() == link.source_int

    def can_prepend(self, link: Link):
        return self.get_start_interface() == link.destination_int

    

    
    


