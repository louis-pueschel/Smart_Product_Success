import numpy as np # Vectors and matrices
from sklearn.svm import SVC # Support Vector Machine Approach
from sklearn.multiclass import OneVsRestClassifier # Approach for multiple classes
from sklearn.preprocessing import label_binarize # Convert textual classes in binary classes
from Backend_Database_Read import read_train_test_data # Provide data from databases

# Function to predict the success of the user's smart product/input
def evaluate_user_input(user_input):
      
      train_test_data = np.array(read_train_test_data())                      # Read data from database into an array
      np.random.shuffle(train_test_data)                                      # Random mix of data to secure a real world situation and to avoid patterns 

      characteristics_without_clusters = train_test_data[:, :-2]              # Seperate independent variable: characteristics without clusters
      clusters = train_test_data[:,17:18]                                     # Seperate independent variable: clusters for binarization
      success_classes = train_test_data[:,18:19]                              # Seperate dependent variable: smart ojects' success (i.e. Google search query) 
      clusters_binary = label_binarize(clusters, classes=[0, 1, 2, 3])/4      # Binarization of clusters
      
      sensing = train_test_data[:,0:1]
      autonomy = train_test_data[:,3:4]
      direction = train_test_data[:,4:5]
      source_cloud = train_test_data[:,12:13]
      data_usage = train_test_data[:,13:14]
      offline_function = train_test_data[:,14:15]
      value_proposition = train_test_data[:,15:16]
      
      characteristics_with_clusters_binary = np.concatenate((characteristics_without_clusters, clusters_binary), axis=1) # Merge characteristics without clusters and binarized clusters           
            
      characteristics_reduced = np.concatenate((autonomy, data_usage), axis=1)
      
      user_input_autonomy = user_input[0,3]
      user_input_data_usage = user_input[0,-4]
      
      user_input_reduced = []
      user_input_reduced.append(user_input_autonomy)
      user_input_reduced.append(user_input_data_usage)
      user_input_reduced = np.reshape(user_input_reduced, (1, -1))

      # Predict the success of the user's smart product/input 
      svm_poly_without_clusters = OneVsRestClassifier(SVC(kernel="poly", C=10, gamma=4, degree=1, coef0=2))
      svm_poly_without_clusters.fit(characteristics_reduced, success_classes)
      success = svm_poly_without_clusters.predict(user_input_reduced)
      
      
      # Predict the type of the user's smart product/input 
      svm_rbf_clusters = OneVsRestClassifier(SVC(kernel="rbf", C=1, gamma=1))
      svm_rbf_clusters.fit(characteristics_without_clusters, clusters)
      cluster_affilication = svm_rbf_clusters.predict(user_input)

      return(success, cluster_affilication)
      
      