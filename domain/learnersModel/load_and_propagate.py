from .Lib.hugin94.pyhugin94 import (  # type: ignore
    ClassCollection,
    Domain,
    HuginException,
)

FILE_NAME_OOBN = "domain/learnersModel/LearnProfile_cc.oobn"
# FILE_NAME_OOBN = "../../domain/learnersModel/LearnProfile_cc.oobn"


def parse_listener(line, description):
    """A parse listener that prints the line number and error description."""
    # Parse listener for reading the network specification
    print("Parse error line {}: {}".format(line, description))


class OOBN_model:
    def __init__(
        self,
        ils_input_answers,
        ils_perception_answers,
        ils_processing_answers,
        ils_understanding_answers,
    ) -> dict:
        """OOBN class"""
        print("\n\n===Start ILS calculation====")
        ils_answers = {}
        ils_answers["ils_input_answers"] = ils_input_answers
        ils_answers["ils_perception_answers"] = ils_perception_answers
        ils_answers["ils_processing_answers"] = ils_processing_answers
        ils_answers["ils_understanding_answers"] = ils_understanding_answers

        self.self_result_ils_oobn = {}

        self.get_input_answers(ils_answers)
        self.domain_oobn = self.get_domain_oobn()

        # ------------------------------
        self.get_poles(dimension="Visual_verbal")
        result = self.calulated_ils(
            "Visual_verbal", "Score_visual_verbal", "Visual_A_highest"
        )
        self.self_result_ils_oobn["ils_input"] = result

        # ------------------------------
        self.get_poles(dimension="Sensory_Intuitive")
        result = self.calulated_ils(
            "Sensory_Intuitive", "Score_Sensory_Intuitive", "Sensitive_A_highest"
        )
        self.self_result_ils_oobn["ils_perception"] = result

        # ------------------------------
        self.get_poles(dimension="Active_Reflective")
        result = self.calulated_ils(
            "Active_Reflective", "Score_active_reflective", "Active_A_highest"
        )
        self.self_result_ils_oobn["ils_processing"] = result

        # ------------------------------
        self.get_poles(dimension="Sequenz_Global")
        result = self.calulated_ils(
            "Sequenz_Global", "Score_sequenz_Global", "Sequential_A_highest"
        )
        self.self_result_ils_oobn["ils_understanding"] = result
        self.print_version_ils(ils_answers, self.self_result_ils_oobn)
        self.close_model_domain()

    def load_model(self, cc_name, class_name):
        """load an OOBN model into a class collection"""
        # load an OOBN model into a class collection,
        # find the main class, and create a Domain
        # We assume the model is stored in a class collection
        # read model and compile it for inference

        domain = None
        class_by_name = None
        #
        # a class collection holds a collection of classes
        #
        class_collection = ClassCollection()

        try:
            # parse the file specification
            class_collection.parse_classes("{}".format(cc_name), parse_listener)
            # get the main class
            class_by_name = class_collection.get_class_by_name(class_name)

            # we need a Domain object to perform inference
            domain = Domain(class_by_name)

            # we need to compile the model to perform inference
            domain.compile()

        except HuginException:
            print("A Hugin Exception was raised!")
            raise

        return domain

    def process_case_1(self, dom, dimDict, str_local_target, bool_target, poles):
        """Process process_case_1"""
        # case 1: enter evidence, propagate, and
        # print the probability distribution of
        # the target node get handles to evidence node.
        # We use "dot" notation to find a node by name
        # get local targets
        local_targets = []

        # we should test to None pointer, here we take the risk;-)
        local_targets.append(dom.get_node_by_name(str_local_target))  # new

        high_belif = 0.0
        high_score = 0.0

        # print the belief for each learning dimension
        for node in local_targets:
            print(f"{node.get_name ()}")
            for i in range(node.get_number_of_states()):
                # print(
                # f"P({node.get_state_value (i)}|e) =
                # {node.get_belief (i):.2f}")
                if node.get_belief(i) > 0.30 and node.get_belief(i) > high_belif:
                    # print(
                    # f"P({node.get_state_value (i)}|e) =
                    # {node.get_belief(i):.2f}")
                    high_belif = node.get_belief(i)
                    high_score = node.get_state_value(i)

        bool_local_targets = []
        bool_local_targets.append(dom.get_node_by_name(bool_target))

        # print("poles:", poles)
        # print("bool_target:", bool_target)
        pole_of_dim = ""
        for node in bool_local_targets:
            # print(f'{node.get_name ()}')
            for i in range(node.get_number_of_states()):
                # print(f'P({node.get_state_label (i)}|e) =
                # {node.get_belief (i):.2f}')
                if node.get_state_label(i) == "true" and node.get_belief(i):
                    pole_of_dim = poles["pole1"]
                else:
                    pole_of_dim = poles["pole2"]

        # remember to remove any evidence and reset the domain

        print(
            "\nMit eine Probability: ",
            high_belif,
            " ist: ",
            pole_of_dim,
            ":",
            high_score,
        )
        result = {}
        result["dimension"] = pole_of_dim
        result["Value"] = high_score
        result["Probability"] = high_belif
        return result

    def get_input_answers(self, ils_answers):
        """assigne input answers of ILS"""
        self.ils_answers_oobn = {}

        ils_input_answers = self.get_ils_answers(ils_answers["ils_input_answers"])
        ils_perception_answers = self.get_ils_answers(
            ils_answers["ils_perception_answers"]
        )
        ils_processing_answers = self.get_ils_answers(
            ils_answers["ils_processing_answers"]
        )
        ils_understanding_answers = self.get_ils_answers(
            ils_answers["ils_understanding_answers"]
        )

        self.ils_answers_oobn.update(ils_input_answers)
        self.ils_answers_oobn.update(ils_perception_answers)
        self.ils_answers_oobn.update(ils_processing_answers)
        self.ils_answers_oobn.update(ils_understanding_answers)

    def get_poles(self, dimension):
        """assigne poles the answers of ILS"""
        self.poles = {}
        if dimension == "Visual_verbal":
            self.poles["pole1"] = "Visual"
            self.poles["pole2"] = "Verbal"
        if dimension == "Sensory_Intuitive":
            self.poles["pole1"] = "Sensory"
            self.poles["pole2"] = "Intuitive"
        if dimension == "Active_Reflective":
            self.poles["pole1"] = "Active"
            self.poles["pole2"] = "Reflective"
        if dimension == "Sequenz_Global":
            self.poles["pole1"] = "Sequenz"
            self.poles["pole2"] = "Global"

    def get_ils_answers(self, ils_answers):
        """assigne the answers of ILS"""
        ils_answers_oobn = {}
        for id, answer in ils_answers.items():
            if id.startswith("vv"):
                str_vv = id.upper()
                pos = str_vv.split("_")
                str_vv = "ILS" + pos[2] + pos[0] + pos[1]
                str_vv = "Visual_verbal." + str_vv
                ils_answers_oobn[str_vv] = answer

            if id.startswith("si"):
                str_si = id.upper()
                pos = str_si.split("_")
                str_si = "ILS" + pos[2] + pos[0] + pos[1]
                str_si = "Sensory_Intuitive." + str_si
                ils_answers_oobn[str_si] = answer

            if id.startswith("ar"):
                str_ar = id.upper()
                pos = str_ar.split("_")
                str_ar = "ILS" + pos[2] + pos[0] + pos[1]
                str_ar = "Active_Reflective." + str_ar
                ils_answers_oobn[str_ar] = answer

            if id.startswith("sg"):
                str_sg = id.upper()
                pos = str_sg.split("_")
                str_sg = "ILS" + pos[2] + pos[0] + pos[1]
                str_sg = "Sequenz_Global." + str_sg
                ils_answers_oobn[str_sg] = answer
        return ils_answers_oobn

    def get_score_name(self, name_dimension_ils, score_dimension, bool_first_pole):
        """get the name of the Node in OOBN"""
        # ils_answers_oobn with answers 20 ist short version
        if len(self.ils_answers_oobn) > 20:
            str_local_target = name_dimension_ils + "." + score_dimension + "_11"
            bool_local_target = name_dimension_ils + "." + bool_first_pole + "_11"
            print("==Full Version ILS =")
        else:
            str_local_target = name_dimension_ils + "." + score_dimension + "_5"
            bool_local_target = name_dimension_ils + "." + bool_first_pole + "_5"
            print("== Short Version ILS =")

        return str_local_target, bool_local_target

    def get_domain_oobn(self):
        """calculate the answers of ILS"""
        # map input to identifiers
        specfile = FILE_NAME_OOBN
        cls_name = "LearnProfile"
        target_name = "Result"
        try:
            # read model and compile it for inference
            domain = self.load_model(specfile, cls_name)

            # Validierung
            input_boolean_target = domain.get_node_by_name(target_name)
            if input_boolean_target is None:
                print(f"{input_boolean_target} not found")
                exit()
            Dim_dict = self.ils_answers_oobn
            # 1. Enter some evidence
            for name, label in Dim_dict.items():
                node = domain.get_node_by_name(name)
                if node is not None:
                    idx = node.get_state_index_from_label(label)
                    if idx < 0:
                        print(f"{label} not found as state of {name}")
                    else:
                        node.select_state(idx)
                else:
                    print(f"{name} not found")

            # propagate the evidence to compute posterior beliefs
            domain.propagate()
        except HuginException:
            print("A Hugin Exception was raised!")
            raise
        return domain

    def close_model_domain(self):
        """ """
        try:
            # clean up any memory allocations
            self.domain_oobn.initialize()
            self.domain_oobn.delete()
        except HuginException:
            print("A Hugin Exception was raised!")
            raise

    def calulated_ils(self, name_dimension_ils, score_dimension, bool_first_pole):
        """calculate the answers of ILS"""

        target_name = "Result"
        try:
            # get target Booolean Result
            str_local_target, bool_target = self.get_score_name(
                name_dimension_ils, score_dimension, bool_first_pole
            )

            # Validierung
            input_boolean_target = self.domain_oobn.get_node_by_name(target_name)
            if input_boolean_target is None:
                print(f"{input_boolean_target} not found")
                exit()

            dim_dict = self.ils_answers_oobn
            self.domain_oobn.propagate()
            result = self.process_case_1(
                self.domain_oobn,
                dimDict=dim_dict,
                str_local_target=str_local_target,
                bool_target=bool_target,
                poles=self.poles,
            )

        except HuginException:
            print("A Hugin Exception was raised!")
            raise

        # all done
        print("calulated_ils Done1, thank you!:")
        return result

    def print_version_ils(self, ils_answers, self_result_ils_oobn):
        """print_version_ils"""

        for x in self_result_ils_oobn:
            print(x)
            print(self_result_ils_oobn[x])
            # print(x.values())
