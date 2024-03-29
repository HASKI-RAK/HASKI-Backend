import os

import pandas as pd
from pgmpy.factors.discrete import TabularCPD

from domain.tutoringModel.NestorFolder.nestor_utils import categorize_lisk_bfi

# VARIABLES START
le_max_dict = {}
le_max_prob_val = []
yes_keys = []

columns_to_encode = [
    "ks",
    "mks",
    "smir",
    "smer",
    "bfie",
    "bfin",
    "bfio",
    "bfic",
    "bfia",
]

# path tp the csv file with sample data
df_data = pd.read_csv(
    os.path.join("domain", "tutoringModel", "NestorFolder", "fakeTrainData.csv")
)

# path to save the BN after training
path_to_trainedmodel = os.path.join(
    "domain", "tutoringModel", "NestorFolder", "fake_saved_model.xml"
)

# encoding the BFI and LISTK columns to Likert scale
df_data_categories = categorize_lisk_bfi(
    input_dataframe=df_data, encoding_columns=columns_to_encode
)


# Start - Variables required for training BN
edges_list_only_psy_models = [
    ("Active_Reflective_Dim", "bfio"),
    ("Active_Reflective_Dim", "bfie"),
    ("Active_Reflective_Dim", "ks"),
    ("Active_Reflective_Dim", "smer"),
    ("Visual_Verbal_Dim", "bfin"),
    ("Sequential_Gloabl_Dim", "mks"),
    ("Sensory_Intuitive_Dim", "bfio"),
    ("Sensory_Intuitive_Dim", "ks"),
    ("bfio", "smer"),
    ("bfia", "smer"),
    ("bfic", "ks"),
    ("bfic", "smir"),
    ("bfie", "bfin"),
    ("bfie", "smer"),
    ("bfin", "ks"),
    ("ks", "mks"),
    ("bfic", "smer"),
    ("bfie", "smer"),
    ("bfic", "smir"),
    ("smir", "smer"),
]

state_names_bn_training_psy_model = {
    "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
    "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
    "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
    "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    "bfie": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "bfin": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "bfio": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "bfic": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "bfia": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "ks": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "mks": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "smir": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
    "smer": [
        "strong_disagree",
        "disagree",
        "neither_agree_disagree",
        "agree",
        "strong_agree",
    ],
}

edges_list_active_reflective = [
    ("Active_Reflective_Dim", "CT"),
    ("Active_Reflective_Dim", "BO"),
    ("Active_Reflective_Dim", "LG"),
    ("Active_Reflective_Dim", "MS"),
    ("Active_Reflective_Dim", "QU"),
    ("Active_Reflective_Dim", "EX"),
    ("Active_Reflective_Dim", "SU"),
    ("Active_Reflective_Dim", "AAM"),
    ("Active_Reflective_Dim", "TAM"),
    ("Active_Reflective_Dim", "VAM"),
]

edges_list_sensory_intuitive = [
    ("Sensory_Intuitive_Dim", "CT"),
    ("Sensory_Intuitive_Dim", "BO"),
    ("Sensory_Intuitive_Dim", "LG"),
    ("Sensory_Intuitive_Dim", "MS"),
    ("Sensory_Intuitive_Dim", "QU"),
    ("Sensory_Intuitive_Dim", "EX"),
    ("Sensory_Intuitive_Dim", "AAM"),
    ("Sensory_Intuitive_Dim", "TAM"),
    ("Sensory_Intuitive_Dim", "VAM"),
]

edges_list_visual_verbal = [
    ("Visual_Verbal_Dim", "CT"),
    ("Visual_Verbal_Dim", "BO"),
    ("Visual_Verbal_Dim", "LG"),
    ("Visual_Verbal_Dim", "MS"),
    ("Visual_Verbal_Dim", "QU"),
    ("Visual_Verbal_Dim", "EX"),
    ("Visual_Verbal_Dim", "AAM"),
    ("Visual_Verbal_Dim", "TAM"),
    ("Visual_Verbal_Dim", "VAM"),
]

edges_list_sequential_global = [
    ("Sequential_Gloabl_Dim", "CT"),
    ("Sequential_Gloabl_Dim", "BO"),
    ("Sequential_Gloabl_Dim", "MS"),
    ("Sequential_Gloabl_Dim", "QU"),
    ("Sequential_Gloabl_Dim", "EX"),
    ("Sequential_Gloabl_Dim", "SU"),
    ("Sequential_Gloabl_Dim", "AAM"),
    ("Sequential_Gloabl_Dim", "TAM"),
    ("Sequential_Gloabl_Dim", "VAM"),
]

cpd_param_CT = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "state_names": {
        "CT": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_BO = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ],
        [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ],
    ],
    "state_names": {
        "BO": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_LG = {
    "evidence": ["Active_Reflective_Dim", "Sensory_Intuitive_Dim", "Visual_Verbal_Dim"],
    "values": [
        [0.67, 0.33, 0.33, 0, 1, 0.67, 0.67, 0.33],
        [0.33, 0.67, 0.67, 1, 0, 0.33, 0.33, 0.67],
    ],
    "state_names": {
        "LG": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
    },
}

cpd_param_MS = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ],
        [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ],
    ],
    "state_names": {
        "MS": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}


cpd_param_QU = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.5,
            0.33,
            0.67,
            0.5,
            0.5,
            0.33,
            0.67,
            0.5,
            0.5,
            0.33,
            0.67,
            0.5,
            0.5,
            0.33,
            0.67,
            0.5,
        ],
        [
            0.5,
            0.67,
            0.33,
            0.5,
            0.5,
            0.67,
            0.33,
            0.5,
            0.5,
            0.67,
            0.33,
            0.5,
            0.5,
            0.67,
            0.33,
            0.5,
        ],
    ],
    "state_names": {
        "QU": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_EX = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.2,
            0.4,
            0.4,
            0.6,
            0.4,
            0.5,
            0.6,
            0.8,
            0.2,
            0.4,
            0.4,
            0.6,
            0.4,
            0.6,
            0.6,
            0.8,
        ],
        [
            0.8,
            0.6,
            0.6,
            0.4,
            0.6,
            0.5,
            0.4,
            0.2,
            0.8,
            0.6,
            0.6,
            0.4,
            0.6,
            0.4,
            0.4,
            0.2,
        ],
    ],
    "state_names": {
        "EX": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_SU = {
    "evidence": ["Active_Reflective_Dim", "Sequential_Gloabl_Dim"],
    "values": [[0.5, 0, 1, 0.5], [0.5, 1, 0, 0.5]],
    "state_names": {
        "SU": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_AAM = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.5,
            0.5,
            0.2,
            0.2,
            0.5,
            0.5,
            0.2,
            0.2,
            0.67,
            0.67,
            0.5,
            0.5,
            0.67,
            0.67,
            0.5,
            0.5,
        ],
        [
            0.5,
            0.5,
            0.8,
            0.8,
            0.5,
            0.5,
            0.8,
            0.8,
            0.33,
            0.33,
            0.5,
            0.5,
            0.33,
            0.33,
            0.5,
            0.5,
        ],
    ],
    "state_names": {
        "AAM": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_TAM = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.5,
            0.5,
            0.2,
            0.2,
            0.5,
            0.5,
            0.2,
            0.2,
            0.67,
            0.67,
            0.5,
            0.5,
            0.67,
            0.67,
            0.5,
            0.5,
        ],
        [
            0.5,
            0.5,
            0.8,
            0.8,
            0.5,
            0.5,
            0.8,
            0.8,
            0.33,
            0.33,
            0.5,
            0.5,
            0.33,
            0.33,
            0.5,
            0.5,
        ],
    ],
    "state_names": {
        "TAM": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

cpd_param_VAM = {
    "evidence": [
        "Active_Reflective_Dim",
        "Sensory_Intuitive_Dim",
        "Visual_Verbal_Dim",
        "Sequential_Gloabl_Dim",
    ],
    "values": [
        [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ],
        [
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ],
    ],
    "state_names": {
        "VAM": ["Yes", "No"],
        "Active_Reflective_Dim": list(df_data["Active_Reflective_Dim"].unique()),
        "Sensory_Intuitive_Dim": list(df_data["Sensory_Intuitive_Dim"].unique()),
        "Visual_Verbal_Dim": list(df_data["Visual_Verbal_Dim"].unique()),
        "Sequential_Gloabl_Dim": list(df_data["Sequential_Gloabl_Dim"].unique()),
    },
}

evidence_for_inference = {
    "Active_Reflective_Dim": "Reflective",
    "Sensory_Intuitive_Dim": "Sensory",
    "Visual_Verbal_Dim": "Visual",
    "Sequential_Gloabl_Dim": "Global",
}
le_max_dict = {}
updated_le_max_dict = {}
le_variables = ["CT", "BO", "LG", "MS", "QU", "EX", "SU", "AAM", "VAM", "TAM"]

# Adding CPDs/parameters to extended structure
cpd_ct = TabularCPD(
    variable="CT",
    variable_card=2,
    values=cpd_param_CT["values"],
    evidence=cpd_param_CT["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_CT["state_names"],
)

cpd_bo = TabularCPD(
    variable="BO",
    variable_card=2,
    values=cpd_param_BO["values"],
    evidence=cpd_param_BO["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_BO["state_names"],
)

cpd_lg = TabularCPD(
    variable="LG",
    variable_card=2,
    values=cpd_param_LG["values"],
    evidence=cpd_param_LG["evidence"],
    evidence_card=[2, 2, 2],
    state_names=cpd_param_LG["state_names"],
)

cpd_ms = TabularCPD(
    variable="MS",
    variable_card=2,
    values=cpd_param_MS["values"],
    evidence=cpd_param_MS["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_MS["state_names"],
)

cpd_qu = TabularCPD(
    variable="QU",
    variable_card=2,
    values=cpd_param_QU["values"],
    evidence=cpd_param_QU["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_QU["state_names"],
)

cpd_ex = TabularCPD(
    variable="EX",
    variable_card=2,
    values=cpd_param_EX["values"],
    evidence=cpd_param_EX["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_EX["state_names"],
)

cpd_su = TabularCPD(
    variable="SU",
    variable_card=2,
    values=cpd_param_SU["values"],
    evidence=cpd_param_SU["evidence"],
    evidence_card=[2, 2],
    state_names=cpd_param_SU["state_names"],
)

cpd_aam = TabularCPD(
    variable="AAM",
    variable_card=2,
    values=cpd_param_AAM["values"],
    evidence=cpd_param_AAM["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_AAM["state_names"],
)

cpd_tam = TabularCPD(
    variable="TAM",
    variable_card=2,
    values=cpd_param_TAM["values"],
    evidence=cpd_param_TAM["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_TAM["state_names"],
)

cpd_vam = TabularCPD(
    variable="VAM",
    variable_card=2,
    values=cpd_param_VAM["values"],
    evidence=cpd_param_VAM["evidence"],
    evidence_card=[2, 2, 2, 2],
    state_names=cpd_param_VAM["state_names"],
)
