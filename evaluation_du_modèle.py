# Faire des prédictions sur l'ensemble de test
predictions = model.transform(test)

# Calculer l'erreur RMSE
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE) = {rmse}")