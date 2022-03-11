from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.

def append_member_to_vector_node(request):
    member = request.GET.get('number')
    if not member:
        return JsonResponse({'success' : False, 'message': 'Provide a member'})


