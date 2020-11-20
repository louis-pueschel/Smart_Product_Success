#-*- coding: utf-8 -*-
import os
from tkinter import * # Tkinter for drawining interfaces
from tkinter import ttk  
from ttkthemes import themed_tk as tk # Special theme for buttons. Theme must be downloaded under https://ttkthemes.readthedocs.io/en/latest/themes.html. Further explanations https://docs.python.org/3/library/tkinter.ttk.html
from tkinter import messagebox
from Backend_Database_Load import load_data_into_database # Import function to load data into databases
from Backend_Feature_Reduction import provide_pca_results
from Backend_Support_Vector_Machine_Administration import provide_svm_data, provide_cluster_affiliation
from Backend_Database_Create_New import backend_create_new_database
from Frontend_Database_Create_New import frontend_create_new_database

# Delete database
def delete_database():
    os.remove("smart_product.db")
    messagebox.showinfo(title = "Confirmation", message = "Database successfully deleted!")

# Create a new database
def create_database():
    backend_create_new_database()
    frontend_create_new_database()
    messagebox.showinfo(title = "Confirmation", message = "Database successfully created!")

# Function to write the SVM's evaluation results into the labels 
def get_svm_data():
    
    # Call function to provide/get the results from the evaluation file      
    evaluation_val = provide_svm_data()
       
    ## Parameters without Clusters
    # Poly Parameters: Without Clusters
    poly_c_without_clusters.configure(text=round(evaluation_val[6]["estimator__C"], 2))
    poly_d_without_clusters.configure(text=round(evaluation_val[6]["estimator__degree"], 2))
    poly_gamma_without_clusters.configure(text=round(evaluation_val[6]["estimator__gamma"], 2))
    poly_r_without_clusters.configure(text=round(evaluation_val[6]["estimator__coef0"], 2))

    # RBF Parameters: Without Clusters
    rbf_c_without_clusters.configure(text=round(evaluation_val[8]["estimator__C"], 2))
    rbf_gamma_without_clusters.configure(text=round(evaluation_val[8]["estimator__gamma"], 2))
    
    # Poly Parameters after Feature Reduction: Without Clusters
    poly_fr_c_without_clusters.configure(text=round(evaluation_val[14]["estimator__C"], 2))
    poly_fr_d_without_clusters.configure(text=round(evaluation_val[14]["estimator__degree"], 2))
    poly_fr_gamma_without_clusters.configure(text=round(evaluation_val[14]["estimator__gamma"], 2))
    poly_fr_r_without_clusters.configure(text=round(evaluation_val[14]["estimator__coef0"], 2))

    # RBF Parameters after Feature Reduction: Without Clusters
    rbf_fr_c_without_clusters.configure(text=round(evaluation_val[16]["estimator__C"], 2))
    rbf_fr_gamma_without_clusters.configure(text=round(evaluation_val[16]["estimator__gamma"], 2))

    ## Parameters with Clusters
    # Poly Parameters: With Clusters
    poly_c_with_clusters.configure(text=round(evaluation_val[10]["estimator__C"], 2))
    poly_d_with_clusters.configure(text=round(evaluation_val[10]["estimator__degree"], 2))
    poly_gamma_with_clusters.configure(text=round(evaluation_val[10]["estimator__gamma"], 2))
    poly_r_with_clusters.configure(text=round(evaluation_val[10]["estimator__coef0"], 2))

    # RBF Parameters: With Clusters
    rbf_c_with_clusters.configure(text=round(evaluation_val[12]["estimator__C"], 2))
    rbf_gamma_with_clusters.configure(text=round(evaluation_val[12]["estimator__gamma"], 2))
    
    # Poly Parameters after Feature Reduction: With Clusters
    poly_fr_c_with_clusters.configure(text=round(evaluation_val[18]["estimator__C"], 2))
    poly_fr_d_with_clusters.configure(text=round(evaluation_val[18]["estimator__degree"], 2))
    poly_fr_gamma_with_clusters.configure(text=round(evaluation_val[18]["estimator__gamma"], 2))
    poly_fr_r_with_clusters.configure(text=round(evaluation_val[18]["estimator__coef0"], 2))

    # RBF Parameters after Feature Reduction: With Clusters
    rbf_fr_c_with_clusters.configure(text=round(evaluation_val[20]["estimator__C"], 2))
    rbf_fr_gamma_with_clusters.configure(text=round(evaluation_val[20]["estimator__gamma"], 2))

    ## Scores without Clusters
    RMSE_without_cluster.configure(text=round(evaluation_val[0], 2))
    Score_RMSE_without_cluster.configure(text=round(evaluation_val[2], 2))
    Score_without_cluster.configure(text=round(evaluation_val[4], 2))
    poly_without_cluster.configure(text=round(evaluation_val[7], 2))
    rbf_without_cluster.configure(text=round(evaluation_val[9], 2))
    poly_fr_without_cluster.configure(text=round(evaluation_val[15], 2))
    rbf_fr_without_cluster.configure(text=round(evaluation_val[17], 2))

    ## Scores with Clusters
    RMSE_with_cluster.configure(text=round(evaluation_val[1], 2))
    Score_RMSE_with_cluster.configure(text=round(evaluation_val[3], 2))
    Score_with_cluster.configure(text=round(evaluation_val[5], 2))
    poly_with_cluster.configure(text=round(evaluation_val[11], 2))
    rbf_with_cluster.configure(text=round(evaluation_val[13], 2))
    poly_fr_with_cluster.configure(text=round(evaluation_val[19], 2))
    rbf_fr_with_cluster.configure(text=round(evaluation_val[21], 2))

# Draws results of feature reduction (i.e. Principal Component Analysis)
def show_results_feature_reduction(): 

    pca_components, pca_variance_ratios = provide_pca_results()
      
    # Toplevel object which will be treated as a new window 
    fr_results = Toplevel(root)
  
    # Sets the title of the Toplevel widget 
    fr_results.title("Results Feature Reduction: Principal Component Analysis")
    
    # Frame
    frame_pca = Frame(fr_results)
    frame_pca.grid(padx=30, pady=30, sticky=N+S+W+E)
  
    # Header Names
    header_names = ["Nr. Component", "Variance", "sensing", "acting_own","acting_inter", "autonomy", "direction", 
        "multiplicity", "partner_user", "partner_business",	"partner_thing", "source_state", "source_context", "source_usage", "source_cloud",	
        "data_usage", "offline_func", "value_proposition", "ecosystem", "success_class"
        ]

    # Draw Header Names
    for a in range(len(header_names)):
        pca_labels = Label(frame_pca, text=header_names[a], bg="white", font='Helvetica 8 bold', borderwidth=1, relief="solid")
        pca_labels.grid(row=0, column=a, ipadx=1, ipady=1, sticky=N+S+W+E)

    for b in range(len(pca_components)):
        
        # Draws PCA's component number
        pca_labels = Label(frame_pca, text=b+1, bg="white", font='Helvetica 8 bold', borderwidth=1, relief="solid")
        pca_labels.grid(row=b+1, column=0, ipadx=5, ipady=2, sticky=N+S+W+E)

        # Draws variance ratios
        pca_labels = Label(frame_pca, text=round(pca_variance_ratios[b],2), bg="white", font='Helvetica 8 bold', borderwidth=1, relief="solid")
        pca_labels.grid(row=b+1, column=1, ipadx=5, ipady=2, sticky=N+S+W+E)

        # Set colour if variance ratio is higher than a defined threshold
        if pca_variance_ratios[b] >= 0.1:
                pca_labels.configure(bg="SpringGreen2")
    
        # Draws PCA values for each component
        for c in range(len(pca_components)):
                
                pca_labels = Label(frame_pca, text=round(pca_components[b,c],2), bg="white", font='Helvetica 8', borderwidth=1, relief="solid")
                pca_labels.grid(row=b+1, column=c+2, ipadx=5, ipady=2, sticky=N+S+W+E)

                # Set colour if success variance is higher than a defined threshold
                if pca_components[b,-1] >= 0.1:
                    pca_labels.configure(bg="SpringGreen2")
    mainloop()

def get_cluster_affiliation():
    
    # Call function to provide/get the results from the evaluation file      
    evaluation_val = provide_cluster_affiliation()
    print(evaluation_val)

    ## Parameters Clusters
    # Poly Parameters: Clusters
    poly_c_clusters.configure(text=round(evaluation_val[0]["estimator__C"], 2))
    poly_d_clusters.configure(text=round(evaluation_val[0]["estimator__degree"], 2))
    poly_gamma_clusters.configure(text=round(evaluation_val[0]["estimator__gamma"], 2))
    poly_r_clusters.configure(text=round(evaluation_val[0]["estimator__coef0"], 2))

    # RBF Parameters: Clusters
    rbf_c_clusters.configure(text=round(evaluation_val[2]["estimator__C"], 2))
    rbf_gamma_clusters.configure(text=round(evaluation_val[2]["estimator__gamma"], 2))

    ## Scores Clusters
    poly_cluster.configure(text=round(evaluation_val[1], 2))
    rbf_cluster.configure(text=round(evaluation_val[3], 2))
    


# Draws the backend
if __name__ == "__main__":
       
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("radiance")
    root.title("Administration: Machine Learning Approach")
    root.configure(background="#F6F6F5")

    # Variables for user input
    sensor = IntVar()
    actor_own = DoubleVar()

    # Frames
    mainframe = ttk.Frame(root)
    mainframe.grid(ipadx=45, pady=50)

    ### Prediction Success
    ## Buttons
    delete_db_button = ttk.Button(mainframe, text="Delete Database", command=delete_database)
    delete_db_button.grid(column=0, row=1, padx=30, sticky=N+S+W+E)

    create_db_button = ttk.Button(mainframe, text="Create Database", command=create_database)
    create_db_button.grid(column=0, row=2, padx=30, sticky=N+S+W+E)

    load_button = ttk.Button(mainframe, text="Load Data", command=load_data_into_database)
    load_button.grid(column=0, row=3, padx=30, sticky=N+S+W+E)

    train_button = ttk.Button(mainframe, text="Feature Reduction", command=show_results_feature_reduction)
    train_button.grid(column=0, row=4, rowspan=2, padx=30, sticky=N+S+W+E)

    train_button = ttk.Button(mainframe, text="Train Data", command=get_svm_data)
    train_button.grid(column=0, row=6, rowspan=2, padx=30, sticky=N+S+W+E)

    ## Labels no cluster and cluster
    no_cluster = Label(mainframe, text="Without Cluster", bg="white", font='Helvetica 10 bold', borderwidth=1, relief="solid")
    no_cluster.grid(column=3, columnspan=2, row=0, ipadx=20, ipady=2, sticky=N+S+W+E)

    cluster = Label(mainframe, text="With Cluster", bg="white", font='Helvetica 10 bold', borderwidth=1, relief="solid")
    cluster.grid(column=5, columnspan=2, row=0, ipadx=30, sticky=N+S+W+E)

    ## Labels for describing the evaluation type
    rmse_poly = Label(mainframe, text="RMSE with Train and Test Data (Poly):", font='Helvetica 10 bold', anchor="w", padx=15, bg="white", borderwidth=1, relief="solid")
    rmse_poly.grid(column=1, columnspan=2, row=1, ipady=10, sticky=N+S+W+E)

    rmse_cv_poly = Label(mainframe, text="RMSE with Cross Validation (Poly):", font='Helvetica 10 bold', anchor="w", padx=15, bg="white", borderwidth=1, relief="solid")
    rmse_cv_poly.grid(column=1,columnspan=2, row=2, ipady=10, sticky=N+S+W+E)

    accuracy_poly = Label(mainframe, text="Accuracy with Cross Validation (Poly):", font='Helvetica 10 bold', anchor="w", padx=15, bg="white", borderwidth=1, relief="solid")
    accuracy_poly.grid(column=1, columnspan=2, row=3, ipady=10, sticky=N+S+W+E)

    # Grid Search Polynomial and Parameters
    grid_search_poly = Label(mainframe, text="Grid Search (Poly):", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, width=25, borderwidth=1, relief="solid")
    grid_search_poly.grid(column=1, row=4, rowspan=4, sticky=N+S+W+E)

    grid_search_poly_c = Label(mainframe, text="C", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_c.grid(column=2, row=4, sticky=N+S+W+E)

    grid_search_poly_d = Label(mainframe, text="d", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_d.grid(column=2, row=5, sticky=N+S+W+E)

    grid_search_poly_gamma = Label(mainframe, text=u"\u03B3", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_gamma.grid(column=2, row=6, sticky=N+S+W+E)

    grid_search_poly_r = Label(mainframe, text="r", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_r.grid(column=2, row=7, sticky=N+S+W+E)

    # Grid Search RBF and Parameters
    grid_search_rbf = Label(mainframe, text="Grid Search (RBF):", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_rbf.grid(column=1, row=8, rowspan=2, sticky=N+S+W+E)

    grid_search_rbf_C = Label(mainframe, text="C", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_rbf_C.grid(column=2, row=8, sticky=N+S+W+E)

    grid_search_rbf_gamma = Label(mainframe, text=u"\u03B3", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_rbf_gamma.grid(column=2, row=9, sticky=N+S+W+E)
    
    # Grid Search Poly and Parameters after Feature Reduction
    grid_search_poly_fr = Label(mainframe, text="Grid Search after\nFeature Reduction (Poly):", bg="white", font='Helvetica 10 bold', anchor="w", justify=LEFT, padx=15, borderwidth=1, relief="solid")
    grid_search_poly_fr.grid(column=1, row=10, rowspan=4, sticky=N+S+W+E)

    grid_search_poly_fr_c = Label(mainframe, text="C", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_fr_c.grid(column=2, row=10, sticky=N+S+W+E)

    grid_search_poly_fr_d = Label(mainframe, text="d", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_fr_d.grid(column=2, row=11, sticky=N+S+W+E)

    grid_search_poly_fr_gamma = Label(mainframe, text=u"\u03B3", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_fr_gamma.grid(column=2, row=12, sticky=N+S+W+E)

    grid_search_poly_fr_r = Label(mainframe, text="r", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_poly_fr_r.grid(column=2, row=13, sticky=N+S+W+E)

    # Grid Search RBF and Parameters after Feature Reduction
    grid_search_rbf_fr = Label(mainframe, text="Grid Search after\nFeature Reduction (RBF):", bg="white", font='Helvetica 10 bold', anchor="w", justify=LEFT, padx=15, borderwidth=1, relief="solid")
    grid_search_rbf_fr.grid(column=1, row=14, rowspan=2, sticky=N+S+W+E)

    grid_search_rbf_fr_c = Label(mainframe, text="C", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_rbf_fr_c.grid(column=2, row=14, sticky=N+S+W+E)

    grid_search_rbf_fr_gamma = Label(mainframe, text=u"\u03B3", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_rbf_fr_gamma.grid(column=2, row=15, sticky=N+S+W+E)

    ## Labels for depicting results

    ## Parameters without Clusters
    # Poly Parameters: Without Clusters
    poly_c_without_clusters = Label(mainframe, text="--", bg="white", padx=15, font='Helvetica 10', borderwidth=1, relief="solid")
    poly_c_without_clusters.grid(column=3, row=4, sticky=N+S+W+E)

    poly_d_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_d_without_clusters.grid(column=3, row=5, sticky=N+S+W+E)

    poly_gamma_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_gamma_without_clusters.grid(column=3, row=6,  sticky=N+S+W+E)

    poly_r_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_r_without_clusters.grid(column=3, row=7,  sticky=N+S+W+E)

    # RBF Parameters: Without Clusters
    rbf_c_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_c_without_clusters.grid(column=3, row=8, sticky=N+S+W+E)

    rbf_gamma_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_gamma_without_clusters.grid(column=3, row=9, sticky=N+S+W+E)
    
    # Poly Parameters after Feature Reduction: Without Clusters
    poly_fr_c_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_c_without_clusters.grid(column=3, row=10, sticky=N+S+W+E)

    poly_fr_d_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_d_without_clusters.grid(column=3, row=11, sticky=N+S+W+E)

    poly_fr_gamma_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_gamma_without_clusters.grid(column=3, row=12, sticky=N+S+W+E)

    poly_fr_r_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_r_without_clusters.grid(column=3, row=13, sticky=N+S+W+E)

    # RBF Parameters after Feature Reduction: Without Clusters
    rbf_fr_c_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_fr_c_without_clusters.grid(column=3, row=14, sticky=N+S+W+E)

    rbf_fr_gamma_without_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_fr_gamma_without_clusters.grid(column=3, row=15, sticky=N+S+W+E)

    ## Parameters with Clusters
    # Poly Parameters: With Clusters
    poly_c_with_clusters = Label(mainframe, text="--", bg="white", padx=15,font='Helvetica 10', borderwidth=1, relief="solid")
    poly_c_with_clusters.grid(column=5, row=4, sticky=N+S+W+E)

    poly_d_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_d_with_clusters.grid(column=5, row=5, sticky=N+S+W+E)

    poly_gamma_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_gamma_with_clusters.grid(column=5, row=6,  sticky=N+S+W+E)

    poly_r_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_r_with_clusters.grid(column=5, row=7,  sticky=N+S+W+E)

    # RBF Parameters: With Clusters
    rbf_c_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_c_with_clusters.grid(column=5, row=8, sticky=N+S+W+E)

    rbf_gamma_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_gamma_with_clusters.grid(column=5, row=9, sticky=N+S+W+E)
    
    # Poly Parameters after Feature Reduction: With Clusters
    poly_fr_c_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_c_with_clusters.grid(column=5, row=10, sticky=N+S+W+E)

    poly_fr_d_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_d_with_clusters.grid(column=5, row=11, sticky=N+S+W+E)

    poly_fr_gamma_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_gamma_with_clusters.grid(column=5, row=12, sticky=N+S+W+E)

    poly_fr_r_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_fr_r_with_clusters.grid(column=5, row=13, sticky=N+S+W+E)

    # RBF Parameters after Feature Reduction: With Clusters
    rbf_fr_c_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_fr_c_with_clusters.grid(column=5, row=14, sticky=N+S+W+E)

    rbf_fr_gamma_with_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_fr_gamma_with_clusters.grid(column=5, row=15, sticky=N+S+W+E)

    ## Scores without Clusters
    RMSE_without_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    RMSE_without_cluster.grid(column=3, columnspan=2, row=1, sticky=N+S+W+E)

    Score_RMSE_without_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    Score_RMSE_without_cluster.grid(column=3, columnspan=2, row=2, sticky=N+S+W+E)

    Score_without_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    Score_without_cluster.grid(column=3, columnspan=2, row=3, sticky=N+S+W+E)

    poly_without_cluster = Label(mainframe, text="---", bg="white", width=15, borderwidth=1, relief="solid")
    poly_without_cluster.grid(column=4, row=4, rowspan=4, sticky=N+S+W+E)

    rbf_without_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    rbf_without_cluster.grid(column=4, row=8, rowspan=2, sticky=N+S+W+E)

    poly_fr_without_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    poly_fr_without_cluster.grid(column=4, row=10, rowspan=4, sticky=N+S+W+E)

    rbf_fr_without_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    rbf_fr_without_cluster.grid(column=4, row=14, rowspan=2, sticky=N+S+W+E)

    ## Scores with Clusters
    RMSE_with_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    RMSE_with_cluster.grid(column=5, columnspan=2, row=1, sticky=N+S+W+E)

    Score_RMSE_with_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    Score_RMSE_with_cluster.grid(column=5, columnspan=2, row=2, sticky=N+S+W+E)

    Score_with_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    Score_with_cluster.grid(column=5, columnspan=2, row=3, sticky=N+S+W+E)

    poly_with_cluster = Label(mainframe, text="---", bg="white", width=15, borderwidth=1, relief="solid")
    poly_with_cluster.grid(column=6, row=4, rowspan=4, sticky=N+S+W+E)

    rbf_with_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    rbf_with_cluster.grid(column=6, row=8, rowspan=2, sticky=N+S+W+E)

    poly_fr_with_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    poly_fr_with_cluster.grid(column=6, row=10, rowspan=4, sticky=N+S+W+E)

    rbf_fr_with_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    rbf_fr_with_cluster.grid(column=6, row=14, rowspan=2, sticky=N+S+W+E)

    ## Target Values
    explanation_target_value = Label(mainframe, text="Target Value", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_target_value.grid(column=7, row=0, ipadx=3, sticky=N+S+W+E)

    explanation_rmse = Label(mainframe, text="0", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_rmse.grid(column=7, row=1, sticky=N+S+W+E)

    explanation_rmse_cv = Label(mainframe, text="0", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_rmse_cv.grid(column=7, row=2, sticky=N+S+W+E)

    explanation_score = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_score.grid(column=7, row=3, sticky=N+S+W+E)

    explanation_poly = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_poly.grid(column=7, row=4, rowspan=4, sticky=N+S+W+E)

    explanation_rbf = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_rbf.grid(column=7, row=8, rowspan=2, sticky=N+S+W+E)

    explanation_poly_fr = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_poly_fr.grid(column=7, row=10, rowspan=4, sticky=N+S+W+E)

    explanation_rbf_fr = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_rbf_fr.grid(column=7, row=14, rowspan=2, sticky=N+S+W+E)

    ### Prediction Cluster Affiliation
    # Label Space between tables
    space_tables = Label(mainframe)
    space_tables.grid(column=3, row=17, ipadx=20, ipady=2, sticky=N+S+W+E)

    ## Buttons
    train_button_cluster = ttk.Button(mainframe, text="Train Data", command=get_cluster_affiliation)
    train_button_cluster.grid(column=0, row=19, rowspan=2, padx=30, sticky=N+S+W+E)

    ## Label Cluster Affiliation
    cluster_affiliation = Label(mainframe, text="Cluster Affiliation", bg="white", font='Helvetica 10 bold', borderwidth=1, relief="solid")
    cluster_affiliation.grid(column=3, row=18, columnspan=2, ipadx=20, ipady=2, sticky=N+S+W+E)

    # Grid Search Polynomial and Parameters
    grid_search_cluster_affiliation_poly = Label(mainframe, text="Grid Search (Poly):", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, width=25, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_poly.grid(column=1, row=19, rowspan=4, sticky=N+S+W+E)

    grid_search_cluster_affiliation_poly_c = Label(mainframe, text="C", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_poly_c.grid(column=2, row=19, sticky=N+S+W+E)

    grid_search_cluster_affiliation_poly_d = Label(mainframe, text="d", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_poly_d.grid(column=2, row=20, sticky=N+S+W+E)

    grid_search_cluster_affiliation_poly_gamma = Label(mainframe, text=u"\u03B3", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_poly_gamma.grid(column=2, row=21, sticky=N+S+W+E)

    grid_search_cluster_affiliation_poly_r = Label(mainframe, text="r", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_poly_r.grid(column=2, row=22, sticky=N+S+W+E)

    # Grid Search RBF and Parameters
    grid_search_cluster_affiliation_rbf = Label(mainframe, text="Grid Search (RBF):", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_rbf.grid(column=1, row=23, rowspan=2, sticky=N+S+W+E)

    grid_search_cluster_affiliation_rbf_C = Label(mainframe, text="C", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_rbf_C.grid(column=2, row=23, sticky=N+S+W+E)

    grid_search_cluster_affiliation_rbf_gamma = Label(mainframe, text=u"\u03B3", bg="white", font='Helvetica 10 bold', anchor="w", padx=15, borderwidth=1, relief="solid")
    grid_search_cluster_affiliation_rbf_gamma.grid(column=2, row=24, sticky=N+S+W+E)

    ## Parameters Clusters
    # Poly Parameters
    poly_c_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_c_clusters.grid(column=3, row=19, sticky=N+S+W+E)

    poly_d_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_d_clusters.grid(column=3, row=20, sticky=N+S+W+E)

    poly_gamma_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_gamma_clusters.grid(column=3, row=21, sticky=N+S+W+E)

    poly_r_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    poly_r_clusters.grid(column=3, row=22, sticky=N+S+W+E)

    # RBF Parameters
    rbf_c_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_c_clusters.grid(column=3, row=23, sticky=N+S+W+E)

    rbf_gamma_clusters = Label(mainframe, text="--", bg="white", font='Helvetica 10', borderwidth=1, relief="solid")
    rbf_gamma_clusters.grid(column=3, row=24, sticky=N+S+W+E)

    ## Labels for depicting results
    # Scores Clusters
    poly_cluster = Label(mainframe, text="---", bg="white", width=15, borderwidth=1, relief="solid")
    poly_cluster.grid(column=4, row=19, rowspan=4, sticky=N+S+W+E)

    rbf_cluster = Label(mainframe, text="---", bg="white", borderwidth=1, relief="solid")
    rbf_cluster.grid(column=4, row=23, rowspan=2, sticky=N+S+W+E)

    # Target Values
    explanation_target_value_cluster = Label(mainframe, text="TV", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_target_value_cluster.grid(column=5, row=18, ipadx=3, sticky=N+S+W+E)

    explanation_poly_cluster = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_poly_cluster.grid(column=5, row=19, rowspan=4, sticky=N+S+W+E)

    explanation_rbf_cv_cluster = Label(mainframe, text="1", font='Helvetica 10 bold', bg="white", borderwidth=1, relief="solid")
    explanation_rbf_cv_cluster.grid(column=5, row=23, rowspan=2, sticky=N+S+W+E)


    root.mainloop()

