
'''
The next code ask the user to write his city his grew up in and his pads name,
and combine this answers into his rock band name.

'''
def band_generator(city_name, pet_name):
    band_gen = city_name + " "  + pet_name
    return band_gen

if __name__ == "__main__":

    print ("Welcome to the Band Name Generator")
    city_name = input ("What's name of the city you grew up in ?")
    print (city_name)
    pet_name = input ("What's your pet's name ?")
    print(pet_name)

    bend_gen = band_generator(city_name, pet_name)
    print (bend_gen)




