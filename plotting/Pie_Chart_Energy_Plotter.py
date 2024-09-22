import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the new spreadsheet
file_path = 'C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Simulations\\00_Extreme_Optimistic\\Results\\Pie_Chart_Maker_Power.xlsx'  # Update with your new file path
xls = pd.ExcelFile(file_path)

# Define the save directory (same as file path)
save_dir = os.path.dirname(file_path)

# Define the technologies and colors
technologies = ['battery', 'hydrogen_storage', 'pumped_hydro_storage', 'up_devices']
colors = ['dodgerblue', 'forestgreen', 'orange', 'tomato']

# Define a function to create pie charts without zeros and with bold text
def plot_pie_with_bold_text(ax, values, colors, total_value, max_total_value):
    non_zero_values = values[values > 0]
    non_zero_colors = [color for value, color in zip(values, colors) if value > 0]
    pie_size = total_value / max_total_value  # Scale the pie chart size
    ax.pie(non_zero_values, labels=None, autopct=None, startangle=140, colors=non_zero_colors,
           textprops={'fontsize': 20, 'fontweight': 'bold'}, radius=pie_size*2)

# Load the sheets
df_0_8h = pd.read_excel(xls, sheet_name='Discharge_Time(0-12h)')
df_8_20h = pd.read_excel(xls, sheet_name='Discharge_Time(12-50h)')
df_50_150h = pd.read_excel(xls, sheet_name='Discharge_Time(50-150h)')

# Extract values for the charts
values_100_0_8h = df_0_8h[df_0_8h['Percentage_of_total_costs_(%)'] == 100][technologies].iloc[0]
values_50_0_8h = df_0_8h[df_0_8h['Percentage_of_total_costs_(%)'] == 50][technologies].iloc[0]

values_100_8_20h = df_8_20h[df_8_20h['Percentage_of_total_costs_(%)'] == 100][technologies].iloc[0]
values_50_8_20h = df_8_20h[df_8_20h['Percentage_of_total_costs_(%)'] == 50][technologies].iloc[0]

values_100_50_150h = df_50_150h[df_50_150h['Percentage_of_total_costs_(%)'] == 100][technologies].iloc[0]
values_50_50_150h = df_50_150h[df_50_150h['Percentage_of_total_costs_(%)'] == 50][technologies].iloc[0]

# Calculate the total values for proportional sizing
total_100_0_8h = values_100_0_8h.sum()
total_50_0_8h = values_50_0_8h.sum()

total_100_8_20h = values_100_8_20h.sum()
total_50_8_20h = values_50_8_20h.sum()

total_100_50_150h = values_100_50_150h.sum()
total_50_50_150h = values_50_50_150h.sum()

# Maximum total value for proportional scaling
max_total_value = max(total_100_0_8h, total_50_0_8h, total_100_8_20h, total_50_8_20h, total_100_50_150h, total_50_50_150h)

# Create the first figure with top row (100% cost)
fig1, axs1 = plt.subplots(1, 3, figsize=(24, 12))

# Plot for the first sheet (0-8h)
plot_pie_with_bold_text(axs1[0], values_100_0_8h, colors, total_100_0_8h, max_total_value)

# Plot for the second sheet (8-20h)
plot_pie_with_bold_text(axs1[1], values_100_8_20h, colors, total_100_8_20h, max_total_value)

# Plot for the third sheet (50-150h)
plot_pie_with_bold_text(axs1[2], values_100_50_150h, colors, total_100_50_150h, max_total_value)

# Add horizontal axis labels (Discharge Time Ranges)
for i, label in enumerate(['(0-12h)', '(12-50h)', '(50-150h)']):
    axs1[i].set_xlabel(f'{label}', fontsize=40, fontweight='bold', labelpad=160)

# Add vertical axis label (Percentage of Total Costs 100%)
axs1[0].set_ylabel('Total Cost of UP Devices 100%', fontsize=40, fontweight='bold')

# Reduce space between subplots
plt.subplots_adjust(wspace=0, hspace=0)  # Adjust wspace to reduce horizontal space

plt.tight_layout()

# Save the figure to the same directory
fig1_save_path = os.path.join(save_dir, 'pie_chart_100_percent.png')
plt.savefig(fig1_save_path)

plt.show()

# Create the second figure with bottom row (50% cost)
fig2, axs2 = plt.subplots(1, 3, figsize=(24, 12))

# Plot for the first sheet (0-8h)
plot_pie_with_bold_text(axs2[0], values_50_0_8h, colors, total_50_0_8h, max_total_value)

# Plot for the second sheet (8-20h)
plot_pie_with_bold_text(axs2[1], values_50_8_20h, colors, total_50_8_20h, max_total_value)

# Plot for the third sheet (50-150h)
plot_pie_with_bold_text(axs2[2], values_50_50_150h, colors, total_50_50_150h, max_total_value)

# Add horizontal axis labels (Discharge Time Ranges)
for i, label in enumerate(['(0-12h)', '(12-50h)', '(50-150h)']):
    axs2[i].set_xlabel(f'{label}', fontsize=40, fontweight='bold', labelpad=160)

# Add vertical axis label (Percentage of Total Costs 50%)
axs2[0].set_ylabel('Total Cost of UP Devices 50%', fontsize=40, fontweight='bold')

# Reduce space between subplots
plt.subplots_adjust(wspace=0.05, hspace=0)  # Adjust wspace to reduce horizontal space

plt.tight_layout()

# Save the figure to the same directory
fig2_save_path = os.path.join(save_dir, 'pie_chart_50_percent.png')
plt.savefig(fig2_save_path)

plt.show()

"""import pandas as pd
import matplotlib.pyplot as plt

# Load the new spreadsheet
file_path = 'C:\\Users\\Hareesh S P\\Documents\\MT_Offline\\MT_Simulations\\00_Extreme_Optimistic\\Results\\Pie_Chart_Maker_Energy.xlsx'  # Update with your new file path
xls = pd.ExcelFile(file_path)

# Define the technologies and colors
technologies = ['battery', 'hydrogen_storage', 'pumped_hydro_storage', 'up_devices']
colors = ['dodgerblue', 'forestgreen', 'orange', 'tomato']

# Define a function to create pie charts without zeros and with bold text
def plot_pie_with_bold_text(ax, values, colors):
    non_zero_values = values[values > 0]
    non_zero_colors = [color for value, color in zip(values, colors) if value > 0]
    ax.pie(non_zero_values, labels=None, autopct=None, startangle=140, colors=non_zero_colors,
           textprops={'fontsize': 20, 'fontweight': 'bold'})

# Load the sheets
df_0_8h = pd.read_excel(xls, sheet_name='Discharge_Time(0-12h)')
df_8_20h = pd.read_excel(xls, sheet_name='Discharge_Time(12-50h)')
df_50_150h = pd.read_excel(xls, sheet_name='Discharge_Time(50-150h)')

# Extract values for the charts
values_100_0_8h = df_0_8h[df_0_8h['Percentage_of_total_costs_(%)'] == 100][technologies].iloc[0]
#values_75_0_8h = df_0_8h[df_0_8h['Percentage_of_total_costs_(%)'] == 75][technologies].iloc[0]
values_50_0_8h = df_0_8h[df_0_8h['Percentage_of_total_costs_(%)'] == 50][technologies].iloc[0]
#values_25_0_8h = df_0_8h[df_0_8h['Percentage_of_total_costs_(%)'] == 25][technologies].iloc[0]

values_100_8_20h = df_8_20h[df_8_20h['Percentage_of_total_costs_(%)'] == 100][technologies].iloc[0]
#values_75_8_20h = df_8_20h[df_8_20h['Percentage_of_total_costs_(%)'] == 75][technologies].iloc[0]
values_50_8_20h = df_8_20h[df_8_20h['Percentage_of_total_costs_(%)'] == 50][technologies].iloc[0]
#values_25_8_20h = df_8_20h[df_8_20h['Percentage_of_total_costs_(%)'] == 25][technologies].iloc[0]

values_100_50_150h = df_50_150h[df_50_150h['Percentage_of_total_costs_(%)'] == 100][technologies].iloc[0]
#values_75_50_150h = df_50_150h[df_50_150h['Percentage_of_total_costs_(%)'] == 75][technologies].iloc[0]
values_50_50_150h = df_50_150h[df_50_150h['Percentage_of_total_costs_(%)'] == 50][technologies].iloc[0]
#values_25_50_150h = df_50_150h[df_50_150h['Percentage_of_total_costs_(%)'] == 25][technologies].iloc[0]

# Create the figure with subplots
fig, axs = plt.subplots(2, 3, figsize=(24, 24))

# Plot for the first sheet (0-8h)
plot_pie_with_bold_text(axs[0, 0], values_100_0_8h, colors)
#plot_pie_with_bold_text(axs[1, 0], values_75_0_8h, colors)
plot_pie_with_bold_text(axs[1, 0], values_50_0_8h, colors)
#plot_pie_with_bold_text(axs[3, 0], values_25_0_8h, colors)

# Plot for the second sheet (8-20h)
plot_pie_with_bold_text(axs[0, 1], values_100_8_20h, colors)
#plot_pie_with_bold_text(axs[1, 1], values_75_8_20h, colors)
plot_pie_with_bold_text(axs[1, 1], values_50_8_20h, colors)
#plot_pie_with_bold_text(axs[3, 1], values_25_8_20h, colors)

# Plot for the third sheet (50-150h)
plot_pie_with_bold_text(axs[0, 2], values_100_50_150h, colors)
#plot_pie_with_bold_text(axs[1, 2], values_75_50_150h, colors)
plot_pie_with_bold_text(axs[1, 2], values_50_50_150h, colors)
#plot_pie_with_bold_text(axs[3, 2], values_25_50_150h, colors)

# Add horizontal axis labels (Discharge Time Ranges)
for i, label in enumerate(['(0-12h)', '(12-50h)', '50-150h']):
    axs[1, i].set_xlabel(f'{label}', fontsize=40, fontweight='bold')

# Add vertical axis labels (Percentage of Total Costs)
for i, label in enumerate(['100%', '50%']):
    axs[i, 0].set_ylabel(f' {label}', fontsize=40, fontweight='bold')

plt.tight_layout()
plt.show()"""