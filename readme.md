# Diabetes Prediction using a Decision Tree Classifier

This project trains a scikit-learn Decision Tree classifier to predict the `Outcome` label in the supplied diabetes dataset. It also creates a simple exploratory chart showing the sum of pregnancies grouped by age.

## Dataset

The repository includes `diabetes.csv` with these columns:

- `Pregnancies`
- `Glucose`
- `BloodPressure`
- `SkinThickness`
- `Insulin`
- `BMI`
- `DiabetesPedigreeFunction`
- `Age`
- `Outcome` — target label

## Workflow

1. Load the CSV with pandas and print dataframe information.
2. Group by `Age`, sum `Pregnancies`, and display a bar chart.
3. Use all columns except `Outcome` as features.
4. Split into training and test sets with `random_state=24` and scikit-learn's default test fraction.
5. Train `DecisionTreeClassifier()` with its default parameters.
6. Predict the test labels.
7. Create a Graphviz representation of the fitted tree.

## Technology

- Python
- pandas
- Matplotlib
- scikit-learn
- Graphviz and the Python `graphviz` package

## Run locally

```bash
git clone https://github.com/KARTHIKEYAN-GHOST/Diabetes_Prediction_using_DecisionTreeClassifier.git
cd Diabetes_Prediction_using_DecisionTreeClassifier

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pandas matplotlib scikit-learn graphviz
```

Install the Graphviz system executable as well. On Ubuntu/Debian:

```bash
sudo apt install graphviz
```

The script currently contains an absolute Windows path to `diabetes.csv`. Replace that `read_csv` path with:

```python
df = pd.read_csv("diabetes.csv")
```

Then run:

```bash
python DecisionTree_Classifier.py
```

## Output

The script displays the exploratory chart and constructs a Graphviz tree object. It currently does not print an accuracy score or render the tree to a file.

## Limitations

- The current script does not evaluate the model with a metric.
- Decision-tree depth and other parameters are not tuned.
- Missing-value and zero-value handling are not included.
- This is an educational example, not a medical diagnostic tool. Do not use its predictions for clinical decisions.
