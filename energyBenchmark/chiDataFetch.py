#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:10:18 2018

@author: guru


Python requests library to connect to API endpoint
"""

from requests import get 
import json
import pandas as pd

r = get("https://data.cityofchicago.org/resource/9wsh-b774.json")

print(r.status_code)

print(r.text)

energyData = r.json()

print(energyData)