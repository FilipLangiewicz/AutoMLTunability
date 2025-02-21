# AutoMLTunability 

The **AutoML_PRO1: Tunability** project focuses on studying the tunability of hyperparameters in selected machine learning algorithms for binary classification. We analyzed three models:

- **DecisionTreeClassifier** (scikit-learn)
- **KNeighborsClassifier** (scikit-learn)
- **XGBoost** (xgboost)

The study used **four different datasets** and two methods for sampling hyperparameter points:
- **Random Search** (RandomizedSearchCV from scikit-learn)
- **Bayes Search** (BayesSearchCV from scikit-optimize)

The experiment is based on the paper: *Tunability: Importance of Hyperparameters of Machine Learning Algorithms*.

## Datasets

The experiments were conducted on the following datasets:

1. **Credit Approval (credit)** – 690 rows, 16 columns (credit card data)
2. **Go To College (college)** – 1000 rows, 11 columns (synthetic data on educational decisions)
3. **Pima Indians Diabetes Database (diabetes)** – 768 rows, 9 columns (medical data)
4. **Palmer Penguins (penguins)** – 274 rows, 7 columns (biological data on penguins)

## Models and Hyperparameters Studied

### **1. DecisionTreeClassifier**
- `criterion`: [`gini`, `entropy`, `log_loss`]
- `max_depth`: [1, 29]
- `max_leaf_nodes`: [10, 90]

### **2. KNeighborsClassifier**
- `n_neighbors`: [1, 30]
- `weights`: [`uniform`, `distance`]
- `metric`: [`euclidean`, `manhattan`, `chebyshev`, `minkowski`]

### **3. XGBoost**
- `booster`: [`gbtree`, `gblinear`, `dart`]
- `learning_rate`: [0.0001, 0.3]
- `max_depth`: [3, 10]
- `lambda`: [2^-10, 2^10]

## Experiment Methodology

For each model, we optimized hyperparameters on four datasets using two methods:
- **RandomizedSearchCV** – random hyperparameter sampling
- **BayesSearchCV** – probabilistic optimization method  

Each iteration used **5-fold cross-validation**, and **200 iterations** were performed for each method.

## Results

1. **Best Model**:  
   - **XGBoost** achieved the highest F1 scores on most datasets, especially on more complex datasets (`credit`, `college`).  
   - DecisionTree and KNeighbors obtained competitive results but with higher variance.  

2. **Algorithm Tunability**:  
   - XGBoost and DecisionTree exhibited **higher tunability** with Bayes Search optimization.  
   - KNeighbors showed **lower tunability**, meaning hyperparameter selection had less impact on model performance.  

3. **Comparison of Optimization Methods**:  
   - **Bayes Search** provided **better result stabilization** and **faster convergence**, especially for DecisionTree and XGBoost.  
   - **Random Search** produced more unstable results with a limited number of iterations.  

4. **Number of Iterations for Stable Results**:  
   - **Bayes Search required fewer iterations** to achieve stable results compared to Random Search.  

## Conclusions

- The choice of **optimization method** significantly impacts classification performance and model tunability.  
- **XGBoost** is more sensitive to hyperparameter tuning than KNeighbors.  
- **Bayes Search** is more effective than Random Search with a limited number of iterations.  
- The stability of results achieved with Bayes Search suggests that **advanced hyperparameter optimization methods** should be used in real-world applications.  

## Authors

- [Natalia Choszczyk](https://github.com/nataliachoszczyk)
- [Filip Langiewicz](https://github.com/FilipLangiewicz)

## References

- Philipp Probst, Anne-Laure Boulesteix, Bernd Bischl – *Tunability: Importance of Hyperparameters of Machine Learning Algorithms*
- scikit-learn and XGBoost documentation  
