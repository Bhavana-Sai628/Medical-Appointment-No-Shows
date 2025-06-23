import pandas as pd
import kagglehub
import os

# Download dataset
df = pd.read_csv("KaggleV2-May-2016.csv")

# Drop duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Format dates
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

# Save cleaned data
df.to_csv(os.path.join("cleaned_medical_appointments.csv"), index=False)