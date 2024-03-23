# important package installer 
pip install phonenumbers folium opencage geocoder

import phonenumbers
import folium
import sys
import argparse
import os
import re
from phonenumbers import geocoder
from folium.plugins import MarkerCluster
from opencage.geocoder import OpenCageGeocode

def get_phone_location(phone_number):
    phone_number = clean_phone_number("+91 7632079595")
    try:
        parsed_number = phonenumbers.parse("+91 7632079595")
    except:
        return "Invalid phone number"
    try:
        location = geocoder.description_for_number(parsed_number, "en")
    except:
        return "Unable to locate"
    return location

from phonenumbers import carrier

# Enter the phone number with the country code
phone_number = "+91 7632079595"

# Create a phone number object
phone_number_object = phonenumbers.parse(phone_number)

# Get the service provider
service_provider = carrier.name_for_number(phone_number_object, 'en')

# Print the service provider
print(service_provider) 


