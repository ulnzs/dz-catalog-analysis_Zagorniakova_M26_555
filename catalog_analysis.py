import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]
def average_rating(movies):
    ratings = []

    for movie in movies:
        ratings.append(movie["rating"])

    average = sum(ratings) / len(ratings)

    return round(average, 1)

def catalog_age_stats(movies, current_year=2026):
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, average)

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо" if rating < 9 else "шедевр"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"
    
def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"
def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])
def find_first_masterpiece(movies):
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            print(movie["title"])
            break

        index += 1
    else:
        print("Шедевров не найдено")
def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count
def demo_stage_3():
    print_non_comedy_movies(movies)
    find_first_masterpiece(movies)
    find_first_masterpiece([])
    print(count_long_movies(movies))
def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:]
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)

def make_slug(title):
    normalized = normalize_title(title)
    return normalized.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    top_movies = sorted_movies[:n]

    return [(movie["title"], movie["rating"]) for movie in top_movies]

def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts

def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography

def above_average_ratings(movies):
    average = average_rating(movies)

    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b