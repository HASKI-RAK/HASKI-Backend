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
    """OOBN class"""

    def __init__(
        self,
        ils_input_answers,
        ils_perception_answers,
        ils_processing_answers,
        ils_understanding_answers,
    ):
        """OOBN class"""
        self.self_result_ils_oobn = {}
        self.poles = {}
        print()

        print(ils_input_answers)
        print(ils_perception_answers)
        print(ils_processing_answers)
        print(ils_understanding_answers)
        print()
        self.ils_answers_oobn = self.merge_all_answers_ils(
            ils_input_answers,
            ils_perception_answers,
            ils_processing_answers,
            ils_understanding_answers,
        )
        self.domain_oobn = self.give_all_answers_to_the_model_oobn()  # Dict
        self.calculate_oobn_for_all_dimensions()

        self.print_version_ils(self.self_result_ils_oobn)
        self.close_model_domain()
        print(self.self_result_ils_oobn)

    def merge_all_answers_ils(
        self,
        ils_input_answers,
        ils_perception_answers,
        ils_processing_answers,
        ils_understanding_answers,
    ):
        """Merge all ils responses into a single variable"""
        ils_answers_oobn = {}
        print("merge_all_answers_ils entro -----")

        ils_input_answers = self.get_correct_name_of_the_nodes(ils_input_answers)
        ils_perception_answers = self.get_correct_name_of_the_nodes(
            ils_perception_answers
        )
        ils_processing_answers = self.get_correct_name_of_the_nodes(
            ils_processing_answers
        )
        ils_understanding_answers = self.get_correct_name_of_the_nodes(
            ils_understanding_answers
        )
        ils_answers_oobn.update(ils_input_answers)
        ils_answers_oobn.update(ils_perception_answers)
        ils_answers_oobn.update(ils_processing_answers)
        ils_answers_oobn.update(ils_understanding_answers)
        return ils_answers_oobn

    def get_correct_name_of_the_nodes(self, ils_answers):
        """This function is used to get the correct name
        of the nodes in the oobn in order to give them
        the value of the students' answers."""
        print("get_correct_name_of_the_nodes entro -----")
        ils_answers_oobn = {}
        dimension_name = ""

        for key, answer in ils_answers.items():
            str_key = key.upper()
            pos = str_key.split("_")
            question_name = "ILS" + pos[2] + pos[0] + pos[1]

            if key.startswith("vv"):
                dimension_name = "Visual_verbal." + question_name
            elif key.startswith("si"):
                dimension_name = "Sensory_Intuitive." + question_name
            elif key.startswith("ar"):
                dimension_name = "Active_Reflective." + question_name
            elif key.startswith("sg"):
                dimension_name = "Sequenz_Global." + question_name

            ils_answers_oobn[dimension_name] = answer

        return ils_answers_oobn

    def give_all_answers_to_the_model_oobn(self):
        """calculate the answers of ILS"""
        # map input to identifiers
        try:
            # read model and compile it for inference
            domain = self.load_model_oobn(FILE_NAME_OOBN, "LearnProfile")
            print("Model OOBN loaded!! entro----")
            # Validierung
            input_boolean_target = domain.get_node_by_name("Result")

            if input_boolean_target is None:
                print(f"{input_boolean_target} not found")
                exit()
            else:
                # 1. Enter some evidence
                for name, label in self.ils_answers_oobn.items():
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
            print("A Hugin Exception was raised in give_all_answers!")
            raise
        return domain

    def load_model_oobn(self, cc_name, class_name):
        """load an OOBN model into a class collection"""
        # load an OOBN model into a class collection,
        # find the main class, and create a Domain
        # We assume the model is stored in a class collection
        # read model and compile it for inference

        # domain object to perform inference
        domain = None
        class_by_name = None
        print("load_model_oobn entro -----")
        # a class collection holds a collection of classes
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
            print("A Hugin Exception was raised in load_model_oobn!")
            raise

        return domain

    def process_case_1(self, str_local_target, bool_target):
        """Process process_case_1"""
        # case 1: enter evidence, propagate, and
        # print the probability distribution of
        # the target node get handles to evidence node.
        # We use "dot" notation to find a node by name
        # get local targets
        local_targets = []
        bool_local_targets = []
        high_belif = 0.0
        high_score = 0.0
        print("process_case_1 entro-----")
        # we should test to None pointer, here we take the risk;-)
        local_targets.append(self.domain_oobn.get_node_by_name(str_local_target))

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

        bool_local_targets.append(self.domain_oobn.get_node_by_name(bool_target))

        # print("poles:", poles)
        # print("bool_target:", bool_target)
        pole_of_dim = ""
        for node in bool_local_targets:
            # print(f'{node.get_name ()}')
            for i in range(node.get_number_of_states()):
                # print(f'P({node.get_state_label (i)}|e) =
                # {node.get_belief (i):.2f}')
                if node.get_state_label(i) == "true" and node.get_belief(i):
                    pole_of_dim = self.poles["pole1"]
                else:
                    pole_of_dim = self.poles["pole2"]

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
        print("Result", result)
        return result

    def get_poles(self, dimension):
        """return the poles of a given dimension"""
        print("get_poles entro-----")
        poles = {
            "Visual_verbal": ["Visual", "Verbal"],
            "Sensory_Intuitive": ["Sensory", "Intuitive"],
            "Active_Reflective": ["Active", "Reflective"],
            "Sequenz_Global": ["Sequenz", "Global"],
        }

        if dimension in poles:
            self.poles["pole1"], self.poles["pole2"] = poles[dimension]
        print("Answer OOBN")

    def get_score_node_name(self, name_dimension_ils, score_dimension, bool_first_pole):
        """get the name of the Node in OOBN"""
        # ils_answers_oobn with answers 20 ist short version
        print("get_score_node_name entro-----")
        version = ""
        if len(self.ils_answers_oobn) > 20:
            version = "_11"
            print("==Full Version ILS =")
        else:
            version = "_5"
            print("== Short Version ILS =")

        str_local_target = name_dimension_ils + "." + score_dimension + version
        bool_local_target = name_dimension_ils + "." + bool_first_pole + version

        return str_local_target, bool_local_target

    def calculate_answers_of_ils(
        self, name_dimension_ils, score_dimension, bool_first_pole
    ):
        """calculate the answers of ILS"""
        self.get_poles(dimension=name_dimension_ils)
        print("calculate_answers_of_ils entro-----")

        try:
            # Validierung
            input_boolean_target = self.domain_oobn.get_node_by_name("Result")

            if input_boolean_target is None:
                print(f"{input_boolean_target} not found")
                exit()

            # get target Booolean Result
            str_local_target, bool_target = self.get_score_node_name(
                name_dimension_ils, score_dimension, bool_first_pole
            )

            self.domain_oobn.propagate()

            result = self.process_case_1(
                str_local_target=str_local_target, bool_target=bool_target
            )
            print("process_case_1", result)

        except HuginException:
            print("A Hugin Exception was raised calculate_answers_of_ils!")
            raise

        # all done
        print("calculate_answers_of_ils Done1, thank you!:")
        return result

    def calculate_oobn_for_all_dimensions(self):
        """calculate_oobn_for_all_dimensions"""
        print("calculate_oobn_for_all_dimensions--------")

        self.self_result_ils_oobn["ils_input"] = self.calculate_answers_of_ils(
            "Visual_verbal", "Score_visual_verbal", "Visual_A_highest"
        )

        self.self_result_ils_oobn["ils_perception"] = self.calculate_answers_of_ils(
            "Sensory_Intuitive", "Score_Sensory_Intuitive", "Sensitive_A_highest"
        )

        self.self_result_ils_oobn["ils_processing"] = self.calculate_answers_of_ils(
            "Active_Reflective", "Score_active_reflective", "Active_A_highest"
        )

        self.self_result_ils_oobn["ils_understanding"] = self.calculate_answers_of_ils(
            "Sequenz_Global", "Score_sequenz_Global", "Sequential_A_highest"
        )

    def close_model_domain(self):
        """close_model_domain"""
        try:
            # clean up any memory allocations
            self.domain_oobn.initialize()
            self.domain_oobn.delete()
        except HuginException:
            print("A Hugin Exception was raised close_model_domain!")
            raise

    def print_version_ils(self, self_result_ils_oobn):
        """print_version_ils"""

        for x in self_result_ils_oobn:
            print(x)
            print(self_result_ils_oobn[x])
            # print(x.values())

    def get_result(self):
        return self.self_result_ils_oobn
