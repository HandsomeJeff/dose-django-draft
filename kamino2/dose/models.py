# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    simulation_name = models.CharField(max_length=20)
    population_names = models.CharField(max_length=20)
    population_locations = models.CharField(max_length=20)
    deployment_code = models.CharField(max_length=20)
    chromosome_bases = models.CharField(max_length=20)
    background_mutation = models.CharField(max_length=20)
    additional_mutation = models.CharField(max_length=20)
    mutation_type = models.CharField(max_length=20)
    chromosome_size = models.CharField(max_length=20)
    genome_size = models.CharField(max_length=20)
    max_tape_length = models.CharField(max_length=20)
    clean_cell = models.CharField(max_length=20)
    interpret_chromosome = models.CharField(max_length=20)
    max_codon = models.CharField(max_length=20)
    population_size = models.CharField(max_length=20)
    eco_cell_capacity = models.CharField(max_length=20)
    world_x = models.CharField(max_length=20)
    world_y = models.CharField(max_length=20)
    world_z = models.CharField(max_length=20)
    goal = models.CharField(max_length=20)
    maximum_generations = models.CharField(max_length=20)
    fossilized_ratio = models.CharField(max_length=20)
    fossilized_frequency = models.CharField(max_length=20)
    print_frequency = models.CharField(max_length=20)
    ragaraja_version = models.CharField(max_length=20)
    ragaraja_instructions = models.CharField(max_length=20)
    eco_buried_frequency = models.CharField(max_length=20)
    database_file = models.CharField(max_length=20)
    database_logging_frequency = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    save_date = models.DateTimeField(blank=True, null=True)

    def Save(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
