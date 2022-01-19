from pygal_maps_world import i18n

for countryCode in sorted(i18n.COUNTRIES.keys()):
    print(countryCode, i18n.COUNTRIES[countryCode])