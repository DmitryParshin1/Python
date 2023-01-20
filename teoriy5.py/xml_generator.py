from user_interface import wind_speed_view
from user_interface import pressure_view

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '        <temperature units = "f">{}<temperature>\n'\
        .format(t)
    xml += '        <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '        <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '</xml>'

    with open('new_index.html', 'w') as page:
        page.write(xml)

    return xml