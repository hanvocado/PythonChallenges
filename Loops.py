from data import countries as ct

def find_most_spoken_lan():
    languages = {}
    for country in countries :
        for lan in country['languages'] :
            if languages.get(lan) :
                languages[lan] += country['population']
            else :
                languages[lan] = country['population']

    sorted_languages = sorted(languages.items(), key = lambda item: item[1], reverse=True)
    return sorted_languages[:10]

def find_most_populated_countries():
    sorted_contries = sorted(countries, key = lambda country: country['population'], reverse=True)
    return sorted_contries[:10]

countries = ct.data
print('Most spoken languages: ')
for lanuage in find_most_spoken_lan() :
    print(f'{lanuage[0]}: {lanuage[1]}')

print('\nMost populated countries: ')
for country in find_most_populated_countries() :
    print(f'{country["name"]}: {country["population"]}')