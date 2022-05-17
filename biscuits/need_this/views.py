from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from need_this.models import Zodiac, Individual

def get_header():
    header = '<nav class="navbar navbar-light bg-light">\
  <div class="container-fluid">\
    <a class="navbar-brand" href="'+reverse('splash')+'">\
      <img src="/static/starastro.png" alt="" width="60" height="30" class="d-inline-block align-text-top">\
      Star Astrology\
    </a>\
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">\
      <span class="navbar-toggler-icon"></span>\
    </button>\
    <div class="collapse navbar-collapse" id="navbarNavDropdown">\
      <ul class="navbar-nav">\
        <li class="nav-item">\
          <a class="nav-link active" aria-current="page" href="'+ reverse('splash') +'">Home</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link" href="'+reverse('calculator') +'">Fantasy Celebrity Zodiac Sign Calculator</a>\
        </li>\
        <li class="nav-item">\
          <a class="nav-link" href="'+ reverse('b') +'">Natal Value Estimator</a>\
        </li>\
        <li class="nav-item dropdown">\
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">\
            Fantasy Celebrity Zodiac Signs\
          </a>\
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">'
    zodiacs = Zodiac.objects.all()
    for z in zodiacs:
        header += '<li><a class="dropdown-item" href="' + reverse('individuals',  kwargs={'zodiac_value': z.value}) + '">' + z.sign + '</a></li>'

    header += '\
          </ul>\
        </li>\
      </ul>\
    </div>\
  </div>\
</nav>'
    return header

def Splash(self):
    html = "<html><head><title>Star Astrology</title><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'> \
<style>ul{color:orange;}li{display:inline; padding: 0 5px;} \
body{background-size: 100% !important; background: lightblue; \
    </style></head><body>"
    html += get_header()
    html += "<body><div style='margin: 10px auto; width:300px; text-align:center;'><a class='btn btn-info btn-lg' href='" + reverse('b') + "'>Natal Value Estimator</a> \
    </br></br>\
    <a class='btn btn-secondary btn-lg' href='" + reverse('calculator') + "'> \
    Find Your Fantasy Celebrity Sign</a></div>"
    html += "<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script>\
</body></html>"
    return HttpResponse(html)

def Individuals(self, zodiac_value):
    inds = Individual.objects.filter(zodiac=Zodiac.objects.filter(value=zodiac_value).first()).order_by('name')
    html = "<html><head><title>Star Astrology</title><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'><style>body{background-size: 100% !important; background: lightblue; }</style></head><body>"
    html += get_header()
    html += "<h1>" + Zodiac.objects.filter(value=zodiac_value).first().sign + "<img style='max-height: 40px;' src='/static/" + Zodiac.objects.filter(value=zodiac_value).first().sign + ".png' /></h1><ul>"
    for i in inds:
        html += "<li><a target=_blank href='" + i.wiki + "'>" + i.name + "</a></li>"
    html += "</ul><script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script></body></html>"
    return HttpResponse(html)

def Calculator(self):
    html = "<html><head><title>Star Astrology</title><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'><style>body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} form,h3{text-align: center;}</style></head><body>"
    html += get_header()
    html += "<h3>Your birthday</h3><form action='calculate' method='POST'><select name=month><option value=01>January</option> \
    <option value=02>February</option> \
    <option value=03>March</option> \
    <option value=04>April</option> \
    <option value=05>May</option> \
    <option value=06>June</option> \
    <option value=07>July</option> \
    <option value=08>August</option> \
    <option value=09>September</option> \
    <option value=10>October</option> \
    <option value=11>November</option> \
    <option value=12>December</option> \
    </select><select name=day>"
    for i in range(1, 32):
        if i >= 10:
            html += "<option value=" + str(i) + ">" + str(i) + "</option>"
        else:
            html += "<option value=0" + str(i) + ">" + str(i) + "</option>"
    html += "</select><select name=year>"
    for i in range(1900, 2022):
        html += "<option>" + str(i) + "</option>"
    html += "</select></br></br><button class='btn btn-primary' type=submit>Calculate</button>"
    import django.middleware.csrf
    token = django.middleware.csrf.get_token(self)
    html += "<input type=hidden name=csrfmiddlewaretoken value='" + token + "'></form><script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script></body></html>"
    return HttpResponse(html)

def get_astro(sum):
    astro = 0
    rem = sum % 12
    sum /= 12
    sum = int(sum)
    if rem == 0:
        astro = (sum + 1) % 12
    elif rem == 1:
        if sum % 2 == 0:
            astro = int(sum / 2)
        elif sum < 6:
            astro = int(sum * 2)
        else:
            astro = sum - 6
    elif rem == 2:
        astro = ((sum - 4) + 12) % 12
    elif rem == 3:
        astro = (sum + 4) % 12
    elif rem == 4:
        astro = ((sum - 1) + 12) % 12
    elif rem == 5:
        astro = ((sum - 2) + 12) % 12
    elif rem == 6:
        astro = (sum + 6) % 12
    elif rem == 7:
        astro = ((sum - 5) + 12) % 12
    elif rem == 8:
        astro = (sum + 2) % 12
    elif rem == 9:
        if sum != 7:
            astro = sum
        else:
            astro = 1
    elif rem == 10:
        astro = (sum + 3) % 12
    else:
        astro = ((sum - 3) + 12) % 12
    if astro == 0:
        astro = 12
    return astro

def Calculate(self):
    month = self.POST.get('month')
    day = self.POST.get("day")
    year = self.POST.get('year')

    from flatlib.datetime import Datetime
    from flatlib.geopos import GeoPos
    from flatlib.chart import Chart
    from flatlib import const
    from flatlib import props
    
    date = Datetime(str(year) + '/' + str(month) + '/' + str(day), '12:00', '+00:00')
    pos = GeoPos('38n32', '8w54')
    lis = const.LIST_OBJECTS
    if "Chiron" in lis:
        lis.remove('Chiron')
    chart = Chart(date, pos, IDs=lis)
    numbers = props.sign().number
    sun = chart.get(const.SUN).sign
    sun = (numbers.get(sun) + 3) % 12
    if sun == 0:
        sun = 12
    moon = chart.get(const.MOON).sign
    moon = (numbers.get(moon) + 3) % 12
    if moon == 0:
        moon = 12
    mercury = chart.get(const.MERCURY).sign
    mercury = (numbers.get(mercury) + 3) % 12
    if mercury == 0:
        mercury = 12
    venus = chart.get(const.VENUS).sign
    venus = (numbers.get(venus) + 3) % 12
    if venus == 0:
        venus = 12
    mars = chart.get(const.MARS).sign
    mars = (numbers.get(mars) + 3) % 12
    if mars == 0:
        mars = 12
    jupiter = chart.get(const.JUPITER).sign
    jupiter = (numbers.get(jupiter) + 3) % 12
    if jupiter == 0:
        jupiter = 12
    saturn = chart.get(const.SATURN).sign
    saturn = (numbers.get(saturn) + 3) % 12
    if saturn == 0:
        saturn = 12
    uranus = chart.get(const.URANUS).sign
    uranus = (numbers.get(uranus) + 3) % 12
    if uranus == 0:
        uranus = 12
    neptune = chart.get(const.NEPTUNE).sign
    neptune = (numbers.get(neptune) + 3) % 12
    if neptune == 0:
        neptune = 12
    pluto = chart.get(const.PLUTO).sign
    pluto = (numbers.get(pluto) + 3) % 12
    if pluto == 0:
        pluto = 12
    north_node = chart.get(const.NORTH_NODE).sign
    north_node = (numbers.get(north_node) + 3) % 12
    if north_node == 0:
        north_node = 12

    if int(day) < 10:
        day = day[1]
    if int(month) < 10:
        month = month[1]

    import requests
    response = requests.get('https://widgets.astro-seek.com/calculate-lilith/',\
                         params={'muz_narozeni_den': day,\
                               'muz_narozeni_mesic': month,\
                               'muz_narozeni_rok': year,\
                               'muz_narozeni_hodina': '12',\
                               'muz_narozeni_minuta': '00',\
                               'muz_narozeni_city': 'Seattle, USA, Washington',\
                                 'muz_narozeni_mesto_hidden': 'Seattle',\
                                 'muz_narozeni_stat_hidden': 'US',\
                                 'muz_narozeni_podstat_hidden': 'Washington'})
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    td = soup.find_all('td')[4]
    import re
    lilith = 1
    for i, k in enumerate(list(numbers.keys())):
        if k in td.img['alt']:
            lilith = (i + 4) % 12
            if lilith == 0:
                lilith == 12
            break
    sum = sun + moon + mercury + venus + mars \
      + jupiter + saturn + uranus + neptune \
      + pluto + north_node + lilith
    astro = (get_astro(sum) - 3) % 12
    if astro == 0:
        astro = 12

    sign = list(numbers.keys())[list(numbers.values()).index(astro)]

    html = "<html><head> <title>Star Astrology</title><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'><style>body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} div{text-align: center;}</style> </head><body>"
    html += get_header()
    html += "<div><h1>The fantasy celebrity sign for the birthday, </h1><blockquote>" + self.POST.get('month') + "/" + self.POST.get('day') + "/" + self.POST.get('year') + "</blockquote>"
    html += "<h2>is</h2>"
    html += "<blockquote><u>" + sign + "</u></blockquote><div style='text-align:center;'><img style='max-height: 200px;' src='static/" + sign  + ".png' /></div></br><a class='btn btn-info' href='" + reverse('calculator') + "'>Back</a></div><script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script></body></html>"
    return HttpResponse(html) 


def B(request):
    html = "<!DOCTYPE html><head><title>Star Astrology</title><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'>"
    html += "<link rel='shortcut icon' href='/favicon.ico'/></head>"
    html += "<body>"
    html += get_header()
    html += "<div class='container'><h1>Value of Natal Chart</h1>"
    html += "<form action='/estimate' method=GET><div class='mb-3'><label class='form-label' for='month'>Month</label><input requiredi min=1 max=12 class='form-control' type=number name=month id='month' /></div><div class='mb-3'><label class='form-label' for='day'>Day</label><input class='form-control' min=1 max=31 required type=number name=day id='day' /></div><div class='mb-3'><label for='year' class='form-label'>Year</label><input class='form-control' required type=number name=year id='year' /></div><button type=submit class='btn btn-primary'>Submit</button><div class='form-text'>This website uses <a href='https://www.astro.com/astrowiki/en/Domicile' target=_blank>domiciles</a> to determine the value of your natal chart.</div></form>"
    html += "</div><script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script></body></html>"
    return HttpResponse(html)

def do_some_stuff(request):
    import astro
    html = "<!DOCTYPE html><head><meta name='viewport' content='width=device-width, initial-scale=1'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'><link rel='shortcut icon' href='/favicon.ico'/><title>" + request.GET['month'] + "/" + request.GET['day'] + "/" + request.GET['year'] + "</title><style> body{background-color: #80f; text-align: center;} table{text-align:center;} tr{background-color: #c328b1;} tr:nth-child(odd){background-color: pink;} th{background-color: cyan !important;} a{color: white;} a:visited{color: black;} h3{margin: auto; margin-bottom: 10px;width: 400px; background-color: white; font-size: 35px;} div{margin: auto; text-align: center;}</style></head>"
    html += "<body>"
    html += get_header()
    html += "<h1>Estimated Value</h1>"
    ev = astro.get_estimated_value(request.GET['year'], request.GET['month'], request.GET['day'])
    estimated_value = ev[0]
    planets = ev[1]
    summa_cumma_latte = ev[2]
    degrees = ev[3]
    html += "<h3>" + str(estimated_value) + "</h3>"
    html += "<div><table border=1 align=center><tr><th>Planet</th><th>Sign</th><th>Degrees</th><th>Value</th></tr><tr><td>Sun</td><td>" + planets[0] + "</td><td>" + str(int(degrees[0]))  + "&deg;</td><td>" + str(summa_cumma_latte[0]) + "</td></tr>"
    html += "<tr><td>Moon</td><td>" + planets[1] + "</td><td>" + str(int(degrees[1]))  + "&deg;</td><td>" + str(summa_cumma_latte[1]) + "</td></tr>"
    html += "<tr><td>Mercury</td><td>" + planets[2] + "</td><td>" + str(int(degrees[2]))  + "&deg;</td><td>" + str(summa_cumma_latte[2]) + "</td></tr>"
    html += "<tr><td>Venus</td><td>" + planets[3] + "</td><td>" + str(int(degrees[3]))  + "&deg;</td><td>" + str(summa_cumma_latte[3]) + "</td></tr>"
    html += "<tr><td>Mars</td><td>" + planets[4] + "</td><td>" + str(int(degrees[4]))  + "&deg;</td><td>" + str(summa_cumma_latte[4]) + "</td></tr>"
    html += "<tr><td>Jupiter</td><td>" + planets[5] + "</td><td>" + str(int(degrees[5]))  + "&deg;</td><td>" + str(summa_cumma_latte[5]) + "</td></tr>"
    html += "<tr><td>Saturn</td><td>" + planets[6] + "</td><td>" + str(int(degrees[6]))  + "&deg;</td><td>" + str(summa_cumma_latte[6]) + "</td></tr>"
    html += "<tr><td>Uranus</td><td>" + planets[7] + "</td><td>" + str(int(degrees[7]))  + "&deg;</td><td>" + str(summa_cumma_latte[7]) + "</td></tr>"
    html += "<tr><td>Neptune</td><td>" + planets[8] + "</td><td>" + str(int(degrees[8]))  + "&deg;</td><td>" + str(summa_cumma_latte[8]) + "</td></tr>"
    html += "<tr><td>Pluto</td><td>" + planets[9] + "</td><td>" + str(int(degrees[9])) + "&deg;</td><td>" + str(summa_cumma_latte[9]) + "</td></tr></table></div>"
    html += "</br><a class='btn btn-info btn-lg' href='" + reverse('b') + "'>Back</a>"
    html += "<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script></body></html>"
    return HttpResponse(html)
 
