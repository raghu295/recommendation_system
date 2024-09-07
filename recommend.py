import math

# Step 1: Define a simple dataset of Hindi movies
movies = [
    {"title": "3 Idiots", "genres": ["Drama", "Comedy"]},
    {"title": "Dangal", "genres": ["Drama", "Biography", "Sport"]},
    {"title": "Chhichhore", "genres": ["Drama", "Comedy"]},
    {"title": "Sholay", "genres": ["Action", "Adventure", "Drama"]},
    {"title": "PK", "genres": ["Comedy", "Drama", "Fantasy"]},
    {"title": "Gully Boy", "genres": ["Drama", "Music"]},
    {"title": "Kabir Singh", "genres": ["Drama", "Romance"]},
    {"title": "Lagaan", "genres": ["Drama", "Sport", "Musical"]},
    {"title": "Zindagi Na Milegi Dobara", "genres": ["Adventure", "Comedy", "Drama"]},
    {"title": "Andhadhun", "genres": ["Crime", "Thriller", "Comedy"]}
]

# Step 2: Extract unique genres
unique_genres = set(genre for movie in movies for genre in movie["genres"])
genre_index = {genre: idx for idx, genre in enumerate(unique_genres)}

# Create a binary vector for each movie based on the genres
def create_genre_vector(movie, genre_index):
    genre_vector = [0] * len(genre_index)
    for genre in movie["genres"]:
        genre_vector[genre_index[genre]] = 1
    return genre_vector

for movie in movies:
    movie["genre_vector"] = create_genre_vector(movie, genre_index)

# Step 3: Cosine similarity function
def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    magnitude_vec1 = math.sqrt(sum(v1**2 for v1 in vec1))
    magnitude_vec2 = math.sqrt(sum(v2**2 for v2 in vec2))
    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0
    return dot_product / (magnitude_vec1 * magnitude_vec2)

# Calculate similarity between all movies
similarity_matrix = [[cosine_similarity(m1["genre_vector"], m2["genre_vector"]) for m2 in movies] for m1 in movies]

# Step 4: Recommendation function
def get_recommendations(title, movies, similarity_matrix):
    try:
        movie_index = next(i for i, movie in enumerate(movies) if movie["title"] == title)
    except StopIteration:
        return ["Movie not found in the dataset."]
    
    similarity_scores = similarity_matrix[movie_index]
    similar_movies = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)
    similar_movies = similar_movies[1:4]
    return [movies[i]["title"] for i, _ in similar_movies]

# User interaction: Ask the user for input
user_input = input("Enter a movie title to get recommendations: ")

# Provide recommendations based on user input
recommendations = get_recommendations(user_input, movies, similarity_matrix)
print(f"\nMovies similar to '{user_input}':", recommendations)
