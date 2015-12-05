import sys
import os
import re
import json
import pprint

orbituray_di_path = "/Users/zhiyan/Projects/Tessa/tessa/orbiturary/highres"


# orbituray_path = os.path.join(orbituray_di_path, "kookeetiang_output.txt")

# print(orbituray_path)

def get_orbiturary_info(orbiturary_path):
    f = open(orbiturary_path, 'r')
    orbiturary_text = [ i for i in f]
    # print(orbiturary_text)
    return look_for_info(orbiturary_text)


def look_for_info(orbiturary_text):
    info = { "Name": None, "Family and Friends": None, "Postal Code": None, "Address": None, "Age": None, "Date of Death": None}
    names = list()
    name_regex = r"((([A-Z][a-zA-Z]+ ?){2,3})+)"
    name_pattern = re.compile(name_regex)
    date_regex = r"([0-9][0-9]? ?(january|feburary|march|april|may|june|july|august|september|october|december) (\d\d\d\d)?)"
    date_pattern = re.compile(date_regex, re.IGNORECASE)
    address_postal_code = list()
    postal_code_regex = r"(\b|\D)(?P<postalcode>[\d]{6})(\b|\D)"
    postal_code_pattern = re.compile(postal_code_regex)
    age_regex = "[Aa][Gg][Ee]|[Yy][Ee][Aa][Ss] ?[Oo][Ll][Dd]"
    age_pattern = re.compile(age_regex)
    age_number_regex = "(\d\d?\d?)"
    age_number_pattern = re.compile(age_number_regex)
    family_friends = list()

    for line in orbiturary_text:
        postal_code_search = postal_code_pattern.search(line)
        if postal_code_search:
            # print(postal_code_search)
            # print(postal_code_search.groups)
            address_postal_code.append((postal_code_search.group("postalcode"), line))
            # print(address_postal_code)
        name_search = name_pattern.search(line)
        while name_search:
            names.append(name_search.group(0))
            if name_search.end() == len(line):
                break
            else:
                name_search = name_pattern.search(line, name_search.end())
        if info["Age"] == None:
            age_search = age_pattern.search(line)
            if age_search:
                age_number_search_after = age_number_pattern.search(line, age_search.end())
                if age_number_search_after:
                    info["Age"] = age_number_search_after.group(0)
                else:
                    age_number_search_before = age_number_pattern.search(line, endpos=age_search.end())
                    if age_number_search_before:
                        info["Age"] = age_number_search_before.group(0)
        date_search = date_pattern.search(line)
        if date_search:
            info["Date of Death"] = date_search.group(0)

    
    if len(address_postal_code) > 2:
        info["Postal Code"] = address_postal_code[1][0]
        info["Address"] = address_postal_code[1][1]
    elif address_postal_code != list():
        info["Postal Code"] = address_postal_code[0][0]
        info["Address"] = address_postal_code[0][1]

    if names != list():
        info["Name"] = names[0]
        if len(names) > 1:
            info["Family and Friends"] = names[1:]
    # print(info)
    return info

def tojsonfile(fi_name, info):
    # print(info)
    with open(fi_name + ".json", 'w') as f:
        json.dump(info, f)
    pprint.pprint(info)

# tojsonfile("kookeetiang_output_parsed", get_orbiturary_info(orbituray_path))




