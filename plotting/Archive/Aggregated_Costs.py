import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_44 (SD + LD Tests Origin)\\Results"

# Change this variable to the desired folder name
folder_name = "PI_HSP_FB_100P100E_LD_SD"
out_folder1 = f"{base_folder}\\{folder_name}"
r = Results(out_folder1)

# Total Costs
data_capex_total = r.get_total("cost_capex_total")
data_opex_total = r.get_total("cost_opex_total")
data_carrier_total = r.get_total("cost_carrier_total")

data_carbon_emissions = r.get_df("cost_carbon_emissions_total")
data_capex_split = r.get_df("cost_capex")
data_opex_split = r.get_df("cost_opex")
data_carrier_split = r.get_df("cost_carrier")

a=1