#%%
### define constants
script_path = './dataset/screenplay_data/data/raw_text_lemmas/raw_text_lemmas/'

#%%
script_file = '3 Idiots_1187043_lemmas.txt'
script = open(script_path + script_file, 'r')
script_text = script.read()
script.close()
# %%
