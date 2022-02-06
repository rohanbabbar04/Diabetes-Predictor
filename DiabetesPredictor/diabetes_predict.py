import pandas as pd
import pickle

diabetes_df = pd.read_csv('data/diabetes.csv', index_col=0)
X = diabetes_df.drop(columns={'Outcome'})
y = diabetes_df.Outcome

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

from sklearn.preprocessing import MinMaxScaler
min_max = MinMaxScaler()
X_train = min_max.fit_transform(X_train)
X_test = min_max.transform(X_test)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='liblinear')
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))

pickle.dump(logreg, open('model.pkl', 'wb'))
