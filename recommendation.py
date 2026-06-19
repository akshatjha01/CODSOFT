movies = {
    "Action": ["Avengers", "John Wick", "Mad Max"],
    "Comedy": ["3 Idiots", "Hera Pheri", "Dhamaal"],
    "Horror": ["The Conjuring", "Annabelle", "Insidious"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print("=== Movie Recommendation System ===")
print("Available Genres:")
print("Action, Comedy, Horror, Sci-Fi")

genre = input("\nEnter your favorite genre: ").title()

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Sorry! Genre not available.")