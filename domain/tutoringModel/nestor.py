# LIBARIES:
import os
import random

from pgmpy.inference import VariableElimination
from pgmpy.readwrite import XMLBIFReader

from domain.tutoringModel.NestorFolder import nestor_utils
from errors import errors as err
from utils import constants as cons


class Nestor:
    """
    This class is defined to implement the
    CausalNestor algorithm
    """

    def __init__(self):
        """
        All the global values used in Nestor
        are initiated here.
        """
        # random.seed(ran_seed)
        # the following dict maps
        # output variables' states of the
        # trained BN with their respective
        # LE formats which are used in common HASKI.
        # A random seed with unix timestamp is used to choose
        # map LEs, in case of multiple mappings
        self.le_name_map_rgb_to_common_HASKI = {
            "{'CT': 'Yes'}": [cons.abbreviation_fo],
            "{'CT': 'No'}": [cons.abbreviation_fo],
            "{'BO': 'Yes'}": [cons.abbreviation_ct],
            "{'BO': 'No'}": [cons.abbreviation_ct],
            "{'LG': 'Yes'}": [cons.abbreviation_as],
            "{'LG': 'No'}": [cons.abbreviation_as],
            # the manuscript is mapped with three LE from common HASKI
            # so a random weighted selection of this LE is made below
            "{'MS': 'Yes'}": random.choices(
                [cons.abbreviation_co, cons.abbreviation_ra, cons.abbreviation_ex],
                weights=[0.8, 0.1, 0.1],
            ),
            "{'MS': 'No'}": random.choices(
                [cons.abbreviation_co, cons.abbreviation_ra, cons.abbreviation_ex],
                weights=[0.8, 0.1, 0.1],
            ),
            # "{'QU': 'Yes'}": ["RQ", "SE"],
            # "{'QU': 'No'}": ["RQ", "SE"],
            "{'QU': 'Yes'}": [cons.abbreviation_rq],
            "{'QU': 'No'}": [cons.abbreviation_rq],
            "{'EX': 'Yes'}": [cons.abbreviation_ec],
            "{'EX': 'No'}": [cons.abbreviation_ec],
            "{'SU': 'Yes'}": [cons.abbreviation_cc],
            "{'SU': 'No'}": [cons.abbreviation_cc],
            # the additional auditive material states
            # are not mapped to any LE formats
            # "{'AAM': 'Yes'}": [cons.abbreviation_an],
            # "{'AAM': 'No'}": [cons.abbreviation_an],
            "{'VAM': 'Yes'}": [cons.abbreviation_an],
            "{'VAM': 'No'}": [cons.abbreviation_an],
            "{'TAM': 'Yes'}": [cons.abbreviation_rm],
            "{'TAM': 'No'}": [cons.abbreviation_rm],
        }

        # the following are the LE formats used in Nestor Inference
        self.rgb_le_variables = [
            "CT",
            "BO",
            "LG",
            "MS",
            "QU",
            "EX",
            "SU",
            "AAM",
            "VAM",
            "TAM",
        ]
        # this dict maps FSLSM model learning style nomenclature
        # used in HASKI to nomenclature
        # used in trained Nestor.
        self.ls_map_common_HASKI_to_nestor = {
            "act": "Active",
            "ref": "Reflective",
            "sns": "Sensory",
            "int": "Intuitive",
            "vis": "Visual",
            "vrb": "Verbal",
            "seq": "Sequential",
            "glo": "Global",
        }

    def get_learning_path(
        self,
        input_learning_style: dict,
        input_learning_elements: list,
        path_to_model=os.path.join(
            "domain", "tutoringModel", "NestorFolder", "backup_saved_model.xml"
        ),
    ):
        """
        This function reads in pre-processed information
        of learner
        to recommend personalized learning paths
        """
        # random.seed(ran_seed)
        # defining the path to saved BN
        # path_to_model = path_to_model
        # The HASKI Gemeninsam uses the Learning styles naming convention of
        # act, ref, sen, int, vis, vrb, seq, glo.
        # The Nesor uses a naming convention of
        # Active, Reflective, Sensory, Intuitive,
        # Visual, Verbal, Sequential, Global
        # First it is checked if the input learning style is
        # empty or no to raise errors
        # The dictionary defined in constants file is used
        # to to map this naming convention and
        # set evidence to Nestor.
        if not input_learning_style:
            raise err.MissingParameterError()
        else:
            evidence_for_inference = {
                "Active_Reflective_Dim": self.ls_map_common_HASKI_to_nestor[
                    input_learning_style["processing_dimension"]
                ],
                "Sensory_Intuitive_Dim": self.ls_map_common_HASKI_to_nestor[
                    input_learning_style["perception_dimension"]
                ],
                "Visual_Verbal_Dim": self.ls_map_common_HASKI_to_nestor[
                    input_learning_style["input_dimension"]
                ],
                "Sequential_Gloabl_Dim": self.ls_map_common_HASKI_to_nestor[
                    input_learning_style["understanding_dimension"]
                ],
            }
        # local variables for nestor inference
        le_max_dict = {}
        # updating the LE names with tags used in common HASKI
        le_renamed_dict = {}
        # the following list is used to store LE formats from
        le_format_no_duplicates = []
        # In mapping HASKI LEs with RGB LEs,
        # more than one HASKI LEs are mapped to a few RGB LEs
        # The union of non-duplicated HASKI LEs and RGB LEs,
        # are recommended with highest prob. first,
        # and least at the end as final learning path
        le_path = []
        # post processing the learning path to a sting
        output_string = ""
        # Inference Start
        # preparing the learning elements
        # the input param for LEs is a list of LEs (Learning path)
        # Each LE in learning path is a dict. and
        # the "classification" key returns the format of LE
        # first, if input learning element is an empty value
        # throw an error
        if not input_learning_elements:
            raise err.NoValidParameterValueError()
        else:
            le_format_no_duplicates = list(
                set(ele["classification"] for ele in input_learning_elements)
            )

        # start inference with BN
        bn = XMLBIFReader(path_to_model).get_model()
        le_infer = VariableElimination(bn)

        for le_var in self.rgb_le_variables:
            # Query both LE format and probability values
            query_map = le_infer.map_query(
                variables=[le_var], evidence=evidence_for_inference, show_progress=False
            )
            le_max_dict[str(query_map)] = str(
                le_infer.max_marginal(
                    variables=[le_var],
                    evidence=evidence_for_inference,
                    show_progress=False,
                )
            )

        # The RGB LEs AAM and VAM are mapped with Animation.
        # 70% of times, AN is VAM and 30% of times AN is AAM
        # Removing the AAM from recommending since it has
        # no mapping with HASKI common LEs.
        # Workflow as follows:
        # if both AAM and VAM are present in the le_max dict:
        # 70% of times remove AAM and 30% of times remove VAM
        if str({"VAM": "Yes"}) in le_max_dict:
            # If VAM is present or VAM and AAM are present,
            # remove AAM with 30% probability
            ele_to_remove = random.choices(
                [str({"VAM": "Yes"}), str({"AAM": "No"})], weights=[0.7, 0.3]
            )
            remove_key = str(ele_to_remove[0])
            try:
                le_max_dict.pop(remove_key)
            except KeyError:
                le_max_dict.update({remove_key: le_max_dict.pop(str({"VAM": "Yes"}))})

        # here the dictionary contains inference with both yes and no
        # The LEs with state 'No' is not removed but
        # probability for state to be 'yes' is calculated
        le_max_dict = {
            key: str(round(1 - float(val), 1)) if "No" in key else val
            for key, val in le_max_dict.items()
        }
        # soring LEs in descending order, randomizing same value LEs
        le_max_dict = nestor_utils.randomize_same_values(le_max_dict)
        # Get items from the input_dict and
        # sort them based on the numerical values in descending order
        sorted_items = sorted(
            le_max_dict.items(), key=lambda item: float(item[1]), reverse=True
        )
        # Iterate through the sorted items and populate the sorted_dict
        for key, value in sorted_items:
            updated_key = random.choice(
                self.le_name_map_rgb_to_common_HASKI.get(key, [key])
            )
            le_renamed_dict[updated_key] = value

        le_renamed = list(le_renamed_dict.keys())

        for ele in le_renamed:
            if ele in le_format_no_duplicates:
                le_path.append(ele)

        output_string = ", ".join(le_path)

        return output_string
