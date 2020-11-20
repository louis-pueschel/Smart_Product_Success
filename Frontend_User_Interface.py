from tkinter import * # Tkinter for drawining interfaces
from tkinter import ttk
from ttkthemes import themed_tk as tk # Special theme for buttons. Theme must be downloaded under https://ttkthemes.readthedocs.io/en/latest/themes.html. Further explanations https://docs.python.org/3/library/tkinter.ttk.html
from tkinter import messagebox # To display the predicting result
import numpy as np # Vectors and matrices
from Frontend_Smart_Product_Class import smart_object # Import smart object class to save the values of a new smart product
from Frontend_Database_Write import write_to_database # Import function to write the user's smart product data into the related table
from Backend_Support_Vector_Machine_Evaluation_User_Input import evaluate_user_input # Import function to predict the success of the user's smart product/input

# Read values (i.e. characteristics) from the user input (i.e. buttons) and set them to a new object/instance (i.e. distinct smart object) of the class smart_object
# Important: Nested structure. Value from get-method is directly transferred to the class smart object 
def user_input_processing():
    # Thing layer
    smart_object_instance.set_smart_object_characteristic(sensor.get())
    smart_object_instance.set_smart_object_characteristic(actor_own.get())
    smart_object_instance.set_smart_object_characteristic(actor_intermediary.get())
    smart_object_instance.set_smart_object_characteristic(autonomy.get())
    # Interaction layer
    smart_object_instance.set_smart_object_characteristic(interaction_direction.get())
    smart_object_instance.set_smart_object_characteristic(interaction_multiplicity.get())
    smart_object_instance.set_smart_object_characteristic(interaction_partner_user.get())
    smart_object_instance.set_smart_object_characteristic(interaction_partner_business.get())
    smart_object_instance.set_smart_object_characteristic(interaction_partner_thing.get())
    # Data layer
    smart_object_instance.set_smart_object_characteristic(data_source_state.get())
    smart_object_instance.set_smart_object_characteristic(data_source_context.get())
    smart_object_instance.set_smart_object_characteristic(data_source_usage.get())
    smart_object_instance.set_smart_object_characteristic(data_source_cloud.get())
    smart_object_instance.set_smart_object_characteristic(data_usage.get())
    # Service layer
    smart_object_instance.set_smart_object_characteristic(offline.get())
    smart_object_instance.set_smart_object_characteristic(value_proposition.get())
    smart_object_instance.set_smart_object_characteristic(ecosystem.get())

    # Write the smart object values to database
    write_to_database(smart_object_instance.get_smart_object_characteristic())

    # Evaluate user input with SVM
    user_input = smart_object_instance.get_smart_object_characteristic()
    user_input_reshaped = np.reshape(user_input, (1, -1))
    user_input_evaluation_results = evaluate_user_input(user_input_reshaped)
    success_without_clusters = user_input_evaluation_results[0]
    cluster_affiliation = user_input_evaluation_results[1]

    cluster_description = ["Standalone Thing-Centric Executant","Connected Thing-Centric Performer","Standalone Service-Centric Monitor","Connected Service-Centric Partner","Self-Learning Service-Centric All-rounder"]

    # Presentation of evaluation's result
    if success_without_clusters[0] == 4 or success_without_clusters[0] == 5:
        a = "\nCongratulations. \n\nYour Smart Product has achieved \n"
        b = str(int(success_without_clusters[0]))
        c = " out of 5 \npossible points! \nIt will be a true champion at the market!\n"
        d = "Smart Product Type: \nYour Smart Product is a " + "'" + str(cluster_description[int(cluster_affiliation)]) + "'!\n"
        z = d + a + b + c
        messagebox.showinfo(title="Your Result", message = z)
    
    if success_without_clusters[0] == 1 or success_without_clusters[0] == 2 or success_without_clusters[0] == 3:
        a = "\nOh. \n\nYour Smart Product has achieved \n"
        b = str(int(success_without_clusters[0]))
        c = " out of 5 \npossible points! \nMaybe, a bit improvement is necessary! You can do this!\n"
        d = "Smart Product Type: \nYour Smart Product is a " + "'" + str(cluster_description[int(cluster_affiliation)]) + "' !\n"
        z = d + a + b + c
        messagebox.showinfo(title="Your Result", message = z)
    
  

# Draws frontend
if __name__ == "__main__":
       
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("radiance")
    root.title("Smart Product Evaluation")
    root.configure(background="#F6F6F5")

    # Instance of a smart object
    smart_object_instance = smart_object()

    # Variables for user input
    sensor = IntVar()
    actor_own = DoubleVar()
    actor_intermediary = DoubleVar()
    autonomy = DoubleVar()
    interaction_direction = IntVar()
    interaction_multiplicity = IntVar()
    interaction_partner_user = DoubleVar()
    interaction_partner_business = DoubleVar()
    interaction_partner_thing = DoubleVar()
    data_source_state = DoubleVar()
    data_source_context = DoubleVar()
    data_source_usage = DoubleVar()
    data_source_cloud = DoubleVar()
    data_usage = DoubleVar()
    offline = IntVar()
    value_proposition = IntVar()
    ecosystem = DoubleVar()

    # Frames
    mainframe = ttk.Frame(root)
    mainframe.grid(padx=45, pady=50, sticky=N+S+W+E)
    

    # Submit-Button
    submit_button = ttk.Button(mainframe, text="Submit", command=user_input_processing)
    submit_button.grid(column=14, row=11, pady=20, sticky=N+S+W+E)

    # Layer
    layer_service = Label(mainframe, text="Service", bg="white", borderwidth=1, relief="solid")
    layer_service.grid(column=0, row=0, rowspan=3, sticky=N+S+W+E)
    layer_data = Label(mainframe, text="Data", bg="white", borderwidth=1, relief="solid")
    layer_data.grid(column=0, row=3, rowspan=2, sticky=N+S+W+E)
    layer_interaction = Label(mainframe, text="Interaction", bg="white", padx=5, borderwidth=1, relief="solid")
    layer_interaction.grid(column=0, row=5, rowspan=3, sticky=N+S+W+E)    
    layer_thing = Label(mainframe, text="Thing", bg="white", borderwidth=1, relief="solid")
    layer_thing.grid(column=0, row=8, rowspan=3, sticky=N+S+W+E)

    # Dimensions
    dimension_ecosystem_integration = Label(mainframe, text="Ecosystem Integration", bg="white", borderwidth=1, relief="solid")
    dimension_ecosystem_integration.grid(column=1, row=0, sticky=N+S+W+E)
    dimension_value_proposition = Label(mainframe, text="Value Proposition", bg="white", borderwidth=1, relief="solid")
    dimension_value_proposition.grid(column=1, row=1, sticky=N+S+W+E)
    dimension_offline_functionality = Label(mainframe, text="Offline Functionality", bg="white", borderwidth=1, relief="solid")
    dimension_offline_functionality.grid(column=1, row=2, sticky=N+S+W+E)

    dimension_data_usage = Label(mainframe, text="Data Usage", bg="white", borderwidth=1, relief="solid")
    dimension_data_usage.grid(column=1, row=3, sticky=N+S+W+E)
    dimension_data_source = Label(mainframe, text="Data Source", bg="white", borderwidth=1, relief="solid")
    dimension_data_source.grid(column=1, row=4, sticky=N+S+W+E)

    dimension_interaction_partner = Label(mainframe, text="Interaction Partner", bg="white",borderwidth=1, relief="solid")
    dimension_interaction_partner.grid(column=1, row=5, sticky=N+S+W+E)
    dimension_interaction_multiplicty = Label(mainframe, text="Interaction Multiplicty", bg="white",padx=5, borderwidth=1, relief="solid")
    dimension_interaction_multiplicty.grid(column=1, row=6, sticky=N+S+W+E)
    dimension_interaction_direction = Label(mainframe, text="Interaction Direction", bg="white",borderwidth=1, relief="solid")
    dimension_interaction_direction.grid(column=1, row=7, sticky=N+S+W+E)

    dimension_autonomy = Label(mainframe, text="Autonomy", bg="white", borderwidth=1, relief="solid")
    dimension_autonomy.grid(column=1, row=8, sticky=N+S+W+E)
    dimension_actor = Label(mainframe, text="Acting Capabilities", bg="white", borderwidth=1, relief="solid")
    dimension_actor.grid(column=1, row=9, sticky=N+S+W+E)
    dimension_sensor = Label(mainframe, text="Sensing Capabilities", bg="white", borderwidth=1, relief="solid")
    dimension_sensor.grid(column=1, row=10, sticky=N+S+W+E)

    ### Characteristics
    # Service layer
    button_ecosystem = Radiobutton(mainframe, text="None", variable=ecosystem, value=0.0, indicatoron=0)
    button_ecosystem.grid(column=2, row=0, columnspan=4, sticky=N+S+W+E)
    button_ecosystem.deselect()
    button_ecosystem = Radiobutton(mainframe, text="Proprietary", variable=ecosystem, value=0.5, indicatoron=0)
    button_ecosystem.grid(column=6, row=0, columnspan=4, sticky=N+S+W+E)
    button_ecosystem.deselect()
    button_ecosystem = Radiobutton(mainframe, text="Open", variable=ecosystem, value=1.0, indicatoron=0)
    button_ecosystem.grid(column=10, row=0, columnspan=4, sticky=N+S+W+E)
    button_ecosystem.deselect()
    
    button_value_proposition = Radiobutton(mainframe, text="Thing-Centric", variable=value_proposition, value=0, indicatoron=0)
    button_value_proposition.grid(column=2, row=1, columnspan=6, sticky=N+S+W+E)
    button_value_proposition.deselect()
    button_value_proposition = Radiobutton(mainframe, text="Service-Centric", variable=value_proposition, value=1, indicatoron=0)
    button_value_proposition.grid(column=8, row=1, columnspan=6, sticky=N+S+W+E)
    button_value_proposition.deselect()

    button_offline = Radiobutton(mainframe, text="None", variable=offline, value=0, indicatoron=0)
    button_offline.grid(column=2, row=2, columnspan=6, sticky=N+S+W+E)
    button_offline.deselect()
    button_offline = Radiobutton(mainframe, text="Limited", variable=offline, value=1, indicatoron=0)
    button_offline.grid(column=8, row=2, columnspan=6, sticky=N+S+W+E)
    button_offline.deselect()

    # Data layer
    button_data_usage = Radiobutton(mainframe, text="Transactional", variable=data_usage, value=0.0, indicatoron=0)
    button_data_usage.grid(column=2, row=3, columnspan=4, sticky=N+S+W+E)
    button_data_usage.deselect()
    button_data_usage = Radiobutton(mainframe, text="Analytical (basic)", variable=data_usage, value=0.5, indicatoron=0)
    button_data_usage.grid(column=6, row=3, columnspan=4, sticky=N+S+W+E)
    button_data_usage.deselect()
    button_data_usage = Radiobutton(mainframe, text="Analytical (extended)", variable=data_usage, value=1.0, indicatoron=0)
    button_data_usage.grid(column=10, row=3, columnspan=4, sticky=N+S+W+E)    
    button_data_usage.deselect()

    button_data_source = Checkbutton(mainframe, text="Thing State", variable=data_source_state, onvalue=0.25, offvalue=0.00, indicatoron=0)
    button_data_source.grid(column=2, row=4, columnspan=3, sticky=N+S+W+E)
    button_data_source = Checkbutton(mainframe, text="Thing Context", variable=data_source_context, onvalue=0.25, offvalue=0.00, indicatoron=0)
    button_data_source.grid(column=5, row=4, columnspan=3, sticky=N+S+W+E)
    button_data_source = Checkbutton(mainframe, text="Thing Usage", variable=data_source_usage, onvalue=0.25, offvalue=0.00, indicatoron=0)
    button_data_source.grid(column=8, row=4, columnspan=3, sticky=N+S+W+E)
    button_data_source = Checkbutton(mainframe, text="Cloud", variable=data_source_cloud, onvalue=0.25, offvalue=0.00, indicatoron=0)
    button_data_source.grid(column=11, row=4, columnspan=3, sticky=N+S+W+E)

    # Interaction layer
    button_interaction_partner = Checkbutton(mainframe, text="User", variable=interaction_partner_user, onvalue=0.33, offvalue=0.00, indicatoron=0)
    button_interaction_partner.grid(column=2, row=5, columnspan=4, sticky=N+S+W+E)
    button_interaction_partner = Checkbutton(mainframe, text="Business", variable=interaction_partner_business, onvalue=0.33, offvalue=0.00, indicatoron=0)
    button_interaction_partner.grid(column=6, row=5, columnspan=4, sticky=N+S+W+E)
    button_interaction_partner = Checkbutton(mainframe, text="Thing", variable=interaction_partner_thing, onvalue=0.33, offvalue=0.00, indicatoron=0)
    button_interaction_partner.grid(column=10, row=5, columnspan=4, sticky=N+S+W+E)

    button_interaction_multiplicity = Radiobutton(mainframe, text="One-To-One", variable=interaction_multiplicity, value=0, indicatoron=0)
    button_interaction_multiplicity.grid(column=2, row=6, columnspan=6, sticky=N+S+W+E)
    button_interaction_multiplicity.deselect()
    button_interaction_multiplicity = Radiobutton(mainframe, text="One-To-Many", variable=interaction_multiplicity, value=1, indicatoron=0)
    button_interaction_multiplicity.grid(column=8, row=6, columnspan=6, sticky=N+S+W+E)
    button_interaction_multiplicity.deselect()

    button_interaction_direction = Radiobutton(mainframe, text="Uni-Directional", variable=interaction_direction, value=0, indicatoron=0)
    button_interaction_direction.grid(column=2, row=7, columnspan=6, sticky=N+S+W+E)
    button_interaction_direction.deselect()
    button_interaction_direction = Radiobutton(mainframe, text="Bi-Directional", variable=interaction_direction, value=1, indicatoron=0)
    button_interaction_direction.grid(column=8, row=7, columnspan=6, sticky=N+S+W+E)
    button_interaction_direction.deselect()

    # Thing layer
    button_autonomy = Radiobutton(mainframe, text="None", variable=autonomy, value=0.0, indicatoron=0)
    button_autonomy.grid(column=2, row=8, columnspan=4, sticky=N+S+W+E)
    button_autonomy.deselect()
    button_autonomy = Radiobutton(mainframe, text="Self-Controlled", variable=autonomy, value=0.5, indicatoron=0)
    button_autonomy.grid(column=6, row=8, columnspan=4, sticky=N+S+W+E)
    button_autonomy.deselect()
    button_autonomy = Radiobutton(mainframe, text="Self-Learning", variable=autonomy, value=1.0, indicatoron=0)
    button_autonomy.grid(column=10, row=8, columnspan=4, sticky=N+S+W+E)
    button_autonomy.deselect()
    
    button_actor = Checkbutton(mainframe, text="Own", variable=actor_own, onvalue=0.5, offvalue=0.0, indicatoron=0)
    button_actor.grid(column=2, row=9, columnspan=6,sticky=N+S+W+E)   
    button_actor = Checkbutton(mainframe, text="Intermediary", variable=actor_intermediary, onvalue=0.5, offvalue=0.0, indicatoron=0)
    button_actor.grid(column=8, row=9, columnspan=6, sticky=N+S+W+E)
    
    button_sensor = Radiobutton(mainframe, text="Lean", variable=sensor, value=0, indicatoron=0, width=30)
    button_sensor.grid(column=2, row=10, columnspan=6, sticky=N+S+W+E)
    button_sensor.deselect()
    button_sensor = Radiobutton(mainframe, text="Rich", variable=sensor, value=1, indicatoron=0, width=30)
    button_sensor.grid(column=8, row=10, columnspan=6, sticky=N+S+W+E)
    button_sensor.deselect()
    
    # Exclusivity
    exclusivity_ecosystem_integration = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_ecosystem_integration.grid(column=14, row=0, sticky=N+S+W+E)
    exclusivity_value_proposition = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_value_proposition.grid(column=14, row=1, sticky=N+S+W+E)
    exclusivity_offline_functionality = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_offline_functionality.grid(column=14, row=2, sticky=N+S+W+E)
    exclusivity_data_usage = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_data_usage.grid(column=14, row=3, sticky=N+S+W+E)

    exclusivity_data_source = Label(mainframe, text="Non E", bg="white", borderwidth=1, relief="solid")
    exclusivity_data_source.grid(column=14, row=4, sticky=N+S+W+E)

    exclusivity_interaction_partner = Label(mainframe, text="Non E", bg="white", borderwidth=1, relief="solid")
    exclusivity_interaction_partner.grid(column=14, row=5, sticky=N+S+W+E)
    exclusivity_interaction_multiplicty = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_interaction_multiplicty.grid(column=14, row=6, sticky=N+S+W+E)
    exclusivity_offline_direction = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_offline_direction.grid(column=14, row=7, sticky=N+S+W+E)

    exclusivity_autonomy = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_autonomy.grid(column=14, row=8, sticky=N+S+W+E)
    exclusivity_actor = Label(mainframe, text="Non E", bg="white", padx=10, borderwidth=1, relief="solid")
    exclusivity_actor.grid(column=14, row=9, sticky=N+S+W+E)
    exclusivity_sensor = Label(mainframe, text="ME", bg="white", borderwidth=1, relief="solid")
    exclusivity_sensor.grid(column=14, row=10, sticky=N+S+W+E)

    root.mainloop()