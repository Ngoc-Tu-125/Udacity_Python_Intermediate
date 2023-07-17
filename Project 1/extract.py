"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos_list = []
    with open(neo_csv_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            neos_designation = row['pdes']
            neos_name = row['name'] or None
            neos_diameter = float(row['diameter']) if row['diameter'] else float('nan')
            neos_hazardous = False if row['pha'] in ['', 'N'] else True
            neos_list.append(
                NearEarthObject(
                    designation=neos_designation,
                    name=neos_name,
                    diameter=neos_diameter,
                    hazardous=neos_hazardous,
                )
            )

    return neos_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cad_list = []
    with open(cad_json_path, 'r') as jsonfile:
        cad_data = json.load(jsonfile)['data']

    # "des" = 0, "cd" = 3, "dist" = 4, "v_rel" = 7
    for row in cad_data:
        cad_list.append(
            CloseApproach(
                designation=row[0],
                time=row[3],
                distance=float(row[4]),
                velocity=float(row[7]),
            )
        )

    return cad_list
