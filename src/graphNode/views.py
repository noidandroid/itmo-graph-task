from django.shortcuts import render

from django.http import JsonResponse
from . import models
from . import operationService as s


# Create your views here.


def create_graph(request):
    req = request.GET.get('Create graph')
    if not req:
        return JsonResponse({'success': False})
    connections = []
    models.Graph(connections)

    return JsonResponse({'success': True})


def summarize(request, graph: models.Graph,
              vector1: models.Vector,
              vector2: models.Vector, operation: models.Operation):
    req = request.GET.get('Provide Nodes')
    if not req:
        return JsonResponse({'success': False})

    graph.add(vector1, operation)
    graph.add(vector2, operation)
    graph.add(operation, s.sum(vector1, vector2))


def multiply(request, graph: models.Graph,
             vector1: models.Vector,
             vector2: models.Vector, operation: models.Operation):
    req = request.GET.get('Provide Nodes')
    if not req:
        return JsonResponse({'success': False})

    graph.add(vector1, operation)
    graph.add(vector2, operation)
    graph.add(operation, s.sum(vector1, vector2))


def length(request, graph: models.Graph,
           vector1: models.Vector,
           vector2: models.Vector, operation: models.Operation):
    req = request.GET.get('Provide Nodes')
    if not req:
        return JsonResponse({'success': False})

    graph.add(vector1, operation)
    graph.add(vector2, operation)
    graph.add(operation, s.len(vector1, vector2))
