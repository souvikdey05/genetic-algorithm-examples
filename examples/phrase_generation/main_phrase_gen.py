import json
import os
from utils.logger import create_logger, get_logger

from .population import Population_PhraseGeneration

class Phrase_Generation:
    r"""Main class for Phrase generation example"""

    def __init__(self, population_size=20, mutation_rate=0.0, target_phrase=None, max_generations=None, score_file=None):
        
        self._population_size = population_size
        self._mutation_rate = mutation_rate
        self._target_phrase = target_phrase
        self._max_generations = max_generations
        
        self._population = Population_PhraseGeneration(self._population_size, self._mutation_rate, target_phrase, self._max_generations, score_file)
        

    def run(self):
        r"""Method to run the generations and solve the problem"""
        self._population.run()
    
    @staticmethod
    def main(config_file, output_path):
        config = json.load(open(config_file))

        log_file = os.path.join(output_path, "log.txt")
        if os.path.exists(log_file):
            os.remove(log_file)

        create_logger("Phrase Generation Logger", log_file)
        logger = get_logger()

        # delete all the files from scores folder
        scores_path = os.path.join(output_path, "scores")
        filelist = [ f for f in os.listdir(scores_path)]
        for f in filelist:
            os.remove(os.path.join(scores_path, f))

        # Some validity checks
        target_phrase = None
        if "target_phrase" not in config or config["target_phrase"] is None:
            logger.error("You need to specify the target phrase to solve in config file")
            raise Exception("You need to specify the target phrase to solve in config file")
        else:
            target_phrase = config["target_phrase"]
            logger.info(f"Target Phrase = {target_phrase}")

        population_size = 20
        if "population_size" in config and config["population_size"] is not None:
            population_size = config["population_size"]
        logger.info(f"Population size = {population_size}")

        mutation_rate = 0.0
        if "mutation_rate" in config and config["mutation_rate"] is not None:
            if not 0.0 <= mutation_rate <= 1.0:
                logger.error("Mutation rate is probability value. It should be [0, 1]")
                raise Exception("Mutation rate is probability value. It should be [0, 1]")
            mutation_rate = config["mutation_rate"]
        logger.info(f"Mutation Rate = {mutation_rate}")

        max_generations = 5000
        if "max_generations" in config and config["max_generations"] is not None:
            max_generations = config["max_generations"]
        logger.info(f"Max Generations Possible = {max_generations}")

        num_of_iterations = 1
        if "num_of_iterations" in config and config["num_of_iterations"] is not None:
            num_of_iterations = config["num_of_iterations"]
        logger.info(f"Number of Iterations = {num_of_iterations}")


        for itr in range(num_of_iterations):
            logger.info(f"Run Number = {itr + 1} ->")
            logger.info(f"------------------------------")
            
            scores_file = os.path.join(scores_path, f"score_{itr + 1}.csv")
            obj = Phrase_Generation(population_size, mutation_rate, target_phrase, max_generations, score_file=scores_file)
            obj.run()
        