from django.shortcuts import render  # Default
from django.http import HttpResponse, JsonResponse  # Tut 1, Step 3
from django.views.decorators.csrf import csrf_exempt  # Tut 1, Step 3
from rest_framework.parsers import JSONParser  # Tut 1, Step 3
from rest_framework import status  # Tut 2, Step 1
from rest_framework.decorators import api_view  # Tut 2, Step 1
from rest_framework.response import Response  # Tut 2, Step 1
from snippets.models import Snippet  # Tut 1, Step 3
from snippets.serializers import SnippetSerializer  # Tut 1, Step 3
from django.http import Http404  # Tut 3, Step 1
from rest_framework.views import APIView  # Tut 3, Step 1
from rest_framework import mixins  # Tut 3, Step 2
from rest_framework import generics  # Tut 3, Step 2
from snippets.serializers import UserSerializer  # Tut 4, Step 2
from django.contrib.auth.models import User  # Tut 4, Step 2
from rest_framework import permissions  # Tut 4, Step 5
from snippets.permissions import IsOwnerOrReadOnly  # Tut 4, Step 7

# -------------------MODEL VIEW!!!-------------------
# Tut 1, Step 3
# @csrf_exempt  # tut 1, step 3
# @api_view(['GET', 'POST'])  # Tut 2, Step 1
# def snippet_list(request, format=None):  # Tut 2, Step 2 (format=None)
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()  # Tut 1, Step 3
#         serializer = SnippetSerializer(snippets, many=True)  # Tut 1, Step 3
#         # return JsonResponse(serializer.data, safe=False)  # Tut 1, Step 3
#         return Response(serializer.data)  # Tut 2, Step 1

#     elif request.method == 'POST':
#         # data = JSONParser().parse(request) # Tut 1, Step 3
#         # serializer = SnippetSerializer(data=data)  # Tut 1, Step 3
#         serializer = SnippetSerializer(data=request.data)  # Tut 2, Step 1
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data, status=201)# Tut 1, Step 3
#             # Tut 2, Step 1
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.errors, status=400)# Tut 1, Step 3
#         # Tut 2, Step 1
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Tut 1, Step 3
# # @csrf_exempt  # tut 1, step 3
# @api_view(['GET', 'PUT', 'DELETE'])  # Tut 2, Step 1
# def snippet_detail(request, pk, format=None):  # Tut 2, Step 2 (format=None)
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         # return HttpResponse(status=404)# Tut 1, Step 3
#         return Response(status=status.HTTP_404_NOT_FOUND)  # Tut 2, Step 1

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         # return JsonResponse(serializer.data)# Tut 1, Step 3
#         return Response(serializer.data)  # Tut 2, Step 1

#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)  # Tut 1, Step 3
#         # serializer = SnippetSerializer(snippet, data=data)  # Tut 1, Step 3
#         serializer = SnippetSerializer(
#             snippet, data=request.data)  # Tut 2, Step 1
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data)  # Tut 1, Step 3
#             return Response(serializer.data)  # Tut 2, Step 1
#         # return JsonResponse(serializer.errors, status=400) # Tut 1, Step 3
#         # Tut 2, Step 1
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         # return HttpResponse(status=204)  # Tut 1, Step 3
#         return Response(status=status.HTTP_204_NO_CONTENT)  # Tut 2, Step 1


# ---------------------CLASS VIEW!!!-------------------------
# Tut 3, Step 1
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------CLASS VIEW!!! (USING MIXINS)-------------------------
# Tut 3, Step 2
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# ---------------------CLASS VIEW!!! (USING GENERIC CLASS-BASED VIEWS)-------------------------
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]  # Tut 4, Step 5

    def perform_create(self, serializer):  # Tut 4, Step 3
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Tut 4, Step 5
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]  # Tut 4, Step 7


# Auth & Perm -------------------------------


# Tut 4, Step 2
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Tut 4, Step 2
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
