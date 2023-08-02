# Import necessary libraries and modules
import requests
from django.db import models
from rest_framework import serializers

# Define the Movie model with fields for title, actors, and rating
class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField('Actor')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    # String representation of the Movie model
    def __str__(self):
        return self.title

# Define the Actor model with a field for name
class Actor(models.Model):
    name = models.CharField(max_length=100)
    
    # String representation of the Actor model
    def __str__(self):
        return self.name

# Define a serializer for the Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'actors', 'rating')

# Define a class for the movie recommender system
class Recommender:
    def __init__(self):
        self.movies = []  # list to store movies
        self.url = 'https://api.example.com/movies/'  # API URL to fetch movies from

    def fetch_movies(self):
        """Fetch list of movies from API"""
        response = requests.get(self.url)
        self.movies = response.json()

    def recommend(self, user_profile):
        """Recommend movies based on user profile"""
        recommendations = []
        for movie in self.movies:
            if movie.rating >= 4 and 'Sci-Fi' in movie.actors:  # If movie rating is 4 or higher and genre is 'Sci-Fi'
                recommendations.append(movie)
        
        return recommendations  # Return list of recommended movies
