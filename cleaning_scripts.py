import os

script_path = './dataset/screenplay_data/data/raw_text_lemmas/raw_text_lemmas/'
movies_names_path = 'movies_names.txt'

with open(movies_names_path, 'r') as list_of_movies:
    for movie_file in list_of_movies:
        movie_file = movie_file.strip()  # Remove leading/trailing whitespace and newline
        if not movie_file:
            continue  # Skip empty lines
        
        movie_script_path = os.path.join(script_path, movie_file)
        if not os.path.exists(movie_script_path):
            print(f"Script not found for movie: {movie_file}")
            continue
        
        with open(movie_script_path, 'r') as script:
            script_text = script.read()
        
        # Modify script_text (remove quotes)
        modified_script_text = script_text.replace('"', '')
        
        # Write the modified content back to the same file
        with open(movie_script_path, 'w') as script:
            script.write(modified_script_text)
        
        # Do something with modified_script_text, e.g., process or analyze it
        
print("Script processing and modification completed.")
