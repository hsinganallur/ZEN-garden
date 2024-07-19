import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_18\\Results"
# Change this variable to the desired folder name
folder_name = "VPI_2024_25_8760"
out_folder1 = f"{base_folder}\\{folder_name}"
r = Results(out_folder1)

data_capex = r.get_df("cost_capex_total")
data_opex = r.get_df("cost_opex_total")
data_carbon_emissions = r.get_df("cost_carbon_emissions_total")
data_carrier = r.get_df("cost_carrier_total")
data_total_costs = r.get_df("cost_total")

a=1
