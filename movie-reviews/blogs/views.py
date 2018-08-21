from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class MovieList(ListView):
    model = models.Post
    paginate_by=6


class MovieDetailView(DetailView):
    model = models.Post
