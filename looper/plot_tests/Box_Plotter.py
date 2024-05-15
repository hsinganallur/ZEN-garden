import matplotlib.pyplot as plt

# Your data
battery = [289.8614206	,289.8614206,	289.8614206	,289.8614206	,289.8614206


]
hydrogen_storage = [12.76487395	,12.76487395	,12.76487395,	12.76487395	,12.76487395

]
pumped_hydro = [75.88346816	,75.88346816	,75.88346816	,75.88346816,	75.88346816


]
vanadium_redox_flow_battery = [385	,385	,385,	385,	385


]
vrfb_references = [173.34,	136.84	,989.85	,912.3,	385


]
up_membraneless_redox_flow_battery = [263152.1197	,27537.73956,	11152.62214	,2293.374308,	157.4

]
up_devices =  [500.00	,370.00,	250.00,	210.00,	180.00

]

data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and capex_specific_energy (€/kWh)')
plt.ylabel('capex_specific_energy (€ /kWh)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")

import matplotlib.pyplot as plt

# Your data
battery = [0, 0, 0, 0, 0,

]
hydrogen_storage = [0, 0, 0, 0, 0,

]
pumped_hydro = [0, 0, 0, 0, 0,

]
vanadium_redox_flow_battery = [133.12,	133.12	,133.12,	133.12,	133.12


]
vrfb_references = [63.86	,9.34	,9.34	,63.86	,63.86


]
up_membraneless_redox_flow_battery = [0, 0, 0, 0, 0,
]
up_devices =  [9.34, 9.34, 9.34, 9.34, 9.34,
]

data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and opex_specific_energy (€/kWh)')
plt.ylabel('opex_specific_energy (€/kWh)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")"""


"""import matplotlib.pyplot as plt

# Your data
battery = [280.3475604	,280.3475604	,280.3475604	,280.3475604,	280.3475604


]
hydrogen_storage = [2957.121575	,2957.121575	,2957.121575	,2957.121575	,2957.121575

]
pumped_hydro = [280.3475604,	280.3475604,	280.3475604,	280.3475604	,280.3475604


]
vanadium_redox_flow_battery = [1080,	1080	,1080,	1080,	1080



]
vrfb_references = [593.91,	547.38	,1485.22	,1368.45,	1080


]
up_membraneless_redox_flow_battery = [800,	4000	,8000	,200,	800

]
up_devices = [4000.00	,200.00	,3155.56,	800.00	,1898.15


]


data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and capex_specific (€/kW)')
plt.ylabel('capex_specific (€/kW)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")"""


"""import matplotlib.pyplot as plt

# Your data
battery = [10, 10, 10, 10, 10

]
hydrogen_storage = [0, 0, 0, 0, 0,

]
pumped_hydro = [0, 0, 0, 0, 0,

]
vanadium_redox_flow_battery = [0.59	,0.59		,0.59		,0.59	,0.59
]
vrfb_references = [0	,0.2,	0.59,	0.2,	0

]
up_membraneless_redox_flow_battery = [0.59	,0.59		,0.59		,0.59	,0.59
]
up_devices = [0	,0.2,	0.2,	0.2,	0

]


data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and self_discharge (%)')
plt.ylabel('self_discharge (%)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")"""

"""import matplotlib.pyplot as plt

# Your data
battery = [92.736185	,92.736185,	92.736185,	92.736185,	92.736185

]
hydrogen_storage = [63.2455532,	63.2455532,63.2455532,63.2455532	,63.2455532

]
pumped_hydro = [88.3176086632784,	88.3176086632784	,88.3176086632784,	88.3176086632784	,88.3176086632784

]
vanadium_redox_flow_battery = [75.9	,75.9		,75.9		,75.9	,75.9
]
vrfb_references = [70	,78.3,	85,	80,	70

]
up_membraneless_redox_flow_battery = [80	,80,	80,	80,	80
]
up_devices = [85.00	,70.00	,76.67,	85.00,	81.67

]


data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and efficiency_discharge (%)')
plt.ylabel('efficiency_discharge (%)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")

import matplotlib.pyplot as plt

# Your data
battery = [92.736185	,92.736185,	92.736185,	92.736185,	92.736185

]
hydrogen_storage = [63.2455532,	63.2455532,63.2455532,63.2455532	,63.2455532

]
pumped_hydro = [88.3176086632784,	88.3176086632784	,88.3176086632784,	88.3176086632784	,88.3176086632784

]
vanadium_redox_flow_battery = [75.9	,75.9		,75.9		,75.9	,75.9
]
vrfb_references = [70	,78.3,	85,	80,	70

]
up_membraneless_redox_flow_battery = [80	,80,	80,	80,	80
]
up_devices = [85.00	,70.00	,76.67,	85.00,	81.67

]


data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and efficiency_charge (%)')
plt.ylabel('efficiency_charge (%)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")"""

"""
import matplotlib.pyplot as plt

# Your data
battery = [2.471110756,2.471110756,2.471110756,	2.471110756	,2.471110756
]
hydrogen_storage = [56.32675703	,56.32675703	,56.32675703	,56.32675703	,56.32675703
]
pumped_hydro = [7.588346816,	7.588346816	,7.588346816,	7.588346816	,7.588346816
]
vanadium_redox_flow_battery = [0,0,0,0,0]
vrfb_references = [6.39	,10.95	,14.6,	63.86	,5.47
]
up_membraneless_redox_flow_battery = [0,0,0,0,0]
up_devices = [17.2,	0.86,	13.568908	,3.44	,8.162045
]


data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and opex_specific_fixed (€/kW)')
plt.ylabel('opex_specific_fixed (€/kW)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")"""


"""import matplotlib.pyplot as plt

# Your data
battery = [0,0,0,0,0]
hydrogen_storage = [0,0,0,0,0]
pumped_hydro = [0,0,0,0,0]
vanadium_redox_flow_battery = [0,0,0,0,0]
vrfb_references = [6.39,1.73,3.74,4.74,2.19]
up_membraneless_redox_flow_battery = [0,0,0,0,0]
up_devices = [0.84108, 0.042054,0.99641919,0.25261296,0.599371613]


data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,
        vrfb_references, up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and opex_specific_variable (€/kW)')
plt.ylabel('opex_specific_variable (€/kW)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")


import matplotlib.pyplot as plt

# Your data
battery = [13, 13, 13, 13, 13]
hydrogen_storage = [100, 100, 100, 100, 100]
pumped_hydro = [60, 60, 60, 60, 60]
vanadium_redox_flow_battery = [20, 20, 25, 20, 25]
vrfb_references = [15,20,20,25,10]
up_membraneless_redox_flow_battery = [20, 25, 25, 20, 20]
up_devices = [20, 25, 25, 20, 20]

data = [battery, hydrogen_storage, pumped_hydro, vanadium_redox_flow_battery,vrfb_references,
        up_membraneless_redox_flow_battery, up_devices]

labels = ['Battery', 'Hydrogen Storage', 'Pumped Hydro', 'Vanadium RFB', 'Vanadium RFB References',
          'UP Membraneless RFB Current Range', 'UP Devices']

colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightgrey', 'blue']

# Create box plots
#plt.figure(figsize=(10, 6))
#box = plt.boxplot(data, labels=labels, patch_artist=True)

# Create box plots
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(edgecolor=None), notch=False, medianprops=dict(color='None'), meanprops=dict(color='None'))

#Fill boxes with colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add legend with adjusted position outside the plot area

legend_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor='none') for color in colors]
plt.legend(legend_patches, labels, loc='upper left', bbox_to_anchor=(1.05, 1))

plt.title('Box Plot of Energy Storage Types and Lifetime (Years)')
plt.ylabel('Lifetime (Years)')
#plt.xlabel('Energy Storage Types')
plt.xticks(rotation=45, ha='right')  # Rotate labels and adjust alignment
plt.tight_layout()

# Specify the file path
file_path = 'C:\\Users\\Hareesh S P\\OneDrive - Unbound Potential GmbH\\MasterThesis\\Other Data\\Older Versions of Files\\box_plot_energy_storage.png'

# Save plot to file
plt.savefig(file_path)

print(f"Plot saved at {file_path}")