from pygal_maps_world import i18n

def getCountryCode(countryName):

    for code, name in i18n.COUNTRIES.items():
        if name == countryName:
            return code
    
    return None

print(getCountryCode("Somalia"))
print(getCountryCode("Pakistan"))
print(getCountryCode("Iraq"))