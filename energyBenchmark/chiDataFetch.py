#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:10:18 2018

@author: guru


Python requests library to connect to API endpoint
"""

from requests import get 
import json

energyData = get("https://data.cityofchicago.org/resource/jaif-n74j.json")


print(energyData.status_code)

print(energyData.content)
