import pandas as pd


enrollment_df = pd.read_csv("data/input/CPSC_Enrollment_Info_2015_01.csv")
service_area_df = pd.read_csv("data/input/MA_Cnty_SA_2015_01.csv")

enrollment_df = enrollment_df.rename(columns={"Contract Number": "Contract ID", "Plan ID": "Plan ID", "FIPS State County Code": "FIPS", "Enrollment": "Enrollment"})
service_area_df = service_area_df.rename(columns={"FIPS": "FIPS"})


enrollment_df["Enrollment"] = pd.to_numeric(enrollment_df["Enrollment"], errors="coerce")


service_area_df["FIPS"] = pd.to_numeric(service_area_df["FIPS"], errors="coerce")


enrollment_df = enrollment_df.drop_duplicates()
service_area_df = service_area_df.drop_duplicates()


merged_df = pd.merge(enrollment_df, service_area_df, on=["Contract ID", "FIPS"], how="inner")


table_1 = merged_df.groupby("Plan Type")["Plan ID"].nunique().reset_index()
table_1.columns = ["Plan Type", "Plan Count"]

# Identify rows to exclude (SNP, EGHP, and 800-series plans)
filtered_df = merged_df[
    (~merged_df["Plan Type"].str.contains("SNP", case=False, na=False)) &  # Exclude SNP
    (merged_df["EGHP"].isna()) &  # Exclude Employer Group Plans
    (~merged_df["Plan ID"].astype(str).str.startswith("8"))  # Exclude 800-series plans
]

# Table 2: Count of plans by type after exclusions
table_2 = filtered_df.groupby("Plan Type")["Plan ID"].nunique().reset_index()
table_2.columns = ["Plan Type", "Plan Count"]

# Table 3: Average enrollments per plan type
table_3 = filtered_df.groupby("Plan Type")["Enrollment"].mean().reset_index()
table_3.columns = ["Plan Type", "Average Enrollment"]

# Display tables
print("Plan Count by Type (Before Exclusions):")
print(table_1)
print("\nPlan Count by Type (After Exclusions):")
print(table_2)
print("\nAverage Enrollment by Plan Type:")
print(table_3)










