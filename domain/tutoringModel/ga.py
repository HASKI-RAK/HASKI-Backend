import numpy as np

import errors.errors as err
from domain.tutoringModel import utils


class GeneticAlgorithm:
    """The Genetic Algorithm class simulates the process of natural
    selection using methods of evolutionary selection,
    combination and variation of individuals (Learning path)."""

    # learning path sequencing problem will be considered as
    # a Traveling Salesman Problem (TSP) and the Learning Style
    # of the Student is used for creating Personalized and
    # adaptive learning paths.

    def __init__(
        self,
        learning_elements=None,
    ):
        self.learning_elements = learning_elements
        self.learning_style = {}
        self.best_population = []
        self.le_coordinate: np.ndarray = np.array([])
        self.population: np.ndarray = np.array([])
        self.n_generation = 100
        self.le_size = 0
        self.mutate_rate = 0.4
        self.cross_rate = 0.9
        self.pop_size = 100

        if learning_elements is not None:
            #  convert learning element into
            #  a list with the short name of learning element
            le = utils.get_learning_element(learning_elements)
            self.le_size = len(le)

    def create_random_population(self, learning_style) -> None:
        """Function for the calculation of the score.
        position a also Initialise some populations
        with Clustering if this is possible.
        param dict_coordinates"""

        coordinates = utils.get_coordinates(learning_style, self.learning_elements)
        self.dict_coordinate = {"first": (20, 20, 20, 20)}
        self.dict_coordinate.update(coordinates)

        self.le_coordinate = np.array(list(self.dict_coordinate.values()))
        self.learning_elements = np.array(list(self.dict_coordinate.keys()))

        self.le_size = len(self.learning_elements)

        # learning_elements sorted by the x-coordinate of the first learning element
        idx = np.argsort(self.le_coordinate[:, 0])
        idx = np.flip(idx, axis=0)
        self.le_coordinate = self.le_coordinate[idx]
        self.learning_elements = self.learning_elements[idx]
        self.population = utils.permutation_generator(self.le_size, self.pop_size)

    def valide_population(self):
        """Function to add validation: First Learning Element is fixed
        in the Learning path."""

        col_zeros = np.zeros((self.pop_size, 1), dtype=int)
        new_pop = np.concatenate(
            (col_zeros, self.population[:, 0 : self.le_size]), axis=1
        )
        return new_pop

    def get_lines_paths(self, new_pop):
        """This function extract all the positions X,Y,Z,K.
        in the space of the generated trajectories"""
        le_coord = self.le_coordinate[new_pop]
        line_x, line_y, line_z, line_k = (
            le_coord[:, :, 0],
            le_coord[:, :, 1],
            le_coord[:, :, 2],
            le_coord[:, :, 3],
        )
        return (line_x, line_y, line_z, line_k)

    def get_fitness(self, line_x, line_y, line_z, line_k):
        """Function to calculate the fitness function for GA"""
        # a score is evaluated for each individual, which is
        # calculated using the fitness function: dtype=np.float64)
        total_sum = (
            np.square(np.diff(line_x))
            + np.square(np.diff(line_y))
            + np.square(np.diff(line_z))
            + np.square(np.diff(line_k))
        )
        fitness = np.sum(np.sqrt(total_sum), 1)
        return fitness

    def crossover(self, parent, pop):
        """Function for the calculation of crossovers between
        each individual."""
        # two parents are randomly selected from the population,
        # to inherit a part of their solution to their child.

        if utils.rng.random() < self.cross_rate:
            samples = 2
            i_ = utils.random_generator(samples, size=1, type_="int")
            # choose crossover learning elements
            temp = self.le_size - 1
            cross_points = utils.random_generator(2, size=temp, type_="bool")
            keep_le = parent[~cross_points]
            swap_le = pop[i_, np.isin(pop[i_].ravel(), keep_le, invert=True)]
            parent = np.concatenate((keep_le, swap_le))
        return parent

    def mutate(self, child):
        """To prevent all offspring of a new generation
        from having the same approximation, a percentage
        probability is set at which an offspring will receive
        a mutation"""
        temp = 0
        if self.le_size > 2:
            temp = self.le_size - 2
        for point in range(temp):
            if utils.rng.random() < self.mutate_rate:
                swap_point = utils.random_generator(2, temp, "int")
                swap_a, swap_b = child[point], child[swap_point]
                child[point], child[swap_point] = swap_b, swap_a
        return child

    def evolve(self, fitness, best_sample) -> None:
        """In the selection phase, after knowing
        the aptitude of each individual, those that will be selected
        of each individual, those that are
        most suitable to evolve will be selected."""
        best_samples = 5
        if self.pop_size > 50:
            self.population[20:25, :] = best_sample

        idx = np.argsort(fitness)
        population = self.population[idx]

        pop_copy = population.copy()
        for parent in population:
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.population[best_samples:] = population[:-best_samples].copy()

    def calculate_learning_path_ga(self):
        """This function calculates the learning path with Genetic algorithm"""
        best_total_score = 300

        for i in range(self.n_generation):
            new_pop = self.valide_population()
            lx, ly, lz, lk = self.get_lines_paths(new_pop)
            fitness = self.get_fitness(lx, ly, lz, lk)

            # sort population
            best_index = np.argsort(fitness)
            fitness = fitness[best_index]
            best_score = fitness[0]

            # update population
            new_pop = self.population[best_index]
            self.population = new_pop
            best_sample = new_pop[0]

            if best_score < best_total_score and i < self.n_generation:
                best_total_score = best_score
                self.best_population = best_sample

            # evolution
            self.evolve(fitness, best_sample)

        population = self.valide_population()
        idx = population[0]

        # sort the learning elements
        self.learning_elements = self.learning_elements[idx]
        self.le_coordinate = self.le_coordinate[idx]

        # eliminate the first elements
        self.learning_elements = self.learning_elements[1:]

        learning_path_as_str = ", ".join(self.learning_elements)
        if len(self.learning_elements) == 1:
            learning_path_as_str = self.learning_elements[0] + ", "

        return learning_path_as_str

    def get_learning_style(self, learning_style):
        """Convert the dictionary into another format
        with the dimension and value for Genetic algorithm"""
        new_learning_style = {}
        str_processing = learning_style.get("processing_dimension")
        value_processing = learning_style.get("processing_value")
        new_learning_style[str_processing] = value_processing

        str_perception = learning_style.get("perception_dimension")
        value_perception = learning_style.get("perception_value")
        new_learning_style[str_perception] = value_perception

        str_input = learning_style.get("input_dimension")
        value_input = learning_style.get("input_value")
        new_learning_style[str_input] = value_input

        str_understanding = learning_style.get("understanding_dimension")
        value_understanding = learning_style.get("understanding_value")
        new_learning_style[str_understanding] = value_understanding

        for key, value in dict(new_learning_style).items():
            if value is None:
                del new_learning_style[key]
        return new_learning_style

    def check_learning_style(self, input_learning_style):
        """Checks if the learning styles
        have values between 0 and 11"""
        for iterator in input_learning_style:
            if input_learning_style.get(iterator):
                dimension_number = input_learning_style.get(iterator)
                if dimension_number < -11 or dimension_number > 11:
                    return False

        return True

    def check_name_learning_style(self, input_learning_style):
        """Check if the names of learning styles are correct."""
        pairs = [
            {"act", "ref"},
            {"sns", "int"},
            {"vis", "vrb"},
            {"seq", "glo"},
        ]
        return any(
            [
                True if set(pair).issubset(input_learning_style) else False
                for pair in pairs
            ]
        )

    def get_learning_path(self, input_learning_style=None, input_learning_element=None):
        """calculates and verifies the learning path the genetic algorithm"""

        result_ga = []
        if input_learning_style is None:
            raise err.MissingParameterError()
        else:
            learning_style = self.get_learning_style(input_learning_style)
            # Wrong  Number input_learning_style
            if len(learning_style) != 4:
                raise err.WrongLearningStyleNumberError()

            if not self.check_learning_style(learning_style):
                # Wrong  Dimension input_learning_style
                raise err.WrongLearningStyleDimensionError()

        if input_learning_element is None:
            raise err.NoValidParameterValueError()
        else:
            self.learning_elements = utils.get_learning_element(input_learning_element)

        if len(self.learning_elements) == 0:
            raise err.NoValidParameterValueError()

        if len(self.learning_elements) == 1:
            return self.learning_elements[0]

        self.create_random_population(input_learning_style)
        result_ga = self.calculate_learning_path_ga()
        return result_ga
