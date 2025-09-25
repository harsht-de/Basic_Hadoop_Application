# Heart Disease Dataset

## Overview
This is the basic flow which is created on Hadoop Ecosystems using MapReduce, HDFS, YARN.

Main aim for creating this flow is to see practical implementation of Hadoop and its components, also to perform distributed data processing.


Design of this Hadoop workflow:  
**Dataset → HDFS → MapReduce (Python Mapper/Reducer) → Results in HDFS**

---

## Dataset
We use a subset of the **Cleveland Heart Disease dataset** with the following attributes:

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
