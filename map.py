import folium
import pandas
web_data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(web_data["LAT"])
lon=list(web_data["LON"])
elev=list(web_data["ELEV"])
def color_chooser(elevation):
    if elevation < 1000:
        return "blue"
    elif 1000 <= elevation < 3000:
        return "green"
    else:
        return "orange"

mapps=folium.Map(location=[8.066969, -1.056430],zoom_start=7,tiles="Mapbox Bright")

feature_volcanoes = folium.FeatureGroup(name="volcanoes")


for lt,ln,el in zip(lat,lon,elev):
    feature_volcanoes.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+" m",
    radius=8, fill_color=color_chooser(el), color ="grey", fill_opacity=0.6))

feature_population =folium.FeatureGroup(name="Population")

feature_population.add_child(folium.GeoJson(data=open('115 world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':"brown" if x['properties']['POP2005'] < 10000000
else 'yellow' if 10000000<= x['properties']['POP2005'] < 20000000 else 'green'}))

mapps.add_child(feature_volcanoes)
mapps.add_child(feature_population)
mapps.add_child(folium.LayerControl())
mapps.save("map.html")
