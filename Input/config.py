"""===========================================================================================================================================================================
Title:        ZEN-GARDEN
Created:      October-2021
Authors:      Alissa Ganter (aganter@ethz.ch)
Organization: Laboratory of Reliability and Risk Engineering, ETH Zurich

Description:  Model settings. Overwrite default values defined in default_config.py here.
==========================================================================================================================================================================="""
from zen_garden.model import Config

# create a config
config = Config()

## Analysis - Default dictionary
analysis = config.analysis
## Solver - Default dictionary
solver = config.solver

## Analysis - settings update compared to default values
analysis["objective"] = "total_cost"
analysis["dataset"] = "C:\GitHub\ZEN-garden\Input\PI"
analysis["time_series_aggregation"]["clusterMethod"] = "hierarchical"

## Solver - settings update compared to default values
#solver["name"] = "glpk"
solver["name"] = "gurobi"
solver["solver_options"]["Method"] = 2
solver["solver_options"]["NodeMethod"] = 2
solver["solver_options"]["BarHomogeneous"] = 1
# solver["solver_options"]["BarOrder"] = 0
solver["solver_options"]["DualReductions"] = 0
solver["solver_options"]["Threads"] = 64
solver["solver_options"]["Crossover"] = 0
solver["solver_options"]["ScaleFlag"] = 2
solver["analyze_numerics"] = True
solver["check_unit_consistency"] = True
solver["immutable_unit"] = ["hour","km","kilotCO2eq"]
solver["use_symbolic_labels"] = True
solver["add_duals"] = True
solver["rounding_decimal_points_units"] = 6

