import pandas as pd
# Retrieve data and create DataFrames
df_a = r.get_full_ts("flow_storage_charge")
df_b = r.get_df("flow_storage_charge")
df_c = r.get_total("flow_storage_charge")
# Convert to DataFrames
df_a = pd.DataFrame(df_a)
df_b = pd.DataFrame(df_b)
df_c = pd.DataFrame(df_c)
# Define file paths
file_path_a = "C:\\GitHub\\ZEN-garden\\looper\\other_tests\\flow_storage_charge_full_ts.csv"
file_path_b = "C:\\GitHub\\ZEN-garden\\looper\\other_tests\\flow_storage_charge_get_df.csv"
file_path_c = "C:\\GitHub\\ZEN-garden\\looper\\other_tests\\flow_storage_charge_get_total.csv"
# Save DataFrames to CSV files
df_a.to_csv(file_path_a, index=True, mode='w')
df_b.to_csv(file_path_b, index=True, mode='w')
df_c.to_csv(file_path_c, index=True, mode='w')
print("CSV files saved successfully.")
