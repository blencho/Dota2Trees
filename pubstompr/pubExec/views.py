from django.http import HttpResponse
from pubstompr import pubstomp

def index(request):
    defaultHero = -1;
    radiant = [];
    radKeys = ["0.1", "0.2", "0.3", "0.4", "0.5"];

    dire = [];
    direKeys = ["1.1", "1.2", "1.3", "1.4", "1.5"];


    queryDict = request.GET;

    team = queryDict.get("team", 0);
    for i in range(5):
        radiant.append(queryDict.get(radKeys[i], defaultHero));
        dire.append(queryDict.get(direKeys[i], defaultHero));

    # Call python executable
    recommend = pubstomp(team, radiant, dire);

    return HttpResponse(recommend);

