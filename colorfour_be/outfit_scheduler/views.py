from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import OutfitSchedule, UserPreferences, EventLogs
from .serializers import OutfitScheduleSerializer, EventLogsSerializer

class OutfitScheduleViewSet(viewsets.ModelViewSet):
  queryset = OutfitSchedule.objects.all()
  serializer_class = OutfitScheduleSerializer

  @action(detail=False, methods=['post'])
  def add_event(self, request):
    """新增活動"""
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"status": "event added", "event": serializer.data})
    return Response(serializer.errors, status=400)

  @action(detail=False, methods=['get'])
  def calendar(self, request):
    """顯示行事曆"""
    # 這裡假設是根據使用者或其他條件顯示行事曆，可以根據需求調整
    events = self.get_queryset()  # 這裡可以進行過濾或排序
    serializer = self.get_serializer(events, many=True)
    return Response(serializer.data)

class EventLogsViewSet(viewsets.ModelViewSet):
  queryset = EventLogs.objects.all()
  serializer_class = EventLogsSerializer

  
