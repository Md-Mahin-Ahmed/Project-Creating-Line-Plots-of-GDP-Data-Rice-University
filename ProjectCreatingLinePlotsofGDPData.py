# -*- coding: utf-8 -*-
"""
Project: Creating Line Plots of GDP Data
Course: Python Data Visualization
"""

import csv


# ----------------------------
# CSV READER
# ----------------------------

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Read CSV into nested dictionary.
    Outer key = keyfield value (country name/code)
    """
    table = {}

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)

        for row in reader:
            table[row[keyfield]] = row

    return table


# ----------------------------
# GDP VALUES PER COUNTRY
# ----------------------------

def build_plot_values(gdpinfo, country_row):
    """
    Build list of (year, gdp) tuples for one country.

    Uses:
      gdpinfo["min_year"]
      gdpinfo["max_year"]
    """
    values = []

    for year in range(gdpinfo["min_year"], gdpinfo["max_year"] + 1):
        year_str = str(year)

        if year_str in country_row and country_row[year_str] != "":
            values.append((year, float(country_row[year_str])))

    return values


# ----------------------------
# MULTI-COUNTRY PLOT DICT
# ----------------------------

def build_plot_dict(gdpinfo, country_list):
    """
    Build dictionary:
      { country: [(year, gdp), ...] }
    """

    gdpdata = read_csv_as_nested_dict(
        gdpinfo["gdpfile"],
        gdpinfo["country_name"],
        gdpinfo["separator"],
        gdpinfo["quote"]
    )

    plot_dict = {}

    for country in country_list:
        if country in gdpdata:
            plot_dict[country] = build_plot_values(gdpinfo, gdpdata[country])
        else:
            plot_dict[country] = []

    return plot_dict


# ----------------------------
# STYLE FUNCTION (REQUIRED)
# ----------------------------

def style(gdpinfo, country_list):
    """
    Required by autograder.
    Returns same structure as build_plot_dict.
    """
    return build_plot_dict(gdpinfo, country_list)