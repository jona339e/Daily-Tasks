from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import extend_schema
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['due_date', 'priority', 'is_completed']
    ordering_fields = ['due_date', 'start_time', 'created_at']
    ordering = ['due_date', 'start_time']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Task.objects.none()
        return Task.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = TaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save(user=request.user)
        
        return Response({
            'success': True,
            'data': {
                'task': TaskSerializer(task).data
            },
            'message': 'Task created successfully'
        }, status=status.HTTP_201_CREATED)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Task.objects.none()
        return Task.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({
            'success': True,
            'data': {
                'task': serializer.data
            },
            'message': 'Task updated successfully'
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'message': 'Task deleted successfully'
        }, status=status.HTTP_200_OK)

class TaskCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(
        request=None,
        responses={200: TaskSerializer}
    )
    def patch(self, request, pk):
        try:
            task = Task.objects.get(id=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({
                'success': False,
                'error': 'Task not found'
            }, status=status.HTTP_404_NOT_FOUND)

        is_completed = request.data.get('is_completed')
        if is_completed is None:
            return Response({
                'success': False,
                'error': 'is_completed field is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        task.is_completed = is_completed
        if is_completed:
            task.completed_at = timezone.now()
        else:
            task.completed_at = None
        task.save()

        return Response({
            'success': True,
            'data': {
                'task': TaskSerializer(task).data
            },
            'message': 'Task completion status updated'
        })