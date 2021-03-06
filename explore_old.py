import pandas as pd
import numpy as np
from collections import defaultdict
minor_variations = [x.lower().replace(' ', '_') for x in
                    ['Weapon', 'Background', 'War Paint', 'Eye Symbols', 'Piercings']]
major_variations = [x.lower().replace(' ', '_') for x in
                    ['Gender', 'Race', 'Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression',
                     'Armor']]


def cleanup(list_in: list):
    return [x.replace('(Mouth/Eyes/Eyebrows)', '').lower().replace(' ', '_') for x in list_in]


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

male_punk = cleanup(['Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor',
             'Weapon', 'Background', 'Eye Symbols', 'Piercings'])
female_punk = cleanup(['Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Weapon', 'Background', 'Eye Symbols', 'Piercings'])

male_human=     cleanup(['Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Hair', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Weapon', 'Background'])
female_human=   cleanup(['Skin Color', 'Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Weapon', 'Background', 'War Paint'])

male_shiba=     cleanup(['Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])
female_shiba=   cleanup(['Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])

male_ape=       cleanup(['Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])
female_ape=     cleanup(['Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])

male_orc=       cleanup(['Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Facial Hair', 'Piercings', 'War Paint', 'Armor', 'Weapon', 'Background'])
female_orc=     cleanup(['Hair Color', 'Hair Style or Helmet', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'War Paint', 'Piercings', 'Armor', 'Weapon', 'Background'])

male_cat=       cleanup(['Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])
female_cat=     cleanup(['Fur Color', 'Facial Expression (Mouth/Eyes/Eyebrows)', 'Armor', 'Background', 'Weapon', 'Helmet'])

######################
# GENDER DIFFERENCES #
######################
attribute_dict = {'male_punk': male_punk,
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

male_keys = [k for k in attribute_dict.keys() if 'female' not in k]
female_keys = set(attribute_dict.keys())-set(male_keys)

attributes_all = set()
attributes_female_all = set()
attributes_male_all = set()
for v in attribute_dict.keys():
    attributes_all = attributes_all.union(set(attribute_dict[v]))
for v in female_keys:
    attributes_female_all = attributes_female_all.union(set(attribute_dict[v]))
for v in male_keys:
    attributes_male_all = attributes_male_all.union(set(attribute_dict[v]))

###
#long walk to find out male only adds facial hair, but okay!
attributes_both = attributes_male_all.intersection(attributes_female_all)
attributes_female_only = attributes_all-attributes_male_all-attributes_both
attributes_male_only = attributes_all-attributes_female_all-attributes_both

male_only = set(np.setdiff1d(list(attributes_male_all),list(attributes_female_all)))
female_only = set(np.setdiff1d(list(attributes_female_all),list(attributes_male_all)))

####################
# RACE DIFFERENCES #
####################

races = list(set(k.split('_')[1] for k in attribute_dict.keys()))
race_unique_dict = dict()
for race in races:
    race_all = set([sub_k for k in attribute_dict.keys() for sub_k in attribute_dict[k] if race in k])
    other_races = set([sub_k for k in attribute_dict.keys() for sub_k in attribute_dict[k] if race not in k])
    race_unique =  set(np.setdiff1d(list(race_all),list(other_races)))
    race_unique_dict[race]=race_unique


assert sum([len(v) for v in race_unique_dict.values()])==0, 'Coded to expect no unique race attributes'


######################
# RACE GROUPS #
######################

races = list(set(k.split('_')[1] for k in attribute_dict.keys()))
race_group_attributes = defaultdict(lambda: [[],{}])
grp_counter = 0
for race in races:
    race_all = set([sub_k for k in attribute_dict.keys() for sub_k in attribute_dict[k] if race in k])
    new = True
    for k in race_group_attributes.keys():
        if set(race_group_attributes[k][1])==race_all:
            race_group_attributes[k][0]+=[race]
            new=False
    if new:
        race_group_attributes[grp_counter]=[[race],list(race_all)]
        grp_counter+=1



race_groups = {'race_flesh' : ['human', 'punk'],
'race_fur'   : ['ape', 'cat', 'orc', 'shiba']}
race_group_attributes

