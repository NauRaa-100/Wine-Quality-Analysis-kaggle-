#  Wine Quality Analysis  

##  Overview  
This project analyzes the **Wine Quality Dataset (Red Wine)**. 
- **Source**: [Kaggle Titanic Dataset:/](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)
The goal is to explore the dataset, clean and optimize it, and understand which chemical features most influence **wine quality**.  

- **Rows:** 1599  
- **Features:** 12  
- **Target:** `quality` (integer, 0–10)  

---

##  Steps in the Analysis  

###  Data Cleaning  
- No missing values found.  
- **240 duplicated rows** removed.  

###  Memory Optimization  
- Converted numerical columns to `float16` and target to `int32`.  
- Reduced memory usage significantly.  

###  Target (Quality) Distribution  
- Most wines rated **5 or 6**.  
- Very few wines rated **3 or 8**.  
- Dataset is **imbalanced**.  

### Correlation Analysis  
- **Alcohol** → Strong positive correlation with quality.  
- **Volatile acidity** → Strong negative correlation with quality.  
- Other features show weaker influence.  

---

##  Visualizations  
- **Distribution of wine quality (Countplot).**  
- **Heatmap of correlations between all numeric features.**  
- **Barplot of correlations with the `quality` target.**  

---

##  Key Findings  
- Alcohol content increases the chances of higher quality scores.  
- High volatile acidity decreases wine quality.  
- Other factors (pH, sulphates, residual sugar) have smaller impacts.  

---

##  Next Steps  
- Apply **Machine Learning models** (e.g., Regression, Classification) to predict wine quality.  
- Handle **class imbalance** (resampling or weighting).  
- Feature engineering: create new variables or combine existing ones.  
