from django.shortcuts import render
from .model import Position


def render_positions(request, asset):
    positions = Position.objects.filter(asset=asset)
    context = {"asset": asset, "positions": positions}
    return render(request, "positions.html", context)
