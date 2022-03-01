import json
import os
from turtle import width
from xml.etree.ElementPath import get_parent_map
from tqdm import tqdm
import pygame
from pathlib import Path
import random
from utils.logger import create_logger, get_logger
from .population import Population_TSP
from math import inf
import csv

class TSP:
    r"""Main class for TSP example"""
    logger = None

    def __init__(self, num_of_cities=5, num_of_iterations=100,
                    population_size=20, mutation_rate=0.0, max_generations=None, scores_path=None):
        self._num_of_cities = num_of_cities
        self._num_of_iterations = num_of_iterations

        self._population_size = population_size
        self._mutation_rate = mutation_rate
        self._max_generations = max_generations
        self._scores_path = scores_path 

        self.logger = get_logger()     

    def _generate_points(self, num_of_points, xrange_min, xrange_max, yrange_min, yrange_max):
        points = []
        
        #Generate random points on screen
        for _ in range(num_of_points):
            x = random.randint(xrange_min, xrange_max)
            y = random.randint(yrange_min, yrange_max)

            points.append((x, y))

        return points

    def _write_scores(self, scores, scores_file=None):
        r"""Method to write the generation number and scores in a file"""
        if scores_file is not None:
            with open(scores_file, "w", newline='') as file:
                writer = csv.writer(file)

                # write the header
                writer.writerow(['Generation', 'Best Fitness Score', 'Best Chromosome'])

                for s in scores:
                    writer.writerow(s)

    def run(self):
        r"""Method to run the generations and solve the problem"""
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 24)
        red = (255, 0, 0)

        width = 1000
        height = 1000

        pygame.init()
        pygame.display.set_caption("Traveling Sales Problem")
        screen = pygame.display.set_mode((width, height))

        offset_screen = 50
        xrange_min = offset_screen
        xrange_max = width-offset_screen
        yrange_min = offset_screen
        yrange_max = height-offset_screen

        points = self._generate_points(self._num_of_cities, xrange_min, xrange_max, yrange_min, yrange_max)
        starting_point = 0
        
        for itr in tqdm(range(self._num_of_iterations), desc="Iterations"):
            self.logger.info(f"Run Number = {itr + 1} ->")
            self.logger.info(f"------------------------------")
            
            self._population = Population_TSP(points, starting_point, self._population_size, self._mutation_rate)
                
            scores = []     # list of (generation #, best fitness score)

            best_generation = 0
            best_overall_distance = inf
            best_overall_fitness_score = 0.0
            best_overall_chromosome = None

            for generation in tqdm(range(1, self._max_generations + 1), desc="Generation"):
                self.logger.info(f"Generation = {generation}")

                # calculate the fitness of each chromosome
                self.logger.info("Calculating fitness score ->")
                self._population.calculate_fitness()
                
                self.logger.info(f"Best {generation} genaration Chromosome = {self._population._best_generation_chromosome}")
                self.logger.info(f"Best {generation} genaration Distance = {self._population._best_generation_distance}")
                self.logger.info(f"Best {generation} genaration Fitness score = {self._population._best_generation_fitness_score}")
                scores.append([generation, self._population._best_generation_distance, self._population._best_generation_fitness_score, 
                                self._population._best_generation_chromosome._short_repr()])

                self._population.refill_population()

                # if the current generation distance found is better than all other
                if self._population._best_generation_distance < best_overall_distance:
                    best_overall_distance = self._population._best_generation_distance
                    best_overall_fitness_score = self._population._best_generation_fitness_score
                    best_overall_chromosome = self._population._best_generation_chromosome
                    best_generation = generation

                generation_index_order = self._population._best_generation_chromosome._genotypes
                best_index_order = best_overall_chromosome._genotypes
                # draw the lines on the screen
                screen.fill(black)
                for n in range(len(points)):
                    pygame.draw.circle(screen, white, points[n], 10)
                for m in range(len(points) - 1):
                    pygame.draw.line(screen, green, points[generation_index_order[m].get_value()], points[generation_index_order[m+1].get_value()], 2)
                    pygame.draw.line(screen, red, points[best_index_order[m].get_value()], points[best_index_order[m+1].get_value()], 5)
                    pygame.display.update()           

            self.logger.info("Best run ----->")
            self.logger.info(f"Generation #: {best_generation}")
            self.logger.info(f"Solution: {best_overall_chromosome}")
            self.logger.info(f"Distance: {best_overall_distance}")
            self.logger.info(f"Fitness Score: {best_overall_fitness_score}")
            
            if self._scores_path is not None:
                scores_file = str(Path(self._scores_path) / f"score_{itr + 1}.csv")
                self._write_scores(scores, scores_file)

        

    @staticmethod
    def main(config_file, output_path):
        config = json.load(open(config_file))

        log_file = str(Path(output_path) / "log.txt")
        if os.path.exists(log_file):
            os.remove(log_file)

        create_logger("Travelling Salesman Problem Logger", log_file)
        logger = get_logger()

        # delete all the files from scores folder
        scores_path = Path(output_path) / "scores"
        scores_path.mkdir(parents=True, exist_ok=True)
        scores_path = str(scores_path)
        filelist = [ f for f in os.listdir(scores_path)]
        for f in filelist:
            os.remove(os.path.join(scores_path, f))

        ## Generate cities point here.........
        # TODO
        #
        #

        num_of_cities = 5
        if "num_of_cities" in config and config["num_of_cities"] is not None:
            num_of_cities = config["num_of_cities"]
        logger.info(f"Num of Cities = {num_of_cities}")

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

        obj = TSP(num_of_cities, num_of_iterations, population_size, mutation_rate, max_generations, scores_path=scores_path)
        obj.run()