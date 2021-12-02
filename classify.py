def weather(data):
    '''
    Nothing but brute forcing, there may be regex that can do the same but im too lazy to do so.
    This is so ineffective and ugly that it makes me cringe, but theres no switch and case in 3.7 so good luck
    If word cannot be classified, data will be returned'''
    words = data.split(" ")
    if words[-1] == "fair":
        return 1
    elif "warm" in words:
        return 2
    elif words[-1] == "cloudy" and words[-2] == "partly":
        return 3
    elif words[-1] == "cloudy" and words[-2] != "partly":
        return 4
    elif words[-1] == "hazy" and words[-2] != "slightly":
        return 5
    elif words[-1] == "hazy" and words[-2] == "slightly":
        return 6
    elif "windy" in words:
        return 7
    elif "mist" in words:
        return 8
    elif words[-1] == "rain" and words[-2] == "light":
        return 9
    elif words[-1] == "rain" and words[-2] == "moderate":
        return 10
    elif words[-1] == "rain" and words[-2] == "heavy":
        return 11
    elif words[-1] == "showers" and words[-2] == "passing":
        return 12
    elif words[-1] == "showers" and words[-2] == "light":
        return 13
    elif words[-1] == "showers" and words[-2] == "heavy":
        return 15
    elif words[-1] == "showers" and words[-2] == "thundery" and words[-3] != "heavy":
        return 16
    elif words[-1] == "showers" and words[-2] == "thundery" and words[-3] == "heavy":
        return 17
    elif words[-1] == "showers" and words[-2] != ("passing" or "light" or "heavy" or "thundery"):
        return 14
    elif "gusty" in words:
        return 18
    else:
        return data


"""
Testing:

for i in ['e fair',
'e fair & warm',
'e partly cloudy',
'e cloudy',
'e hazy',
'e slightly hazy',
'e windy',
'e mist',
'e light rain',
'e moderate rain',
'e heavy rain',
'e passing showers',
'e light showers',
'e showers',
'e heavy showers',
'e thundery showers',
'e heavy thundery showers',
'e heavy thundery showers with gusty winds']:
    print(weather(i))"""

""" TODO add to readme
fair 1
fair & warm 2
partly cloudy 3
cloudy 4
hazy 5
slightly hazy 6
windy 7
mist 8
light rain 9
moderate rain 10
heavy rain 11
passing showers 12
light showers 13
showers 14
heavy showers 15
thundery showers 16
heavy thundery showers 17
heavy thundery showers with gusty winds 18
"""
