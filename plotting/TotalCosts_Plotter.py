import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to calculate total system costs
def calculate_total_system_costs(file_paths):
    all_costs = []

    # Iterate through each file path
    for path in file_paths:
        # Read in the capex, opex, and carrier cost files
        capex_file = os.path.join(path, 'data_capex_total.csv')
        opex_file = os.path.join(path, 'data_opex_total.csv')
        carrier_file = os.path.join(path, 'data_carrier_total.csv')

        capex_total = pd.read_csv(capex_file)
        opex_total = pd.read_csv(opex_file)
        carrier_total = pd.read_csv(carrier_file)

        # Merge the data on the 'year' column
        merged_df = pd.merge(capex_total, opex_total, on='year')
        merged_df = pd.merge(merged_df, carrier_total, on='year')

        # Calculate the total system cost in billions
        merged_df['total_system_cost'] = (merged_df['cost_capex_total'] +
                                          merged_df['cost_opex_total'] +
                                          merged_df['cost_carrier_total']) / 1000

        # Append to the list
        all_costs.append(merged_df['total_system_cost'])

    # Create a DataFrame and return it
    costs_df = pd.DataFrame(all_costs).T
    costs_df['average_system_cost'] = costs_df.mean(axis=1)

    return costs_df

# Define file paths for both simulations
baseline_folder = "00_Extreme_Optimistic"
file_paths_1 = [
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U1",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U2",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U3",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U4",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U5",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U6",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U7",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U8"
]

file_paths_2 = [
     fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U1",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U2",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U3",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U4",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U5",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U6",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U7",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U8"
]

# Calculate total system costs for both sets of file paths
costs_df_1 = calculate_total_system_costs(file_paths_1)
costs_df_2 = calculate_total_system_costs(file_paths_2)

# Specify the file path
file_path_1 = fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\system_cost_average_plot_50PE.xlsx"
file_path_2 = fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\system_cost_average_plot_100PE.xlsx"

# Save the DataFrame to the specified location
costs_df_1.to_excel(file_path_1, index=False)
costs_df_2.to_excel(file_path_2, index=False)

# Update the year labels for the X-axis
year_labels = {0: 2025, 1: 2030, 2: 2035, 3: 2040, 4: 2045, 5: 2050}

# Plot the averaged results for both sets
plt.figure(figsize=(10, 6))
plt.plot(costs_df_1.index, costs_df_1['average_system_cost'], marker='o', linestyle='-', label='Total Costs 50%', color='b')
plt.plot(costs_df_2.index, costs_df_2['average_system_cost'], marker='o', linestyle='-', label='Total Costs 100%', color='r')

# Set labels and ticks with size 15 and bold
#plt.xlabel('Year', fontsize=15, fontweight='bold')
plt.ylabel('Total System Cost (Billions of Euros)', fontsize=15, fontweight='bold')
plt.xticks(ticks=costs_df_1.index, labels=[year_labels.get(year, year) for year in costs_df_1.index], fontsize=15,
           fontweight='bold')
plt.yticks(fontsize=15, fontweight='bold')

# Set Y-axis limit
plt.ylim(300, 451)

# Display grid and legend
plt.grid(False)
#plt.legend(fontsize=15)
# Add legend outside the plot
#plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Define the path to save the figure
save_path = fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\system_cost_average_plot.png"

# Save the plot as a PNG file
plt.savefig(save_path)