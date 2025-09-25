## Cleveland Disease Data - **_BASIC_** Hadoop MapReduce Flow

## Project Overview
This basic flow was created to understand practical implementation of Hadoop and its Components (HDFS, YARN, MapReduce).
  
Performed **distributed data processing**  to understand MapReduce Model and its working.

Design of this Hadoop workflow:  
**Dataset → HDFS → MapReduce (Python Mapper/Reducer) → Results in HDFS**

---

## 📂 Dataset
We use a subset of the **Heart Disease dataset** with the following attributes:

| Column      | Description                                |
|-------------|--------------------------------------------|
| age         | Age of patient                             |
| sex         | Gender (1 = Male, 0 = Female)              |
| cp          | Chest pain type                            |
| trestbps    | Resting blood pressure                     |
| chol        | Serum cholesterol (mg/dl)                  |
| fbs         | Fasting blood sugar                        |
| restecg     | Resting ECG results                        |
| thalach     | Maximum heart rate achieved                |
| exang       | Exercise-induced angina                    |
| oldpeak     | Depression induced by exercise             |
| slope       | Slope of the ST segment                    |
| ca          | Number of major vessels colored by fluoroscopy |
| thal        | Thalassemia test result                    |
| num         | Heart disease diagnosis (0 = no disease, 1-3 = severity) |

---


**JOB Execution LOGS in CLUSTER MANAGER**->_Yarn UI_
<img width="1894" height="832" alt="Screenshot 2025-09-25 182519" src="https://github.com/user-attachments/assets/e0576cc2-80d1-438e-bbe4-1e802807b176" />




**HDFS File Structure _(input, output, tmp)_**->_HDFS UI_
<img width="1496" height="763" alt="Screenshot 2025-09-25 182602" src="https://github.com/user-attachments/assets/2b795b03-028f-4b90-bf03-880515bf7991" />
