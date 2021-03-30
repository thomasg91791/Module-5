if __name__ == "__main__":
    pokedex ={}

    pokedex['Venosaur'] = ['grass', 'poisen']
    pokedex['Charizard'] = ['fire', 'flying']
    pokedex['Blastoise'] = ['water']

    del pokedex['Blastoise']
    
    print(pokedex)