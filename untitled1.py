# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:30:10 2020

@author: Sashank
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Sashank/Documents/ds_salary_india_proj/chromedriver"

df = gs.get_jobs("data scientist",1000, False, path, 15)

