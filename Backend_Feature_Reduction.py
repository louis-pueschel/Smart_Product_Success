from Backend_Database_Read import read_train_test_data # Provide data from databases
import csv
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import label_binarize # Convert textual classes in binary classes


def provide_pca_results():

      train_test_data = np.array(read_train_test_data())                      # Read data from database into an array
      characteristics_without_clusters = train_test_data[:, :-2]              # Seperate independent variable: characteristics without clusters
      success_classes = train_test_data[:,18:19]                              # Seperate dependent variable: smart ojects' success (i.e. Google search query) 

      dataset = np.concatenate((characteristics_without_clusters, success_classes), axis=1) # Merge characteristics without clusters and binarized clusters

      # Principal Component Analysis
      pca = PCA(n_components=18)
      pca_fitted = pca.fit(dataset)      
      
      # Write PCA results into a CSV file      
      with open("Principal_Component_Analysis_Results.csv", mode="w") as pca_file:

            pca_writer = csv.writer(pca_file, delimiter=",")
            pca_writer.writerow(["Explained Variance Ratios:"])
            pca_writer.writerow(pca_fitted.explained_variance_ratio_)
            pca_writer.writerow(["Principal Component Analysis:"])
            pca_writer.writerows(pca_fitted.components_)
      
      # Return components and variance ratio
      return(pca_fitted.components_, pca_fitted.explained_variance_ratio_)
      


