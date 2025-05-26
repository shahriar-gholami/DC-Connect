from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from collections import defaultdict

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

	def get_interfaces(self):
		return [int for int in Interface.objects.filter(device = self) if 'Core' not in int.name]

	def __str__(self) -> str:
		return f'{self.rack.row}-{self.rack.name}-{self.name}'

class Interface(models.Model):
	name = models.CharField(max_length=255)
	device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)

	def get_pathes(self):
		pathes = []
		for path in Path.objects.all():
			path_terminals = path.get_terminals()
			if self.id:
				if self in path_terminals:
					path.sort_links_by_path_order()
					pathes.append(path)
					break
		return pathes

	class Meta:
		verbose_name = 'EndPoint/Port'
		verbose_name_plural = 'Terminals/Ports'

	def __str__(self) -> str:
		if self.device != None:
			return f'{self.device}-{self.name}'
		return self.name

class Link(models.Model):
	terminals = models.ManyToManyField(Interface)
	path_position = models.IntegerField(default=1)

	class Meta:
		ordering = ['path_position']

	def __str__(self) -> str:
		return ' | '.join(str(terminal) for terminal in self.terminals.all())

@receiver(m2m_changed, sender=Link.terminals.through)
def handle_terminals_change(sender, instance, action, **kwargs):
	if action == 'post_add':
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
			new_path = Path.objects.create()
			new_path.links.add(instance)
		elif len(pathes) == 1:
			pathes[0].links.add(instance)
			pathes[0].sort_links_by_path_order()
		elif len(pathes) == 2:
			pathes[0].links.add(instance)
			for link in pathes[1].links.all():
				pathes[0].links.add(link)
				pathes[0].sort_links_by_path_order()
			pathes[1].delete()

class Path(models.Model):
	links = models.ManyToManyField(Link, blank=True)

	def get_devices(self):
		devices = set()
		path_terminals = set()
		for link in self.links.all():
			for terminal in link.terminals.all():
				path_terminals.add(terminal)
		for int in list(path_terminals):
			devices.add(int.device)
		return list(devices)

	def get_outer_device(self):
		endpoints = []
		for device in self.get_devices():
			if OuterEndPoint.objects.filter(device=device).first() != None:
				endpoints.append(f'{device}-{OuterEndPoint.objects.filter(device=device).first().name}')
		return endpoints

	def get_terminals(self):
		path_terminals = set()
		for link in self.links.all():
			for terminal in link.terminals.all():
				path_terminals.add(terminal)
		return path_terminals

	def sort_links_by_path_order(self):
		# Step 1: Build graph (link adjacency based on shared interfaces)
		link_to_interfaces = {}
		interface_to_links = defaultdict(list)

		for link in self.links.all():
			terminals = list(link.terminals.all())
			link_to_interfaces[link] = terminals
			for terminal in terminals:
				interface_to_links[terminal.id].append(link)

		# Step 2: Build adjacency list for links
		link_neighbors = defaultdict(set)
		for link, terminals in link_to_interfaces.items():
			for terminal in terminals:
				for neighbor_link in interface_to_links[terminal.id]:
					if neighbor_link != link:
						link_neighbors[link].add(neighbor_link)

		# Step 3: Find start link (has only one neighbor)
		start_link = None
		for link, neighbors in link_neighbors.items():
			if len(neighbors) == 1:
				start_link = link
				break

		visited = set()
		ordered_links = []
		current = start_link
		prev = None

		while current and current not in visited:
			ordered_links.append(current)
			visited.add(current)
			next_links = link_neighbors[current] - visited
			if prev in next_links:
				next_links.remove(prev)
			prev = current
			current = next_links.pop() if next_links else None

		# Step 5: Update path_position
		for index, link in enumerate(ordered_links, start=1):
			link.path_position = index
			link.save()

		return ordered_links  # Optional: return sorted links

	def __str__(self) -> str:
		if self.get_outer_device() != []:
			return f"{' || '.join(str(link) for link in self.links.all())} -->{self.get_outer_device()}"
		return f"{' || '.join(str(link) for link in self.links.all())}"
		
class OuterEndPoint(models.Model):
	name = models.CharField(max_length=250)
	device = models.ManyToManyField(Device,null=True, blank=True)

	def __str__(self) -> str:
		return self.name
