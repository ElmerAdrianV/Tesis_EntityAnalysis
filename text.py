#%%
### define constants
script_path = './dataset/screenplay_data/data/raw_text_lemmas/raw_text_lemmas/'

#%%
script_file = '3 Idiots_1187043_lemmas.txt'
script = open(script_path + script_file, 'r')
script_text = script.read()
script.close()
# %%
from google.cloud import language_v1



def sample_analyze_entities():
    # Create a client
    client = language_v1.LanguageServiceClient()

    # Initialize request argument(s)
    document = language_v1.Document()
    script_file = '3 Idiots_1187043_lemmas.txt'
    script = open(script_path + script_file, 'r')
    script_text = script.read()
    document.content = script_text

    request = language_v1.AnalyzeEntitiesRequest(
        document=document,
    )

    # Make the request
    response = client.analyze_entities(request=request)

    # Handle the response
    print(response)

sample_analyze_entities()