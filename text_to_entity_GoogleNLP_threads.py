import json
import requests
import os
import threading

def process_movie(movie_file):
    movie_file = movie_file.strip()  # Remove leading/trailing whitespace and newline
    if not movie_file:
        return  # Skip empty lines
        
    movie_script_path = os.path.join(script_path, movie_file)
    if not os.path.exists(movie_script_path):
        print(f"Script not found for movie: {movie_file}")
        return
        
    with open(movie_script_path, 'r') as script:
        script_text = script.read()
    
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": script_text
        }
    }
    
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        json_str = json.dumps(data, indent=4)
        movie_file_json = movie_file.replace('lemmas.txt', 'gc_entities.json')
        movie_entities_path = os.path.join(json_dataset_path, movie_file_json)
        with open(movie_entities_path, 'w') as json_entities:
            json_entities.write(json_str)
        print(f"Request success with status code {response.status_code} in movie {movie_file}")
    else:
        with open("error_list_movie", 'a') as error_list_file:
            error_list_file.write(movie_file)
            error_list_file.write("\n")
            print(f"Request failed with status code {response.status_code}: {response.text} in movie {movie_file}")

def process_movies_thread(thread_num, movies_list):
    thread_movies = [movies_list[i] for i in range(thread_num, len(movies_list), 4)]
    for movie in thread_movies:
        process_movie(movie)

# Open the JSON file
with open('CloudNLP_credentials.json') as json_file:
    credential_data = json.load(json_file)

url = "https://language.googleapis.com/v1/documents:analyzeEntities?key="+credential_data['api_key']

script_path = './dataset/screenplay_data/data/raw_text_lemmas/raw_text_lemmas/'
movies_names_path = 'movies_names.txt'
json_dataset_path = './final_dataset/GoogleNLP_dataset/'

with open(movies_names_path, 'r') as list_of_movies:
    movies_list = list_of_movies.readlines()

num_threads = 4
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=process_movies_thread, args=(i, movies_list))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Script processing and json files record completed.")
