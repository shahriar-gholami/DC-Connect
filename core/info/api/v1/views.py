from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from ...models import *
from rest_framework import mixins, generics
from .serializers import RouteSerializer

class CreateNewLinkAPIView(APIView):
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            input = dict(validated_data)
            src_row, created = Row.objects.get_or_create(
                title = input['src_row']
            )
            if 'OR' in input['src_rack']:
                type, create = RackType.objects.get_or_create(title='open_rack')
            else:
                type , create = RackType.objects.get_or_create(title='normal_rack')
            src_rack, create = Rack.objects.get_or_create(
                name = input['src_rack'],
                type = type,
                row = src_row,
            )
            device_type, created = DeviceType.objects.get_or_create(title='PP')
            src_pp , crrated = Device.objects.get_or_create(
                name = input['src_pp'],
                device_type = device_type,
                rack = src_rack
            )
            dst_row, created = Row.objects.get_or_create(
                title = input['dst_row']
            )
            if 'OR' in input['dst_rack']:
                type, create = RackType.objects.get_or_create(title='open_rack')
            else:
                type, create = RackType.objects.get_or_create(title= 'normal_rack')
            dst_rack, create = Rack.objects.get_or_create(
                name = input['dst_rack'],
                type = type,
                row = dst_row,
            )
            dst_pp , crrated = Device.objects.get_or_create(
                name = input['dst_pp'],
                device_type = device_type,
                rack = dst_rack
            )

            pp1 = src_pp
            pp2 = dst_pp
            

            for j in range(0,min(len(pp2.get_interfaces()),len(pp1.get_interfaces()))):
                new_link = Link.objects.create()
                new_link.terminals.add(pp1.get_interfaces()[j])
                new_link.terminals.add(pp2.get_interfaces()[j])
                new_link.save()

            
            print(f"پورت‌های پچ پنل‌های انتخاب شده نظیر به نظیر متصل شدند.")
                        

            return Response({"message": "اطلاعات با موفقیت دریافت شد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteCreateAPIView(mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
                                                                                                                                                                                                                        








