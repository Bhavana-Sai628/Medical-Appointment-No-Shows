1. Importing Required Libraries
import pandas as pd
import kagglehub
import os
pandas: Used for data loading, manipulation, and cleaning.

kagglehub: (Note: not actually used in the script — can be removed unless you're downloading from Kaggle using it).

os: Used for file path handling during file saving.

2. Load the Dataset
df = pd.read_csv("KaggleV2-May-2016.csv")
Reads the original dataset into a Pandas DataFrame.

This dataset contains patient information related to medical appointments and whether or not they showed up.

 3. Data Cleaning

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
Removes duplicate rows to avoid skewed analysis.

Removes any missing data (NaN values) to maintain data integrity.

4. Standardize Column Names

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
Converts column names to lowercase.

Removes leading/trailing whitespace.

Replaces spaces with underscores (_), making them easier to use in code.

5. Format Date Columns
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')
Converts scheduledday and appointmentday columns to datetime format for proper time-based analysis.

errors='coerce' ensures any invalid formats are converted to NaT (missing time).

 6. Save Cleaned Dataset
df.to_csv(os.path.join("cleaned_medical_appointments.csv"), index=False)
Saves the cleaned data as cleaned_medical_appointments.csv.

index=False avoids saving the row numbers as a separate column.

