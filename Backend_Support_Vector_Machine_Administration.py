import pandas as pd # Manage data (e.g. read from csv-files)
import numpy as np # Vectors and matrices
from sklearn.svm import SVC # Support Vector Machine Approach
from sklearn.multiclass import OneVsRestClassifier # Approach for multiple classes
from sklearn.model_selection import GridSearchCV # Grid Search to find best parameter combination
from sklearn.preprocessing import label_binarize # Convert textual classes in binary classes
from sklearn.model_selection import train_test_split # Split data set into a train and test set
from sklearn.model_selection import cross_val_score # For explanation please show internet
from sklearn.metrics import mean_squared_error # For calculating lost function
from Backend_Database_Read import read_train_test_data # Provide data from databases

# Function to evaluate SVM's performance using smart product data
def provide_svm_data():
      
      evaluation_values = []
      
      train_test_data = np.array(read_train_test_data())    # Read data from database into an array
      np.random.shuffle(train_test_data)                    # Random mix of data to avoid patterns 

      characteristics_without_clusters = train_test_data[:, :-2]              # Seperate independent variable: characteristics without clusters
      clusters = train_test_data[:,17:18]                                     # Seperate independent variable: clusters for binarization
      success_classes = train_test_data[:,18:19]                              # Seperate dependent variable: smart ojects' success (i.e. Google search query) 
      clusters_binary = label_binarize(clusters, classes=[0, 1, 2, 3])/4      # Binarization of clusters
      
      
      characteristics_with_clusters_binary = np.concatenate((characteristics_without_clusters, clusters_binary), axis=1) # Merge characteristics without clusters and binarized clusters

      # Split of data in test and train
      characteristics_with_clusters_train, characteristics_with_clusters_test, success_classes_train, success_classes_test = train_test_split(characteristics_with_clusters_binary, success_classes, test_size=0.3, shuffle=True, stratify=success_classes)
      characteristics_without_clusters_train = characteristics_with_clusters_train[:,:17]
      characteristics_without_clusters_test = characteristics_with_clusters_test[:,:17]

      
      ##############################################################

      # Train model and evaluate it with RMSE: Without clusters
      svm_rmse_without_clusters = OneVsRestClassifier(SVC(kernel="poly"))
      svm_rmse_without_clusters.fit(characteristics_without_clusters_train, success_classes_train)
      success_predict_without_clusters = svm_rmse_without_clusters.predict(characteristics_without_clusters_test)

      mse_without_clusters = mean_squared_error(success_predict_without_clusters, success_classes_test)
      rmse_without_clusters = np.sqrt(mse_without_clusters)
      print("RMSE without Clusters: ", rmse_without_clusters)
      print("---")
      evaluation_values.append(rmse_without_clusters)

      # Train model and evaluate it with RMSE: With clusters
      svm_rmse_with_clusters = OneVsRestClassifier(SVC(kernel="poly"))
      svm_rmse_with_clusters.fit(characteristics_with_clusters_train, success_classes_train)
      success_predict_with_clusters = svm_rmse_with_clusters.predict(characteristics_with_clusters_test)

      mse_with_clusters = mean_squared_error(success_predict_with_clusters, success_classes_test)
      rmse_with_clusters = np.sqrt(mse_with_clusters)
      print("RMSE with Clusters: ", rmse_with_clusters)
      print("---")
      evaluation_values.append(rmse_with_clusters)


      ##############################################################

      # Train and evaluate model with cross validation based on RMSE: Without clusters  
      svm_cv_rmse_without_clusters = OneVsRestClassifier(SVC(kernel="poly"))
      cv_mse_without_clusters = cross_val_score(svm_cv_rmse_without_clusters, characteristics_without_clusters, success_classes, scoring="neg_mean_squared_error", cv=8)
      cv_rmse_without_clusters = np.sqrt(-cv_mse_without_clusters)
      print("Scores RMSE Without Clusters: ", cv_rmse_without_clusters)
      print("Mean: ", cv_rmse_without_clusters.mean())
      print("Standard Deviation: ", cv_rmse_without_clusters.std())
      print("---")
      evaluation_values.append(cv_rmse_without_clusters.mean())

      # Train and evaluate model with cross validation based on RMSE: With clusters  
      svm_cv_rmse_with_clusters = OneVsRestClassifier(SVC(kernel="poly"))
      cv_mse_with_clusters = cross_val_score(svm_cv_rmse_with_clusters, characteristics_with_clusters_binary, success_classes, scoring="neg_mean_squared_error", cv=8)
      cv_rmse_with_clusters = np.sqrt(-cv_mse_with_clusters)
      print("Scores RMSE With Clusters: ", cv_rmse_with_clusters)
      print("Mean: ", cv_rmse_with_clusters.mean())
      print("Standard Deviation: ", cv_rmse_with_clusters.std())
      print("---")
      evaluation_values.append(cv_rmse_with_clusters.mean())

      ##############################################################

      # Train and evaluate model with cross validation based on accuracy-score: Without clusters 
      svm_cv_score_without_clusters = OneVsRestClassifier(SVC(kernel="poly"))
      cv_score_without_clusters = cross_val_score(svm_cv_score_without_clusters, characteristics_without_clusters, success_classes, scoring="accuracy", cv=8)
      print("Score Without Clusters: ", cv_score_without_clusters)
      print("Mean: ", cv_score_without_clusters.mean())
      print("Standard Deviation: ", cv_score_without_clusters.std())
      print("---")
      evaluation_values.append(cv_score_without_clusters.mean())

      # Train and evaluate model with cross validation based on accuracy-score: With clusters 
      svm_cv_score_with_clusters = OneVsRestClassifier(SVC(kernel="poly"))
      cv_score_with_clusters = cross_val_score(svm_cv_score_with_clusters, characteristics_with_clusters_binary, success_classes, scoring="accuracy", cv=8)
      print("Score With Clusters: ", cv_score_with_clusters)
      print("Mean: ", cv_score_with_clusters.mean())
      print("Standard Deviation: ", cv_score_with_clusters.std())
      print("---")
      evaluation_values.append(cv_score_with_clusters.mean())
     
      ##############################################################
      
      # Grid Search: Without Clusters
      print("Grid Search: Without Clusters")
      # Poly
      svm_grid_search_poly = OneVsRestClassifier(SVC())
      parameters_poly = {               
                  "estimator__kernel": ["poly"],
                  "estimator__C": [8,10,12,14,16,18,20,22,24,26,28,30,32],
                  "estimator__degree": [1, 2, 3, 4, 5],
                  "estimator__gamma": [3, 4,5],
                  "estimator__coef0": [0,2]
                  }
      
      grid_search = GridSearchCV(svm_grid_search_poly, parameters_poly, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(characteristics_without_clusters, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      # RBF
      svm_grid_search_rbf = OneVsRestClassifier(SVC())
      parameters_rbf = {
                  "estimator__kernel": ["rbf"],
                  "estimator__C": [1,2,4,6,8,10,12,14, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
                  "estimator__gamma": [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
                  }
      
      grid_search = GridSearchCV(svm_grid_search_rbf, parameters_rbf, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(characteristics_without_clusters, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      ##############################################################

      # Grid Search: With clusters
      print("Grid Search: With Clusters")

      # Poly
      grid_search = GridSearchCV(svm_grid_search_poly, parameters_poly, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(characteristics_with_clusters_binary, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      # RBF
      grid_search = GridSearchCV(svm_grid_search_rbf, parameters_rbf, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(characteristics_with_clusters_binary, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      ##############################################################

      # Grid Search after feature reduction: Without Clusters
      print("Grid Search after Feature Reduction: Without Clusters")

      sensing = train_test_data[:,0:1]
      autonomy = train_test_data[:,3:4]
      direction = train_test_data[:,4:5]
      source_cloud = train_test_data[:,12:13]
      data_usage = train_test_data[:,13:14]
      offline_function = train_test_data[:,14:15]
      value_proposition = train_test_data[:,15:16]

      dataset_reduced_without_clusters = np.concatenate((autonomy, data_usage), axis=1)
      
      # Poly
      grid_search = GridSearchCV(svm_grid_search_poly, parameters_poly, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(dataset_reduced_without_clusters, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      # RBF
      grid_search = GridSearchCV(svm_grid_search_rbf, parameters_rbf, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(dataset_reduced_without_clusters, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      # Grid Search after feature reduction: With Clusters
      print("Grid Search after Feature Reduction: With Clusters")

      dataset_reduced_with_clusters = np.concatenate((autonomy, data_usage, clusters_binary), axis=1)

      # Poly
      grid_search = GridSearchCV(svm_grid_search_poly, parameters_poly, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(dataset_reduced_with_clusters, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      # RBF
      grid_search = GridSearchCV(svm_grid_search_rbf, parameters_rbf, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(dataset_reduced_with_clusters, success_classes)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      return(evaluation_values)


def provide_cluster_affiliation():

      evaluation_values = []
      
      train_test_data = np.array(read_train_test_data())    # Read data from database into an array
      np.random.shuffle(train_test_data)                    # Random mix of data to avoid patterns 

      characteristics_without_clusters = train_test_data[:, :-2]              # Seperate independent variable: characteristics without clusters
      clusters = train_test_data[:,17:18]                                     # Seperate independent variable: clusters for binarization
      # clusters_binary = label_binarize(clusters, classes=[0, 1, 2, 3])/4      # Binarization of clusters
      
      # Poly
      svm_grid_search_poly = OneVsRestClassifier(SVC())
      parameters_poly = {               
                  "estimator__kernel": ["poly"],
                  "estimator__C": [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14],
                  "estimator__degree": [1, 2, 3, 4, 5],
                  "estimator__gamma": [3, 4,5],
                  "estimator__coef0": [0,2]
                  }

      # Poly
      grid_search = GridSearchCV(svm_grid_search_poly, parameters_poly, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(characteristics_without_clusters, clusters)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      # RBF
      svm_grid_search_rbf = OneVsRestClassifier(SVC())
      parameters_rbf = {
                  "estimator__kernel": ["rbf"],
                  "estimator__C": [1,2,4,6,8,10,12,14, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
                  "estimator__gamma": [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45]
                  }

      # RBF
      grid_search = GridSearchCV(svm_grid_search_rbf, parameters_rbf, cv=8, scoring="accuracy", return_train_score=True)
      grid_search.fit(characteristics_without_clusters, clusters)
      
      print(grid_search.best_params_)
      print(grid_search.best_score_)
      print(grid_search.refit_time_)
      evaluation_values.append(grid_search.best_params_)
      evaluation_values.append(grid_search.best_score_)

      return(evaluation_values)

