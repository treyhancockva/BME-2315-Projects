<<<<<<< Updated upstream
<<<<<<< Updated upstream
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
metadata_df = pd.read_csv("NO DATE GENOTYPE Metadata.csv")

head_injury_counts = metadata_df["Known head injury"].value_counts()
print(head_injury_counts)

subset_df = metadata_df[
    metadata_df["Known head injury"].notna() & 
    metadata_df["Age of onset cognitive symptoms"].notna() 
]

print("Number of people:", len(subset_df))

grouped = subset_df.groupby("Known head injury")["Age of onset cognitive symptoms"].mean()
print(grouped)

grouped.plot(kind="bar", color=["skyblue", "salmon"])

plt.title("Average Age of Cognitive Decline by Head Injury Status")
plt.xlabel("Head Injury Status")
plt.ylabel("Average Age of Onset of Cognitive Decline")
plt.xticks(rotation=0)
plt.ylim(70, None)
plt.show() 

from scipy import stats

# Filter dataset (must have both values)
onset_df = metadata_df[
    metadata_df["Known head injury"].notna() &
    metadata_df["Age of onset cognitive symptoms"].notna()
]

# Separate groups
with_injury = onset_df[onset_df["Known head injury"] == "Yes"]["Age of onset cognitive symptoms"]
without_injury = onset_df[onset_df["Known head injury"] == "No"]["Age of onset cognitive symptoms"]

t_stat, p_val = stats.ttest_ind(with_injury, without_injury, nan_policy='omit')

print("t-value:", t_stat)
print("p-value:", p_val)

# Interpretation
alpha = 0.05
if p_val < alpha:
    print("Statistically significant difference (reject null hypothesis).")
else:
    print("No statistically significant difference (fail to reject null hypothesis).")
=======
=======
>>>>>>> Stashed changes
#1) BUILD OUR CLASS BY COMBINING TWO .csv FILES OF DATA
 
import csv
import warnings
import matplotlib.pyplot as plt

class Patient: 

    all_patients = []

    death_age = []

    education_lvl = {}

    def __init__(self, DonorID, ABeta40: float , ABeta42: float, tTau: float, pTau: float):

        self.DonorID = DonorID
        self.ABeta40 = ABeta40
        self.ABeta42 = ABeta42
        self.tTau = tTau
        self.pTau = pTau
        self.sex = None
        self.death_age = None
        self.ed_lvl = None
        self.cog_stat = None
        self.age_symp_on = None
        self.age_diag = None 
        self.head_inj = None
        self.thal_score = None
        Patient.all_patients.append(self)

    def __repr__(self):
        return f"{self.DonorID} | sex: {self.sex} | ABeta40 {self.ABeta40} | tTau {self.tTau} | pTau {self.pTau} | Death Age {self.death_age} | Thal Score {self.thal_score}"

    def get_id(self):
        return self.DonorID

    def get_ABeta42(self):
        return self.ABeta42
    
    def get_thal(self):
        return self.thal_score
    
    def get_death_age(self):
        return self.death_age


    @classmethod
    def combine_data(cls, filename: str):
            with open(filename, encoding="utf8") as f:
                reader = csv.DictReader(f)
                rows_of_patients = list(reader)
                #for line in csv create object
                for row in range(len(rows_of_patients)):
                    if Patient.all_patients[row].DonorID == rows_of_patients[row]["Donor ID"]:
                        if rows_of_patients[row]["Sex"] != "":
                            Patient.all_patients[row].sex = rows_of_patients[row]["Sex"]

                        if rows_of_patients[row]["Age at Death"] != "":
                            Patient.all_patients[row].death_age = int(rows_of_patients[row]["Age at Death"])

                        if rows_of_patients[row]["Highest level of education"] != "":
                            Patient.all_patients[row].ed_lvl = rows_of_patients[row]["Highest level of education"]

                        if rows_of_patients[row]["Cognitive Status"] != "":
                            Patient.all_patients[row].cog_stat = rows_of_patients[row]["Cognitive Status"]

                        if rows_of_patients[row]["Age of onset cognitive symptoms"] != "":
                            Patient.all_patients[row].age_symp_on = int(rows_of_patients[row]["Age of onset cognitive symptoms"])

                        if rows_of_patients[row]["Age of Dementia diagnosis"] != "":
                            Patient.all_patients[row].age_diag = int(rows_of_patients[row]["Age of Dementia diagnosis"])

                        if rows_of_patients[row]["Known head injury"] != "":
                            Patient.all_patients[row].head_inj = rows_of_patients[row]["Known head injury"]

                        if rows_of_patients[row]["Thal"] != "":
                            Patient.all_patients[row].thal_score = int(rows_of_patients[row]["Thal"].split()[1])
            
                    else:
                        warnings.warn("IDs do not match.")
   
    @classmethod
    def instantiate_from_csv(cls, filename: str, other_file: str):
    #open csv and create list of all rows
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
            #for line in csv create object
            for row in rows_of_patients:
                Patient(
                    DonorID = row['Donor ID'],
                    ABeta40 = float(row['ABeta40 pg/ug']),
                    ABeta42 = float(row['ABeta42 pg/ug']),
                    tTau = float(row['tTAU pg/ug']),
                    pTau = float(row['pTAU pg/ug'])
                )
            Patient.all_patients.sort(key = Patient.get_id)
            Patient.combine_data(other_file)
#2) PRINT OUR LIST OF PATIENTS

# from patient import Patient
Patient.instantiate_from_csv('UpdatedLuminex.csv', 'UpdatedMetaData.csv')

for patient in Patient.all_patients:
    print(patient) #3) SORT OUR LIST OF PATIENTS

Patient.all_patients.sort(key=Patient.get_ABeta42, reverse=False)

for patient in Patient.all_patients:
    print(patient)
#4) BUILD DICTIONARIES TO DO SORTING AND SUB-SORTING

@classmethod
def sort_ed():
    for patient in Patient.all_patients:
        Patient.education_lvl.update({patient.ed_lvl: []})
    for patient in Patient.all_patients:
        Patient.education_lvl[patient.ed_lvl].append(patient)

@classmethod
def subsort_thal():
    for key in Patient.education_lvl:
        values = Patient.education_lvl.get(key)
        values.sort(key = Patient.get_thal)
        Patient.education_lvl.update({key: values})


#5) SORT THE SUB-LISTS WITHIN THE LIST AND PRINT IT

#from termcolor import colored

Patient.sort_ed()
Patient.subsort_thal()

for key in Patient.education_lvl:
    print(colored(key,"red"))
    for patient in Patient.education_lvl.get(key):
        print(patient)
    print()
#5) SORT THE SUB-LISTS WITHIN THE LIST AND PRINT IT

#from termcolor import colored

Patient.sort_ed()
Patient.subsort_thal()

for key in Patient.education_lvl:
    print(colored(key,"red"))
    for patient in Patient.education_lvl.get(key):
        print(patient)
    print()

#6) MAKE A FILTER TO PULL OUT PATIENTS WITH SPECIIFC ATTRIBUTES

@classmethod
def filter(cls, list, ABeta40:float ="any", ABeta42:float ="any", tTau:float= "any", pTau:float ="any", sex:str ="any", death_age:int ="any", ed_lvl:str ="any", cog_stat:str ="any", age_symp_on:int ="any", age_diag:int ="any", head_inj:str ="any", thal_score:int ="any"):
        all_patients = list
        remove_list = []
        attr_list = (
                    ABeta40,
                    ABeta42,
                    tTau,
                    pTau,
                    sex,
                    death_age,
                    ed_lvl,
                    cog_stat,
                    age_symp_on,
                    age_diag,
                    head_inj,
                    thal_score
                    )
        attr_name = (
                    "ABeta40",
                    "ABeta42",
                    "tTau",
                    "pTau",
                    "sex",
                    "death_age",
                    "ed_lvl",
                    "cog_stat",
                    "age_symp_on",
                    "age_diag",
                    "head_inj",
                    "thal_score"
                    )
        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient,attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)
                all_patients = [patient for patient in all_patients if patient not in remove_list]
                remove_list.clear()
        
        return all_patients

#7) USE OUR FILTER TO PULL OUT AND COUNT SUB-SETS OF PATIENTS THAT ARE FILTERED

fem_healty_patients = range(len(Patient.filter(Patient.all_patients, sex = "Female", cog_stat = "No dementia")))
male_healthy_patients = range(len(Patient.filter(Patient.all_patients, sex = "Male", cog_stat = "No dementia")))
fem_diseased_patients = range(len(Patient.filter(Patient.all_patients, sex = "Female", cog_stat = "Dementia")))
male_diseased_patients = range(len(Patient.filter(Patient.all_patients, sex = "Male", cog_stat = "Dementia")))

print(f'Female Healthy Patients = {len(fem_healty_patients)} | Male Healthy Patients = {len(male_healthy_patients)}')
print(f'Female Diseased Patients = {len(fem_diseased_patients)} | Male Diseased Patients = {len(male_diseased_patients)}')

#7) PLOT A BAR GRAPH OF THE SORTED DATA

from patient import Patient
from termcolor import colored
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import statistics 


# Patient.instantiate_from_csv('UpdatedLuminex.csv', 'UpdatedMetaData.csv')


# ====== CHANGED SECTION: TBI vs Alzheimer's (Dementia) using same method/structure ======

# Build 0/1 arrays for Dementia by TBI status ("Known head injury" == "Yes"/"No")
Dementia_TBI_yes = []
Dementia_TBI_no  = []

for patient in Patient.filter(Patient.all_patients, head_inj = "Yes"):
     # 1 if Dementia, 0 otherwise
     Dementia_TBI_yes.append(1 if str(patient.cog_stat).strip().lower().startswith("dementia") else 0)

for patient in Patient.filter(Patient.all_patients, head_inj = "No"):
     Dementia_TBI_no.append(1 if str(patient.cog_stat).strip().lower().startswith("dementia") else 0)

# Means (as percentages) and standard deviations (also in percentage points to match plot scale)
x_tbi_yes_bar = 100.0 * (statistics.mean(Dementia_TBI_yes) if len(Dementia_TBI_yes) > 0 else 0.0)
x_tbi_no_bar  = 100.0 * (statistics.mean(Dementia_TBI_no)  if len(Dementia_TBI_no)  > 0 else 0.0)

tbi_yes_stdev = 100.0 * (statistics.stdev(Dementia_TBI_yes) if len(Dementia_TBI_yes) > 1 else 0.0)
tbi_no_stdev  = 100.0 * (statistics.stdev(Dementia_TBI_no)  if len(Dementia_TBI_no)  > 1 else 0.0)

print(f'x_tbi_yes_bar = {x_tbi_yes_bar}, tbi_yes_stdev {tbi_yes_stdev}')
print(f'x_tbi_no_bar  = {x_tbi_no_bar}, tbi_no_stdev  {tbi_no_stdev}')

# Keep these unused ranges to mirror original structure (optional)
x_tbi_yes_vals = range(len(Dementia_TBI_yes))
x_tbi_no_vals  = range(len(Dementia_TBI_no))

tbi_cols = ['Head injury: Yes', 'Head injury: No']
mean_tbi_AD = [x_tbi_yes_bar, x_tbi_no_bar]
stdev_tbi_AD = [tbi_yes_stdev, tbi_no_stdev]
colors = ["pink", "blue"]
yerr = [np.zeros(len(mean_tbi_AD)), stdev_tbi_AD]

# "Same method": two-sample t-test (on 0/1 data) analogous to the ABeta42-by-sex code
if len(Dementia_TBI_yes) > 1 and len(Dementia_TBI_no) > 1:
    t_stat, p_val = stats.ttest_ind(Dementia_TBI_yes, Dementia_TBI_no)
    print("t-statistic:", t_stat)
    print("p-value:", p_val)
else:
    print("Not enough data in one of the groups to run a t-test.")

plt.bar(tbi_cols, mean_tbi_AD, yerr=yerr, capsize=10, color=["red", "blue"])
plt.title("Alzheimer’s (Dementia) Prevalence by TBI History")
plt.xlabel("Known Head Injury")
plt.ylabel("Percent with Dementia")
<<<<<<< Updated upstream
plt.show()
>>>>>>> Stashed changes
=======
plt.show()
>>>>>>> Stashed changes
