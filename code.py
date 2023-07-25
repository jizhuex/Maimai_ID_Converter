import json

path = './data/'

def df2game(get_id):
    with open(path + 'alias.json', 'r', encoding='utf-8') as fp1:
        game_data = json.load(fp1)
    with open(path + 'alias_uc.json', 'r', encoding='utf-8') as fp2:
        df_data = json.load(fp2)

    for key,values in df_data.items():
        try:
            music_id = values[0]

            if music_id == get_id:
                music_name = key
                break
        except:
            k = 0

    for key,values in game_data.items():
        try:
            music_id = values[0]

            if music_name == key:
                ret_id = values[0]
                return(ret_id)
                break
        except:
            k = 0

def game2df(get_id):
    with open(path + 'alias.json', 'r', encoding='utf-8') as fp1:
        game_data = json.load(fp1)
    with open(path + 'alias_uc.json', 'r', encoding='utf-8') as fp2:
        df_data = json.load(fp2)

    for key,values in game_data.items():
        try:
            music_id = values[0]

            if music_id == get_id:
                music_name = key
                break
        except:
            k = 0

    for key,values in df_data.items():
        try:
            music_id = values[0]

            if music_name == key:
                ret_id = values[0]
                return(ret_id)
                break
        except:
            k = 0
