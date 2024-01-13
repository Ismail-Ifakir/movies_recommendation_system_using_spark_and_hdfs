# Faire des recommandations pour tous les utilisateurs
userRecs = model.bestModel.recommendForAllUsers(10)

# Afficher les recommandations pour un utilisateur spécifique (remplacez user_id par l'ID de l'utilisateur)
user_id = 1
specific_user_recs = userRecs.filter(userRecs["userId"] == user_id).select("recommendations")

# Afficher les titres de films recommandés
recommended_movie_ids = specific_user_recs.collect()[0]["recommendations"]["movieId"]
recommended_movies = movies.filter(movies["movieId"].isin(recommended_movie_ids)).select("title")

recommended_movies.show()