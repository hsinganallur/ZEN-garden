"""===========================================================================================================================================================================
Title:        System file for
Created:      January 2023
Authors:      Jacob Mannhardt (jmannhardt@ethz.ch)
Organization: Laboratory of Reliability and Risk Engineering, ETH Zurich
Description:  Model settings. Overwrite default values defined in default_config.py here.
==========================================================================================================================================================================="""

system = dict()
system["set_conversion_technologies"] = [
    "DAC", "biomass_boiler", "biomass_boiler_DH", "biomass_plant", 
    "biomass_plant_CCS", "carbon_storage", "district_heating_grid", "electrode_boiler", 
    "electrode_boiler_DH", "hard_coal_boiler", "hard_coal_boiler_DH", "hard_coal_plant", 
    "hard_coal_plant_CCS", "heat_pump", "heat_pump_DH", "industrial_gas_consumer", 
    "lignite_coal_plant", "lng_terminal", "natural_gas_boiler", "natural_gas_boiler_DH", 
    "natural_gas_turbine", "natural_gas_turbine_CCS", "nuclear", "oil_boiler", 
    "oil_boiler_DH", "oil_plant", "photovoltaics", "reservoir_hydro", 
    "run-of-river_hydro", "waste_boiler_DH", "waste_plant", "wind_offshore", 
    "wind_onshore"
]
system["set_storage_technologies"] = [
    "battery", "hydrogen_storage", "natural_gas_storage", "pumped_hydro"
]
system["set_transport_technologies"] = [
    "carbon_pipeline", "natural_gas_pipeline", "power_line"
]

system["set_nodes"] = [
    "AT", "BE", "BG", "CH", 
    "CZ", "DE", "DK", "EE", 
    "EL", "ES", "FI", "FR", 
    "HR", "HU", "IE", "IT", 
    "LT", "LU", "LV", "NL", 
    "NO", "PL", "PT", "RO", 
    "SE", "SI", "SK", "UK"
]

# time steps
system["reference_year"] = 2022
system["optimized_years"] = 15
system["interval_between_years"] = 2
system["use_rolling_horizon"] = False
system["years_in_rolling_horizon"] = 2

system["unaggregated_time_steps_per_year"] = 8760
system["aggregated_time_steps_per_year"] = 100
system["conduct_time_series_aggregation"] = True

system["knowledge_depreciation_rate"] = 0.1