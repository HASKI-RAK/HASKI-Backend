import math
from datetime import datetime

import numpy as np

import errors.errors as err
from utils import constants as cons

rng = np.random.default_rng(5)

ran_seed = int(datetime.timestamp(datetime.now()))

# Interpretation of Graf et al. for Learning Elements
# -1: negative Influence; 0: neutral; 1: positive Influence
# ACT-REF-SNS-INT-VIS-VRB-SEQ-GLO
influence = {
    "RQ": (-1, 1, 0, 1, 0, 0, 0, 0),
    "SE": (1, -1, 1, 0, 0, 0, 0, 0),
    "FO": (1, -1, 0, -1, -1, 1, 0, 0),
    "ZL": (-1, 1, -1, 1, -1, 1, 0, 0),
    "AN": (1, -1, 1, -1, 1, -1, 0, 0),
    "ÜB": (1, -1, 1, 1, 0, 0, 0, 0),
    "BE": (-1, 1, 1, -1, 0, 0, 0, 1),
    "AB": (0, 0, 1, -1, 0, 0, 0, 1),
}


# Calculate the coordinates for the LEs
def get_coordinates(learning_style, list_of_les, dimensions=4):
    coordinates = {}
    for elememnt in list_of_les:
        if elememnt == cons.abbreviation_ct:
            coordinates[cons.abbreviation_ct] = (13,) * dimensions
        elif elememnt == cons.abbreviation_co:
            coordinates[cons.abbreviation_co] = (12,) * dimensions
        elif elememnt == cons.abbreviation_as:
            coordinates[cons.abbreviation_as] = (-12,) * dimensions
        elif elememnt == cons.abbreviation_cc:
            if (
                learning_style["processing_dimension"] == "ref"
                and learning_style["understanding_dimension"] == "seq"
            ):
                if (
                    learning_style["processing_value"]
                    > learning_style["understanding_value"]
                ):
                    coordinates[cons.abbreviation_cc] = (11,) * dimensions
                else:
                    coordinates[cons.abbreviation_cc] = (0,) * dimensions
            elif (
                learning_style["processing_dimension"] == "ref"
                or learning_style["understanding_dimension"] == "glo"
            ):
                coordinates[cons.abbreviation_cc] = (11,) * dimensions
            else:
                coordinates[cons.abbreviation_cc] = (0,) * dimensions
        else:
            coordinate = list()
            if learning_style["processing_dimension"] == "act":
                coordinate.append(
                    learning_style["processing_value"] * influence[elememnt][0]
                )
            elif learning_style["processing_dimension"] == "ref":
                coordinate.append(
                    learning_style["processing_value"] * influence[elememnt][1]
                )
            if learning_style["perception_dimension"] == "sns":
                coordinate.append(
                    learning_style["perception_value"] * influence[elememnt][2]
                )
            elif learning_style["perception_dimension"] == "int":
                coordinate.append(
                    learning_style["perception_value"] * influence[elememnt][3]
                )
            if learning_style["input_dimension"] == "vis":
                coordinate.append(
                    learning_style["input_value"] * influence[elememnt][4]
                )
            elif learning_style["input_dimension"] == "vrb":
                coordinate.append(
                    learning_style["input_value"] * influence[elememnt][5]
                )
            if learning_style["understanding_dimension"] == "seq":
                coordinate.append(
                    learning_style["understanding_value"] * influence[elememnt][6]
                )
            elif learning_style["understanding_dimension"] == "glo":
                coordinate.append(
                    learning_style["understanding_value"] * influence[elememnt][7]
                )
            # ---
            if len(coordinate) < dimensions:
                coordinate.extend([0] * (dimensions - len(coordinate)))
            # opcional
            elif len(coordinate) > dimensions:
                coordinate = coordinate[:dimensions]
            # ---
            coordinates[elememnt] = tuple(coordinate)
    return coordinates


# Euclidean Distance Function
def distance(xyz1, xyz2) -> float:
    if isinstance(xyz1[0], str):
        xyz1 = xyz1[1]
        xyz2 = xyz2[1]
    return math.dist(xyz1, xyz2)


def permutation_generator(le_size, pop_size):
    """function to randomly generate population for ga"""
    positions = np.arange(1, le_size)
    perm = rng.permutation(positions)
    population = np.tile(perm, (pop_size, 1))
    population[0:20] = positions
    return population


def random_generator(num, size, type_):
    if type_ == "int":
        return rng.integers(0, num, size=1)

    elif type_ == "bool":
        return rng.choice([True, False], size)
    else:
        raise err.WrongParameterValueError()


def check_learning_style(input_learning_style):
    """ Check if learning style is correctly formatted and\
    has the right dimensions"""
    condition1 = cons.name_perception_dimension in input_learning_style.keys()
    condition2 = cons.name_input_dimension in input_learning_style.keys()
    condition3 = cons.name_processing_dimension in input_learning_style.keys()
    condition4 = cons.name_understanding_dimension in input_learning_style.keys()
    condition5 = cons.name_perception_value in input_learning_style.keys()
    condition6 = cons.name_input_value in input_learning_style.keys()
    condition7 = cons.name_processing_value in input_learning_style.keys()
    condition8 = cons.name_understanding_value in input_learning_style.keys()
    if not (
        condition1
        and condition2
        and condition3
        and condition4
        and condition5
        and condition6
        and condition7
        and condition8
    ):
        raise err.WrongLearningStyleNumberError()
    condition9 = -11 <= input_learning_style[cons.name_perception_value] <= 11
    condition10 = -11 <= input_learning_style[cons.name_input_value] <= 11
    condition11 = -11 <= input_learning_style[cons.name_processing_value] <= 11
    condition12 = -11 <= input_learning_style[cons.name_understanding_value] <= 11
    if not (condition9 and condition10 and condition11 and condition12):
        raise err.WrongLearningStyleDimensionError()
    else:
        return True


def check_cons_learning_element(element):
    abbreviations = [
        cons.abbreviation_ct,  # "KÜ",
        cons.abbreviation_co,  # "EK"
        cons.abbreviation_rq,  # "RQ"
        cons.abbreviation_se,  # "SE"
        cons.abbreviation_fo,  # "FO"
        cons.abbreviation_rm,  # "ZL"
        cons.abbreviation_an,  # "AN"
        cons.abbreviation_ec,  # "ÜB"
        cons.abbreviation_ex,  # "BE"
        cons.abbreviation_ra,  # "AB"
        cons.abbreviation_cc,  # "ZF"
        cons.abbreviation_as,  # "LZ"
    ]
    if element in abbreviations:
        return True
    else:
        return False


def get_learning_element(learning_elements):
    """converts the dictionary learning element
    into a list with only the short name LE"""
    classification_learning_element = []
    lz_is_present = False
    lz_element = ""

    for le in learning_elements:
        if le["classification"] == cons.abbreviation_ct:
            classification_learning_element.insert(0, le["classification"])
        elif le["classification"] == cons.abbreviation_as:
            lz_is_present = True
            lz_element = le["classification"]
        elif check_cons_learning_element(le["classification"]):
            classification_learning_element.append(le["classification"])
    if lz_is_present:
        classification_learning_element.append(lz_element)
    return classification_learning_element


def get_learning_path_as_str(result_ga):
    """Convert the list of learning path into string"""
    str_learning_path = ""
    contain_le = False
    for ele in result_ga:
        str_learning_path = str_learning_path + ele + ", "
        contain_le = True
    if contain_le:
        str_learning_path = str_learning_path[:-2]

    return str_learning_path


def normalize_array2(data, old_min, old_max, new_min=-12, new_max=13):
    """
    Scale a value from an old range to a new range.

    Parameters:
        data: float or array-like
            Value(s) to normalize.
        old_min, old_max: float
            Original range.
        new_min, new_max: float, optional
            Target range (default -12 to 13).

    Returns:
        float or array-like: Normalized value(s).
    """
    if old_max == old_min:
        return (new_min + new_max) / 2
    return new_min + (data - old_min) * (new_max - new_min) / (old_max - old_min)


def added_view_times(input_view_time):
    """
    Normalize view/time values for each learning element.

    Parameters:
        input_view_time: dict
            Mapping {label: (view, time)} with raw values.

    Returns:
        dict: {label: (norm_view, norm_time)} normalized to the target range.
    """
    views = [v[0] for v in input_view_time.values()]
    times = [v[1] for v in input_view_time.values()]
    # views, times = zip(*input_view_time.values())

    old_min_view, old_max_view = min(views), max(views)
    old_min_time, old_max_time = min(times), max(times)

    norm_view_time = {
        k: (
            int(normalize_array2(v[0], old_min_view, old_max_view)),  # normaliza view
            int(normalize_array2(v[1], old_min_time, old_max_time)),  # normaliza time
        )
        for k, v in input_view_time.items()
    }
    return norm_view_time


def update_coordinate(dict_coordinate, input_view_time):
    """
    Insert normalized view/time values into the last two positions of coordinates.

    Parameters:
        dict_coordinate: dict
            {label: coord_tuple} original coordinates.
        input_view_time: dict
            {label: (view, time)} normalized view/time values.

    Returns:
        dict: Updated coordinates with new view/time where applicable.
    """
    updated_coords = {}
    for k, coord in dict_coordinate.items():
        if k in input_view_time and k not in ("KÜ", "EK", "LZ"):
            view, time = input_view_time[k]
            # reemplazar penúltima y última posición
            new_coord = coord[:-2] + (view, time)
            updated_coords[k] = new_coord
        else:
            updated_coords[k] = coord  # si no tiene view/time lo dejamos igual
    # print("\n\ncoordinate_update:", updated_coords)
    return updated_coords
