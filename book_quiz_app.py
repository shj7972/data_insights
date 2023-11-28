# run_book_quiz_app.py
import streamlit as st

def run_book_quiz_app():
    st.title("Find Your Next Book!")

    # Expanded genre list
    genres = ["Fantasy", "Mystery", "Romance", "Non-fiction", "Science Fiction", "Thriller", "Biography", "Young Adult", "Children's Books", "Historical Fiction"]
    genre = st.selectbox("Choose your preferred genre", genres)

    # Additional questions (mood, length, etc.)
    # ...

    if st.button("Get Recommendation"):
        # Sample book data (expand this with actual data)
        book_data = {
            "Fantasy": {
                "title": "The Hobbit by J.R.R. Tolkien",
                "thumbnail": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FHobbit-J-R-Tolkien%2Fdp%2F054792822X&psig=AOvVaw3YB_WueGqQlF2TzQk4CPCe&ust=1700658507342000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNCBr-SU1YIDFQAAAAAdAAAAABAE",
                "review": "A classic fantasy novel about..."
            },
            "Mystery": {
                "title": "Sherlock Holmes by Arthur Conan Doyle",
                "thumbnail": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FOriginal-Illustrated-Sherlock-Holmes%2Fdp%2F0890090572&psig=AOvVaw0kfGKlicpSlrg3DZRxsmcH&ust=1700658540930000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCIjA7_SU1YIDFQAAAAAdAAAAABAE",
                "review": "A thrilling mystery featuring the famous detective..."
            },
            # Add entries for other genres
        }

        if genre in book_data:
            book = book_data[genre]
            st.image(book["thumbnail"], caption=book["title"])
            st.write(book["review"])
        else:
            st.write("No recommendation available for the selected options.")

# Remember to import and call this function in your main Streamlit app

if __name__ == '__main__':
    run_book_quiz_app()     