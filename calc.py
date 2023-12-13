
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   result = megabit * 8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   result = (litres * 100) / kilometers
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = celsius * 1.8 + 32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result=0
    a=1
    while (tail>=a):
        result = result + a
        a += 1
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if (grams>=1000000):
        grams=grams/1000000
        return str(int(grams)) + "t"
    elif (grams>=100000):
        grams=grams/100000
        return str(int(grams)) + "c"
    elif (grams>=1000):
        grams=grams/1000
        return str(int(grams)) + "kg"
    else:
        return str(int(grams)) + "g"