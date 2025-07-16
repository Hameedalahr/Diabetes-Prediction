# 🩺 Diabetes Prediction using SVM

This project is a part of my Machine Learning learning phase. It involves building a classification model to predict whether a person is likely to have diabetes based on various medical parameters. The model uses a **Support Vector Machine (SVM)** classifier and is trained on the **Pima Indians Diabetes Dataset**.

---

## 📁 Dataset
- **Source**: Pima Indians Diabetes Database
- **Features**:
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
- **Target**: Outcome (0 - Non-diabetic, 1 - Diabetic)

---

## 📌 Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn

---

## 🔧 Project Workflow

1. **Data Loading**
   - Loaded the dataset using Pandas.
2. **Data Preprocessing**
   - Checked for missing values and found no zero entries.
   - Standardized the data using `StandardScaler`.
   - Split data into training and testing sets with `train_test_split` and `stratify`.
3. **Model Building**
   - Used **SVM classifier** from Scikit-learn.
   - Trained the model on the training data.
4. **Evaluation**
   - Evaluated the model using:
     - Accuracy Score
---

## 📈 Results

- The model performed well in distinguishing diabetic vs non-diabetic cases.
- Accuracy: *(77.8%)*

---

## 💡 Learnings

- Importance of data preprocessing
- Stratification in train-test split
- How SVM works and its advantages in classification tasks
- Performance evaluation using classification metrics

---

