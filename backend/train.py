from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Подготовьте ваши данные
X, y = load_your_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Обучение модели
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Сохраните модель
joblib.dump(model, 'your_model.pkl')