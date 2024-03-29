from django import forms

from .models import Post

parameters = {
              "simulation_name": "01_basic_functions_one_cell_deployment",
              "population_names": ['pop_01'],
              "population_locations": [[(0,0,0)]],
              "deployment_code": 1,
              "chromosome_bases": ['0','1'],
              "background_mutation": 0.1,
              "additional_mutation": 0,
              "mutation_type": 'point',
              "chromosome_size": 30,
              "genome_size": 1,
              "max_tape_length": 50,
              "clean_cell": True,
              "interpret_chromosome": True,
              "max_codon": 2000,
              "population_size": 100,
              "eco_cell_capacity": 100,
              "world_x": 5,
              "world_y": 5,
              "world_z": 5,
              "goal": 0,
              "maximum_generations": 100,
              "fossilized_ratio": 0.01,
              "fossilized_frequency": 20,
              "print_frequency": 10,
              "ragaraja_version": 0,
              "ragaraja_instructions": ['000', '001', '010', 
                                        '011', '100', '101'],
              "eco_buried_frequency": 100,
              "database_file": "simulation.db",
              "database_logging_frequency": 1
             }

pset = set(parameters.keys())


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = pset
