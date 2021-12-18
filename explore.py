import pandas as pd
import numpy as np
from collections import defaultdict
import math
from random import randrange
from scipy.stats import uniform
import random
nft_count = 10000
main = True #if false run with all attributes
minor_variations = [x.lower().replace(' ', '_') for x in
                    ['Weapon', 'Background', 'War Paint', 'Eye Symbols', 'Piercings']]
major_variations = [x.lower().replace(' ', '_') for x in
                    ['Gender', 'Race', 'Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression',
                     'Armor']]

def cleanup(list_in: list):
    return [x.replace(' (Mouth/Eyes/Eyebrows)', '').lower().replace(' ', '_') for x in list_in]
def dict_cleaner(dict_in: dict):
    return {k.replace(' (Mouth/Eyes/Eyebrows)', '').lower().replace(' ', '_'): v for k, v in dict_in.items()}

attributes = cleanup(
                 ['Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Hair',
                  'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Weapon', 'Background',
                  'Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)',
                  'Armor', 'Weapon', 'Background', 'Eye Symbols', 'Piercings',
                  'Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet',
                  'Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet',
                  'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Facial Hair',
                  'Piercings', 'War Paint', 'Armor', 'Weapon', 'Background',
                  'Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet',
                  'Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)',
                  'Armor', 'Weapon', 'Background', 'War Paint',
                  'Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)',
                  'Armor', 'Weapon', 'Background', 'Eye Symbols', 'Piercings',
                  'Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet',
                  'Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet',
                  'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'War Paint',
                  'Piercings', 'Armor', 'Weapon', 'Background',
                  'Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])

male_human =    dict_cleaner({'Skin Color':3, 'Hair Color':5, 'Hair Style or Helmet':8, 'Facial Hair':5, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':20, 'Weapon':15, 'Background':8})
female_human =  dict_cleaner({'Skin Color':3, 'Hair Color':5, 'Hair Style or Helmet':8, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':15, 'Weapon':15, 'Background':8, 'War Paint':10})
male_punk =     dict_cleaner({'Skin Color':3, 'Hair Color':4, 'Hair Style or Helmet':6, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':12, 'Weapon':7, 'Background':8, 'Eye Symbols':10, 'Piercings':7})
female_punk =   dict_cleaner({'Skin Color':3, 'Hair Color':4, 'Hair Style or Helmet':6, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':8, 'Weapon':7, 'Background':8, 'Eye Symbols':10, 'Piercings':7})
male_shiba =    dict_cleaner({'Fur Color':7, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':15, 'Background':8, 'Weapon':5, 'Helmet':4})
female_shiba =  dict_cleaner({'Fur Color':7, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':10, 'Background':8, 'Weapon':5, 'Helmet':4})
male_ape =      dict_cleaner({'Fur Color':8, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':12, 'Background':8, 'Weapon':11, 'Helmet':4})
female_ape =    dict_cleaner({'Fur Color':8, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':8, 'Background':8, 'Weapon':11, 'Helmet':4})
male_orc =      dict_cleaner({'Hair Color':3, 'Hair Style or Helmet':6, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Facial Hair':4, 'Piercings':7, 'War Paint':5, 'Armor':12, 'Weapon':7, 'Background':8})
female_orc =    dict_cleaner({'Hair Color':2, 'Hair Style or Helmet':5, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'War Paint':5, 'Piercings':7, 'Armor':8, 'Weapon':7, 'Background':8})
male_cat =      dict_cleaner({'Fur Color':5, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':12, 'Background':8, 'Weapon':5, 'Helmet':4})
female_cat =    dict_cleaner({'Fur Color':5, 'Facial Expression (Mouth/Eyes/Eyebrows)':6, 'Armor':8, 'Background':8, 'Weapon':5, 'Helmet':4})



######################
# GENDER DIFFERENCES #
######################
attribute_dict = {'male_punk': list(male_punk.keys()),
 'female_punk': list(female_punk.keys()),
 'male_human': list(male_human.keys()),
 'female_human': list(female_human.keys()),
 'male_shiba': list(male_shiba.keys()),
 'female_shiba': list(female_shiba.keys()),
 'male_ape': list(male_ape.keys()),
 'female_ape': list(female_ape.keys()),
 'male_orc': list(male_orc.keys()),
 'female_orc': list(female_orc.keys()),
 'male_cat': list(male_cat.keys()),
 'female_cat': list(female_cat.keys())}

count_dict   = {'male_punk': male_punk,
 'female_punk': female_punk,
 'male_human': male_human,
 'female_human': female_human,
 'male_shiba': male_shiba,
 'female_shiba': female_shiba,
 'male_ape': male_ape,
 'female_ape': female_ape,
 'male_orc': male_orc,
 'female_orc': female_orc,
 'male_cat': male_cat,
 'female_cat': female_cat}

attributes_main_dict = {k:v for k,v in attribute_dict.items() if v not in minor_variations}

attributes_all=set()
attributes_main = set()
attribute_to_race_dict = defaultdict(lambda:[])
for v in attribute_dict.keys():
    attributes_all = attributes_all.union(set(attribute_dict[v]))

for v in attributes_main_dict.keys():
    attributes_main = attributes_main.union(set(attributes_main_dict[v]))

for attribute in attributes_all:
    for class_sex in attribute_dict.keys():
        attribute_to_race_dict[attribute]=list(set(attribute_to_race_dict[attribute]).union(set([class_sex])))

cols = ['character_type']+list(attributes_main) if main else  ['character_type']+list(attributes_all)
df = pd.DataFrame(np.random.rand(nft_count,len(cols)),columns=cols)

character_type_pct_dict = {'male_punk': 10,
 'female_punk': 8,
 'male_human': 20,
 'female_human': 12,
 'male_shiba': 6,
 'female_shiba': 4,
 'male_ape': 8,
 'female_ape': 5,
 'male_orc': 10,
 'female_orc': 4,
 'male_cat': 7,
 'female_cat': 6}

char_field = []
for k,v in character_type_pct_dict.items():
    char_field.extend([k]*int(v*nft_count/100))



df['character_type']=char_field
import random
character_types = list(character_type_pct_dict.keys())

df['character_type']=char_field
character_types = list(character_type_pct_dict.keys())
for i, character_type in enumerate(char_field):
    df.loc[i,list(set(df.columns)-set(attribute_dict[character_type])-set(['character_type']))]=None
    update = df.loc[df['character_type'] == character_type, list(set(df.columns) - set(attribute_dict[character_type]))]
    size = update.shape[0]
    for col in attribute_dict[character_type]:
        update.loc[:, col] = [col + '_' + str(x) for x in
                              np.random.choice(np.arange(1, count_dict[character_type][col] + 1), size)]

#dedupe
dedupe_count = 0
while sum(df.duplicated(keep='last'))>0:
    dedupe_count+=1
    print(dedupe_count)
    for i in range(df[df.duplicated(keep='last')].shape[0]):
        for col in attribute_dict[df.loc[i,'character_type']]:
            df.loc[i,col]=col+'_'+str(random.randrange(1,count_dict[df.loc[i,'character_type']][col]+1)) #

print(f'{dedupe_count} collisions')