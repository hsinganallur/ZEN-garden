import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from zen_garden.postprocess.results.results import Results

# Define your base folder path as a variable
base_folder = "C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Simulations\\T_28\\Results"

# Change this variable to the desired folder name
folder_name = "PI_HSP_FB_EP"
out_folder1 = f"{base_folder}\\{folder_name}"
r = Results(out_folder1)

# Define colors for each technology category
color_map= {
    "DAC": 'aqua',
    "biomass_boiler": 'darkseagreen',
    "biomass_boiler_DH": 'lightseagreen',
    "biomass_plant": 'springgreen',
    "biomass_plant_CCS": 'mediumseagreen',
    "carbon_storage": 'limegreen',
    "district_heating_grid": 'lime',
    "electrode_boiler": 'mediumspringgreen',
    "electrode_boiler_DH": 'darkgreen',
    "hard_coal_boiler": 'brown',
    "hard_coal_boiler_DH": 'darkred',
    "hard_coal_plant": 'firebrick',
    "hard_coal_plant_CCS": 'maroon',
    "heat_pump": 'yellowgreen',
    "heat_pump_DH": 'olive',
    "lignite_coal_plant": 'chocolate',
    "lng_terminal": 'peru',
    "natural_gas_boiler": 'darkgoldenrod',
    "natural_gas_boiler_DH": 'goldenrod',
    "natural_gas_turbine": 'khaki',
    "natural_gas_turbine_CCS": 'gold',
    "nuclear": 'slateblue',
    "oil_boiler": 'orangered',
    "oil_boiler_DH": 'coral',
    "oil_plant": 'tomato',
    "photovoltaics": 'orange',
    "reservoir_hydro": 'skyblue',
    "run-of-river_hydro": 'deepskyblue',
    "waste_boiler_DH": 'lightblue',
    "waste_plant": 'powderblue',
    "wind_offshore": 'aquamarine',
    "wind_onshore": 'deeppink',
    "battery": 'darkslategray',
    "hydrogen_storage": 'teal',
    "natural_gas_storage": 'darkturquoise',
    "pumped_hydro": 'cadetblue',
    "carbon_pipeline": 'lightsteelblue',
    "natural_gas_pipeline": 'steelblue',
    "power_line": 'darkslateblue',
    "vanadium_redox_flow_battery": 'mediumblue',
    "up_redox_flow_battery_1": 'blue',
    "up_redox_flow_battery_2": 'royalblue',
    "up_redox_flow_battery_3": 'cornflowerblue',
    "up_redox_flow_battery_4": 'lightblue',
    "up_redox_flow_battery_5": 'powderblue'
}

# Total Costs
data_capex_total = r.get_total("cost_capex_total")
data_opex_total = r.get_total("cost_opex_total")
data_carrier_total = r.get_total("cost_carrier_total")


data_carbon_emissions = r.get_df("cost_carbon_emissions_total")

data_capex_split = r.get_df("cost_capex")
# Convert the dictionary to a Series
series_capex = pd.Series(data_capex_split['none'])
# Reset the index to convert the multi-index into columns
data_capex_split = series_capex.reset_index()
# Rename the columns
data_capex_split.columns = ['technology', 'capacity_type', 'location', 'year', 'value']
data_capex_split.drop(columns=['capacity_type', 'location','year'], inplace=True)
columns_to_check_capex = data_capex_split.columns.difference(['year', 'technology', 'capacity_type', 'location'])
data_capex_split = data_capex_split.groupby('technology').sum()

data_opex_split = r.get_df("cost_opex")
# Convert the dictionary to a Series
series_opex = pd.Series(data_opex_split['none'])
# Reset the index to convert the multi-index into columns
data_opex_split = series_opex.reset_index()
# Rename the columns
data_opex_split.columns = ['technology', 'location', 'time', 'value']
data_opex_split.drop(columns=['location','time'], inplace=True)
data_opex_split = data_opex_split.groupby('technology').sum()

data_carrier_split = r.get_df("cost_carrier")
# Convert the dictionary to a Series
series_carrier = pd.Series(data_carrier_split['none'])
# Reset the index to convert the multi-index into columns
data_carrier_split = series_carrier.reset_index()
# Rename the columns
data_carrier_split.columns = ['carrier', 'node', 'time', 'value']
data_carrier_split.drop(columns=['node' , 'time'], inplace=True)
columns_to_check_carrier = data_carrier_split.columns.difference(['year', 'technology', 'capacity_type', 'location'])
data_carrier_split = data_carrier_split.groupby('carrier').sum()

# Shed Demand
data_shed_demand = r.get_total("cost_shed_demand").groupby('carrier').sum()

# Define the threshold
threshold = 10**-6
# For data_capex_split
data_capex_split = data_capex_split[data_capex_split['value'] >= threshold]
# For data_opex_split
data_opex_split = data_opex_split[data_opex_split['value'] >= threshold]
# For data_carrier_split
data_carrier_split = data_carrier_split[data_carrier_split['value'] >= threshold]

a=1