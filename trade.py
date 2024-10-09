import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import folium_static
from shapely.geometry import Point
import math

def create_circle_polygon(lat, lon, radius_km):
    # Convert radius from km to degrees
    radius_degrees = radius_km / 111.32  # Approximate degrees per km at the equator
    
    # Create a circle
    circle = Point(lon, lat).buffer(radius_degrees)
    return circle

def main():
    st.title("Trade Area Analysis")

    # User inputs
    lat = st.number_input("Latitude", value=37.7749)
    lon = st.number_input("Longitude", value=-122.4194)
    radius = st.number_input("Trade Area Radius (km)", value=5.0, min_value=0.1)

    # Create a map centered on the input location
    m = folium.Map(location=[lat, lon], zoom_start=12)

    # Add a marker for the center location
    folium.Marker([lat, lon], popup="Center").add_to(m)

    # Create and add the trade area circle
    trade_area = create_circle_polygon(lat, lon, radius)
    gdf = gpd.GeoDataFrame(geometry=[trade_area], crs="EPSG:4326")
    folium.GeoJson(gdf).add_to(m)

    # Display the map
    folium_static(m)

    # Calculate the trade area in square kilometers
    area_km2 = math.pi * radius ** 2
    st.write(f"Trade Area: {area_km2:.2f} km\u00b2")

if __name__ == "__main__":
    main()

print("Streamlit app code created. Run it using 'streamlit run &lt;filename&gt;.py' in your terminal.")