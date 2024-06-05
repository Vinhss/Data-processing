# view data xem chua cai gi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dete_survey = pd.read_csv("C:\\Users\\Admin\\Desktop\\AdPython\\Data_processing\\dete-exit-survey-january-2014.csv", na_values='Not Stated')

dete_survey.info()

dete_survey.head()

# view value cua cac cot xem co missing data ko

print(dete_survey["Classification"].value_counts())

# xem so luong missing data

print(dete_survey.isnull().sum())

# khi minh kham data xong se co nhung nhan xet gi

print(dete_survey)

# bo nhung cot qua nhieu missing data
to_drop_dete = dete_survey.columns[50:]
dete_survey_updated = dete_survey.drop(to_drop_dete, axis=1)

print(dete_survey_updated.info())

# chuan hoa theo kieu nhu sau: 'abc_def_klm'
dete_survey_updated.columns = dete_survey_updated.columns.str.lower().str.strip().str.replace(' ', '_')
print(dete_survey_updated.info())

# gom gia tri cua nhung truong tuong tu nhau lai thanh 1 Resignation
print(dete_survey_updated["separationtype"].value_counts())

dete_survey_updated["separationtype"] = dete_survey_updated["separationtype"].str.split('-').str[0]
print(dete_survey_updated["separationtype"].value_counts())

# tach gia tri cua truong Resignation ra rieng
dete_Resignation = dete_survey_updated[dete_survey_updated["separationtype"] == 'Resignation'].copy()

print(dete_Resignation["cease_date"].value_counts())

# chuyen cot date thanh year
dete_Resignation["cease_date"] = dete_Resignation["cease_date"].str.split("/").str[-1].astype("float")
print(dete_Resignation["cease_date"].value_counts())

print(dete_Resignation["dete_start_date"].value_counts())

dete_Resignation["institute_service"] = dete_Resignation["cease_date"] - dete_Resignation["dete_start_date"]

print(dete_Resignation["institute_service"].value_counts())

# search Job Dissafisfaction
columns_name = ["job_dissatisfaction", "dissatisfaction_with_the_department", "physical_work_environment",
                "lack_of_recognition", "lack_of_job_security", "work_location", "employment_conditions",
                "work_life_balance", "workload"]

dete_Resignation["dissatisfied"] = dete_Resignation[columns_name].any(axis=1, skipna=False)
print(dete_Resignation["dissatisfied"].value_counts())


# viet ham de chuyen doi so nam kinh nghim thanh chac danh tuong ung

def map_career_stage(val):
    if pd.isnull(val):
        return np.nan
    elif val < 3:
        return "New"
    elif val >= 3 and val <= 6:
        return "Experienced"
    elif val >= 7 and val <= 10:
        return "Established"
    else:
        return "Veteran"


dete_Resignation["service_cat"] = dete_Resignation["institute_service"].apply(map_career_stage)

print(dete_Resignation["service_cat"].value_counts())

# tinh phan tram cua dissatisfied nhan vien tren moi service_cat

dissatisfaction_pct = dete_Resignation.pivot_table(index="service_cat", values="dissatisfied")

print(dissatisfaction_pct)

dissatisfaction_pct.plot(kind="bar", legend=False, title="Percentage of resigned employees due dissatisfaction", rot=0)

dissatisfaction_employee = dete_Resignation.pivot_table(index="employment_status", values="dissatisfied")

dissatisfaction_employee.plot(kind="bar", legend=False, title="types of employeement correlation of dissatisfaction",
                              rot=45)

dissatisfaction_gender = dete_Resignation.pivot_table(index="gender", values="dissatisfied")

dissatisfaction_gender.plot(kind="bar", legend=False, title="gender correlation of dissatisfaction", rot=45)
plt.show()

# mapping do tuoi sang chuan sau day

# <20 ; 21-25; 26-30; 31-35; 36-40; 41-45; 46-50; 51-55; older

# col_rename = {'Record ID': 'id',
# 'CESSATION YEAR': 'cease_date',
# 'Reason for ceasing employment': 'separationtype',
# 'Gender. What is your Gender?': 'gender',
# 'CurrentAge. Current Age': 'age',
# 'Employment Type. Employment Type': 'employment_status',
# 'Classification. Classification': 'position',
# 'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service',
# 'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'}
