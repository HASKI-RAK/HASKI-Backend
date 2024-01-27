import numpy as np
import pytest

import errors.errors as err
from domain.domainModel import model as DM
from domain.learnersModel import model as LM
from domain.tutoringModel import model as TM
from domain.tutoringModel import utils

rng = np.random.default_rng(20)


def test_prepare_les_for_aco():
    list_of_les = []
    list_of_keys = ["BE", "FO", "KÜ", "SE", "LZ", "EK", "ÜB"]
    for i, key in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=key,
            name="Test",
            university="TH-AB",
            created_by=i,
            created_at="2023-01-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="aco")
    result = lp.prepare_le_for_aco(list_of_les=list_of_les)
    assert type(result) == list
    assert len(result) != 0
    assert result[0] == "KÜ"
    assert result[-1] == "LZ"


def test_distance():
    result = utils.distance((1, 1, 1, 1), (2, 2, 2, 2))
    assert type(result) == float
    assert result == 2


@pytest.mark.parametrize(
    "input_dimension, perception_dimension,\
                         processing_dimension, understanding_dimension",
    [("vis", "sns", "act", "glo"), ("vrb", "int", "ref", "seq")],
)
def test_get_coordinates(
    input_dimension, perception_dimension, processing_dimension, understanding_dimension
):
    ls = LM.LearningStyle(
        input_dimension=input_dimension,
        input_value=7,
        perception_dimension=perception_dimension,
        perception_value=7,
        processing_dimension=processing_dimension,
        processing_value=7,
        understanding_dimension=understanding_dimension,
        understanding_value=7,
    )
    list_of_les = ["BE", "FO", "KÜ", "SE", "LZ", "EK", "ÜB", "ZF", "ÜB"]
    result = utils.get_coordinates(
        learning_style=ls.serialize(), list_of_les=list_of_les
    )
    assert type(result) == dict
    assert result is not None
    assert result["KÜ"] == (13, 13, 13, 13)
    assert result["EK"] == (12, 12, 12, 12)
    assert result["LZ"] == (-12, -12, -12, -12)


@pytest.mark.parametrize(
    "learning_style",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 11,
                "input_dimension": "vrb",
                "input_value": 11,
                "processing_dimension": "act",
                "processing_value": 11,
                "understanding_dimension": "seq",
                "understanding_value": 11,
            }
        ),
        (
            {
                "id": 1,
                "characteristic_id": 7,
                "perception_dimension": "int",
                "perception_value": 1,
                "input_dimension": "vis",
                "input_value": 1,
                "processing_dimension": "ref",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 0,
            }
        ),
    ],
)
def test_prepare_les_for_ga_fixed_LE(learning_style):
    list_of_les = []
    list_of_keys = ["KÜ", "LZ", "ÜB", "SE", "BE", "AN", "EK", "ZL", "AB", "ZF"]
    for i, ele_name in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="ga")
    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="ga",
        list_of_les=list_of_les,
    )
    result = lp.path
    assert isinstance(result, str)
    assert ", " in result
    result = result.split(", ")
    assert isinstance(result, list)
    assert result[0] == "KÜ"
    assert result[1] == "EK"
    assert result[-1] == "LZ"


@pytest.mark.parametrize(
    "learning_style, list_of_keys",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 3,
                "input_dimension": "vis",
                "input_value": 5,
                "processing_dimension": "ref",
                "processing_value": 7,
                "understanding_dimension": "glo",
                "understanding_value": 1,
            },
            ["KÜ", "ÜB", "ÜB", "ÜB", "ÜB", "SE", "LZ", "ZL", "AN", "EK", "EK"],
        ),
        (
            {
                "id": 1,
                "characteristic_id": 7,
                "perception_dimension": "int",
                "perception_value": 9,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 5,
            },
            ["ÜB", "ÜB", "ÜB", "LZ", "EK", "SE", "EK", "ZL", "ZF", "AN", "KÜ", "EK"],
        ),
        (
            {
                "id": 1,
                "characteristic_id": 7,
                "perception_dimension": "int",
                "perception_value": 9,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 5,
            },
            [
                "ÜB",
                "ÜB",
                "LZ",
                "LZ",
                "SE",
                "BE",
                "AN",
                "EK",
                "KÜ",
                "ZL",
                "AB",
                "ZF",
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
                "ÜB",
            ],
        ),
        (
            {
                "id": 1,
                "characteristic_id": 11,
                "perception_dimension": "int",
                "perception_value": 5,
                "input_dimension": "vis",
                "input_value": 3,
                "processing_dimension": "ref",
                "processing_value": 1,
                "understanding_dimension": "glo",
                "understanding_value": 9,
            },
            [
                "ÜB",
                "LZ",
                "LZ",
                "FO",
                "FO",
                "SE",
                "AN",
                "SE",
                "AN",
                "LZ",
                "FO",
                "KÜ",
                "EK",
            ],
        ),
        (
            None,
            ["ÜB", "FO", "LZ", "SE", "AN", "KÜ", "EK"],
        ),
        # only 1 Learning element is in the list
        # (    None,
        #     ["SE"],
        # ),
        # # only 2 Learning elements are in the list
        # (
        #     None,
        #     ["SE","AN"],
        # ),
        # all learning elements are only once in the list
        (
            None,
            ["ZF", "LZ", "ÜB", "SE", "BE", "AN", "EK", "ZL", "AB", "KÜ", "FO", "RQ"],
        ),
        # all learning elements are only once, except 1 is multiple times in the list
        (
            None,
            [
                "ZF",
                "LZ",
                "ÜB",
                "SE",
                "BE",
                "AN",
                "SE",
                "EK",
                "SE",
                "ZL",
                "AB",
                "KÜ",
                "FO",
                "RQ",
                "SE",
            ],
        ),
        # all learning elements are multiple times in a list
        (
            None,
            [
                "ZF",
                "LZ",
                "ZF",
                "LZ",
                "ÜB",
                "SE",
                "ÜB",
                "SE",
                "BE",
                "AN",
                "BE",
                "AN",
                "EK",
                "ZL",
                "EK",
                "ZL",
                "AB",
                "KÜ",
                "AB",
                "KÜ",
                "FO",
                "RQ",
                "FO",
                "RQ",
            ],
        ),
        # all learning element are in the list, except there is one with an unknown abreviation for example "ZZ"
        (
            None,
            [
                "ZF",
                "LZ",
                "ÜB",
                "SE",
                "BE",
                "AN",
                "SE",
                "EK",
                "SE",
                "ZL",
                "AB",
                "KÜ",
                "FO",
                "RQ",
                "SE",
            ],
        ),
    ],
)
def test_prepare_les_for_ga(learning_style, list_of_keys):
    list_of_les = []
    if learning_style is None:
        learning_style = {
            "id": 1,
            "characteristic_id": 11,
            "perception_dimension": "int",
            "perception_value": 5,
            "input_dimension": "vis",
            "input_value": 3,
            "processing_dimension": "ref",
            "processing_value": 1,
            "understanding_dimension": "glo",
            "understanding_value": 9,
        }

    for i, ele_name in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="ga")
    lp.get_learning_path(
        student_id=1,
        learning_style=learning_style,
        _algorithm="ga",
        list_of_les=list_of_les,
    )
    result = lp.path
    assert isinstance(result, str)
    assert ", " in result
    result = result.split(", ")
    print("result", result)
    assert isinstance(result, list)
    assert result[0] == "KÜ"
    assert result[1] == "EK"
    assert result[-1] == "LZ"


@pytest.mark.parametrize(
    "learning_style",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 15,
                "input_dimension": "vrb",
                "input_value": 20,
                "processing_dimension": "act",
                "processing_value": -50,
                "understanding_dimension": "seq",
                "understanding_value": -13,
            }
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 3,
                "input_dimension": "vrb",
                "input_value": 5,
                "processing_dimension": "act",
                "processing_value": -50,
                "understanding_dimension": "seq",
                "understanding_value": -13,
            }
        ),
    ],
)
def test_with_out_of_range_learning_style_for_ga(learning_style):
    list_of_les = []
    list_of_keys = ["ZF", "KÜ", "SE", "LZ", "ZL", "ÜB", "AB", "EK"]
    for i, ele_name in enumerate(list_of_keys):
        le = DM.LearningElement(
            lms_id=i,
            activity_type="lesson",
            classification=ele_name,
            name="Test LE",
            university="TH-AB",
            created_by="Max Mustermann",
            created_at="2023-09-01",
        )
        list_of_les.append(le.serialize())
    lp = TM.LearningPath(student_id=1, course_id=1, based_on="ga")
    with pytest.raises(err.WrongLearningStyleDimensionError):
        lp.get_learning_path(
            student_id=1,
            learning_style=learning_style,
            _algorithm="ga",
            list_of_les=list_of_les,
        )


@pytest.mark.parametrize(
    "learning_style, error",
    [
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "sns",
                "perception_value": 7,
                "input_dimension": "vrb",
                "input_value": 11,
                "processing_dimension": "act",
                "processing_value": 5,
                "understanding_dimension": "seq",
                "understanding_value": 7,
            },
            None,
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 7,
                "input_dimension": "vis",
                "input_value": 11,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 7,
            },
            None,
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 15,
                "input_dimension": "vis",
                "input_value": 20,
                "processing_dimension": "ref",
                "processing_value": 5,
                "understanding_dimension": "glo",
                "understanding_value": 13,
            },
            "dimension",
        ),
        (
            {
                "id": 1,
                "characteristic_id": 1,
                "perception_dimension": "int",
                "perception_value": 15,
                "input_dimension": "vis",
                "input_value": 20,
                "processing_dimension": "ref",
                "processing_value": 5,
            },
            "number",
        ),
    ],
)
def test_learning_style_check(learning_style, error):
    if error == "dimension":
        with pytest.raises(err.WrongLearningStyleDimensionError):
            utils.check_learning_style(learning_style)
    elif error == "number":
        with pytest.raises(err.WrongLearningStyleNumberError):
            utils.check_learning_style(learning_style)
    else:
        result = utils.check_learning_style(learning_style)
        assert result
