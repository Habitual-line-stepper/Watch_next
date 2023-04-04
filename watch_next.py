# Import SpaCy
import spacy

# Create a pipeline
nlp = spacy.load("en_core_web_md")

# Create a base description to compare to.
# Can be modified to take user input
synopsis = ("Will he save their world or destroy it? When the "
            "Hulk becomes too dangerous for the Earth, "
            "the Illuminati trick Hulk into a shuttle and launch "
            "him into space to a planet where the Hulk can live "
            "in peace. Unfortunately, Hulk land on the planet "
            "Sakaar where he is sold into slavery and trained as "
            "a gladiator.")


# Create a function to find the movie
# most similar to the description
def find_similar_movie(description):
    # open the text file
    with open("movies.txt", "r") as f:
        # read in each line and save to movies variable
        movies = f.readlines()

    # Create an empty list to store the similarity scores
    similarity_scores = []
    # for each movie in the movies variable
    for movie in movies:
        # check which movies have the most similar description
        # using .similarity
        # then print the movie title and similarity scores out
        sim = nlp(movie).similarity(nlp(synopsis))
        doc = nlp(movie.split(":")[1])
        similarity_scores.append(doc.similarity(nlp(description)))
        movie_title = movie.split(":")[0]
        print(f"{movie_title} - Similarity Score: {sim}")

    # Find the index of the highest similarity
    # score in the list similarity_scores.
    # The max() function returns the highest value in the list,
    # and index() returns the index of that value in the list.
    most_similar_index = similarity_scores.index(max(similarity_scores))
    # Retrieves the title of the most similar movie from the movies list
    # using the most_similar_index found in the previous line.
    # The .split(":")[0] method is used to split the
    # movie description by the : character
    # It only keeps the title portion of the string.
    # This title is then assigned to the most_similar_movie variable.
    most_similar_movie = movies[most_similar_index].split(":")[0]

    # Return the result
    return f"\nMost similar movie by description: {most_similar_movie.strip()}"


print(find_similar_movie(synopsis))
