import pandas as pd
import matplotlib.pyplot as plt

# List of file paths for 50% energy penetration
baseline_folder = "00_Baseline"
file_paths_50 = [
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U1\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U2\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U3\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U4\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U5\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U6\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U7\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_50PE_U8\data_capex_split.csv"
]

# List of file paths for 100% energy penetration
file_paths_100 = [
        fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U1\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U2\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U3\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U4\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U5\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U6\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U7\data_capex_split.csv",
    fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\PI_HSP_FB_100PE_U8\data_capex_split.csv"
]

# List of relevant technologies
relevant_technologies = [
    'up_redox_flow_battery_1', 'up_redox_flow_battery_2', 'up_redox_flow_battery_3',
    'up_redox_flow_battery_4', 'up_redox_flow_battery_5', 'up_redox_flow_battery_6',
    'up_redox_flow_battery_7', 'up_redox_flow_battery_8'
]


# Function to process each file
def process_files(file_paths, relevant_technologies):
    all_yearly_totals = []
    for path in file_paths:
        data = pd.read_csv(path)
        filtered_data = data[data['technology'].isin(relevant_technologies)]
        yearly_totals = filtered_data.groupby('year')['none'].sum().reset_index()
        all_yearly_totals.append(yearly_totals)

    combined_yearly_totals = pd.concat(all_yearly_totals)
    average_yearly_totals = combined_yearly_totals.groupby('year')['none'].mean().reset_index()
    return average_yearly_totals

# Process 50% and 100% energy penetration files
average_yearly_totals_50 = process_files(file_paths_50, relevant_technologies)
average_yearly_totals_100 = process_files(file_paths_100, relevant_technologies)

# Convert costs to billions of Euros
average_yearly_totals_50['none'] = average_yearly_totals_50['none'] / 1000
average_yearly_totals_100['none'] = average_yearly_totals_100['none'] / 1000

# Rename columns for clarity
average_yearly_totals_50.columns = ['year', 'cost_50PE']
average_yearly_totals_100.columns = ['year', 'cost_100PE']

# Merge the two datasets for plotting
merged_data = pd.merge(average_yearly_totals_50, average_yearly_totals_100, on='year')

# Specify the file path
file_path_1 = fr"C:\Users\Hareesh S P\Documents\MT_Offline\MT_Simulations\{baseline_folder}\Results\system_cost_average_plot_up.xlsx"
# Save the DataFrame to the specified location
merged_data.to_excel(file_path_1, index=False)

# Customize x-axis labels
x_labels = [2025, 2030, 2035, 2040, 2045, 2050]
merged_data['year'] = x_labels

# Plotting the results with custom colors and markers
plt.figure(figsize=(10, 6))
plt.plot(merged_data['year'], merged_data['cost_50PE'], label='50% Energy Penetration', color='blue', marker='x')
plt.plot(merged_data['year'], merged_data['cost_100PE'], label='100% Energy Penetration', color='red', marker='x')

# Labeling the axes and title
plt.xlabel('Year', fontsize=15, fontweight='bold')
plt.ylabel('Cost of UP Devices (Billions of Euros)', fontsize=15, fontweight='bold')
#plt.title('Average Up Costs for 50% and 100% Energy Penetration')
plt.legend()
plt.xticks(fontsize=15, fontweight='bold')
plt.yticks(fontsize=15, fontweight='bold')
plt.grid(False)
plt.ylim(0,70)

# Show the plot
plt.show()

