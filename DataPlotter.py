#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data Plotter for "Legged Robots that Keep on Learning (fine-tuning-locomotion)"

__author__     = "Giorgio Clivio"
__copyright__  = "Clivio Clivio"
__license__    = "Creative Commons CC0 1.0 Universal"
__version__    = "24.02.25"
__maintainer__ = "Giorgio Clivio"
__email__      = "giorgio@clivio.net"
__status__     = "Development"

https://creativecommons.org/publicdomain/zero/1.0/legalcode
https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt

GitHub Repository "fine-tuning-locomotion" can be found here:
https://github.com/lauramsmith/fine-tuning-locomotion
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import re

# Set default file
previously_read_file = 'output_0.txt'

# Function to extract data from the file
def extract_data(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    
    data_blocks = re.findall(r'[-]+\n(.*?)\n[-]+', content, re.DOTALL)
    
    iterations = []
    wall_times = []
    samples = []
    train_returns = []
    train_paths = []
    test_returns = []
    test_paths = []
    final_robot_x = []
    final_robot_y = []
    robot_travel_forward = []
    robot_travel_sideways = []
    robot_travel_yaw_deg = []
    max_torque = []
    critic_loss = []
    critic_steps = []
    critic_time_per_update_list = []  
    actor_loss = []
    actor_entropy = []
    actor_steps = []

    for block in data_blocks:
        iteration = int(re.search(r'Iteration \| *(\d+)', block).group(1))
        wall_time = float(re.search(r'Wall_Time \| *([\d.]+)', block).group(1))
        samples_value = int(re.search(r'Samples \| *(\d+)', block).group(1))
        train_return = float(re.search(r'Train_Return \| *([\d.-]+)', block).group(1))
        train_path = int(re.search(r'Train_Paths \| *(\d+)', block).group(1))
        test_return = float(re.search(r'Test_Return \| *([\d.-]+)', block).group(1))
        test_path = int(re.search(r'Test_Paths \| *(\d+)', block).group(1))
        final_x = float(re.search(r'Final_Robot_X \| *([\d.-]+)', block).group(1))
        final_y = float(re.search(r'Final_Robot_Y \| *([\d.-]+)', block).group(1))
        travel_forward = float(re.search(r'Robot_Travel_Forward \| *([\d.-]+)', block).group(1))
        travel_sideways = float(re.search(r'Robot_Travel_Sideways \| *([\d.-]+)', block).group(1))
        travel_yaw_deg = float(re.search(r'Robot_Travel_Yaw_Deg \| *([\d.-]+)', block).group(1))
        max_torque_value = float(re.search(r'Max_Torque \| *([\d.-]+)', block).group(1))
        critic_loss_value = float(re.search(r'Critic_Loss \| *([\d.-]+)', block).group(1))
        critic_steps_value = int(re.search(r'Critic_Steps \| *(\d+)', block).group(1))
        critic_time_per_update = float(re.search(r'Critic_Time_Per_Update \| *([\d.-]+)', block).group(1))
        actor_loss_value = float(re.search(r'Actor_Loss \| *([\d.-]+)', block).group(1))
        actor_entropy_value = float(re.search(r'Actor_Entropy \| *([\d.-]+)', block).group(1))
        actor_steps_value = int(re.search(r'Actor_Steps \| *(\d+)', block).group(1))

        iterations.append(iteration)
        wall_times.append(wall_time)
        samples.append(samples_value)
        train_returns.append(train_return)
        train_paths.append(train_path)
        test_returns.append(test_return)
        test_paths.append(test_path)
        final_robot_x.append(final_x)
        final_robot_y.append(final_y)
        robot_travel_forward.append(travel_forward)
        robot_travel_sideways.append(travel_sideways)
        robot_travel_yaw_deg.append(travel_yaw_deg)
        max_torque.append(max_torque_value)
        critic_loss.append(critic_loss_value)
        critic_steps.append(critic_steps_value)
        critic_time_per_update_list.append(critic_time_per_update)
        actor_loss.append(actor_loss_value)
        actor_entropy.append(actor_entropy_value)
        actor_steps.append(actor_steps_value)

    return {
        'iterations': iterations,
        'wall_times': wall_times,
        'samples': samples,
        'train_returns': train_returns,
        'train_paths': train_paths,
        'test_returns': test_returns,
        'test_paths': test_paths,
        'final_robot_x': final_robot_x,
        'final_robot_y': final_robot_y,
        'robot_travel_forward': robot_travel_forward,
        'robot_travel_sideways': robot_travel_sideways,
        'robot_travel_yaw_deg': robot_travel_yaw_deg,
        'max_torque': max_torque,
        'critic_loss': critic_loss,
        'critic_steps': critic_steps,
        'critic_time_per_update_list': critic_time_per_update_list,
        'actor_loss': actor_loss,
        'actor_entropy': actor_entropy,
        'actor_steps': actor_steps,
    }

import matplotlib.pyplot as plt
        
import matplotlib.pyplot as plt

# Function to plot the selected data
def plot_selected_data(selected_params, num_points, file_name):
    data = extract_data(file_name)
    num_plots = len(selected_params)

    if num_plots > 0:
        # Determine number of columns and rows based on the number of plots
        cols = min(3, num_plots)  # Set a maximum of 3 columns for better visibility
        rows = (num_plots + cols - 1) // cols  # Calculate number of rows needed

        # Adjust the figure size based on the number of rows and columns
        fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 3 * rows))  # Adjusting size for better visibility
        axes = axes.flatten() if num_plots > 1 else [axes]

        for i, param in enumerate(selected_params):
            axes[i].plot(data['iterations'][:num_points], data[param][:num_points], label=param)
            axes[i].set_xlabel('Iteration')
            axes[i].set_ylabel(param)
            axes[i].grid()

        # Automatically adjust the layout
        plt.tight_layout()

        # Add additional space between subplots and the figure edges to ensure labels are fully visible
        fig.subplots_adjust(hspace=0.5, wspace=0.3)

        # Hide any unused subplots
        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.show()

        
# Main Tkinter window
def main_window():
    global previously_read_file, root
    root = tk.Tk()
    root.title("Graph Selector")
    root.geometry("600x700")

    # Frame for file input
    file_frame = tk.Frame(root)
    file_frame.pack(pady=10)
    tk.Label(file_frame, text=f"Collecting data from {previously_read_file}. Use another file?").pack(side="left")
    file_entry = tk.Entry(file_frame)
    file_entry.pack(side="left")

    # Frame for parameters checkboxes
    params_frame = tk.Frame(root)
    params_frame.pack(pady=20)
    tk.Label(params_frame, text="Select parameters to plot:", font=("Arial", 12)).pack()

    # List of possible parameters
    param_options = ['wall_times', 'samples', 'train_returns', 'train_paths', 'test_returns', 'test_paths',
                     'final_robot_x', 'final_robot_y', 'robot_travel_forward', 'robot_travel_sideways',
                     'robot_travel_yaw_deg', 'max_torque', 'critic_loss', 'critic_steps',
                     'critic_time_per_update_list', 'actor_loss', 'actor_entropy', 'actor_steps']

    param_vars = {param: tk.BooleanVar() for param in param_options}
    for param in param_options:
        tk.Checkbutton(params_frame, text=param, variable=param_vars[param]).pack(anchor='w')

    # Frame for Select All and Deselect All buttons
    select_frame = tk.Frame(root)
    select_frame.pack(pady=10)
    
    # Select All and Deselect All Buttons
    def select_all():
        for var in param_vars.values():
            var.set(True)

    def deselect_all():
        for var in param_vars.values():
            var.set(False)

    tk.Button(select_frame, text="Select All", command=select_all).pack(side="left", padx=5)
    tk.Button(select_frame, text="Deselect All", command=deselect_all).pack(side="left", padx=5)

    # Frame for number of data points
    points_frame = tk.Frame(root)
    points_frame.pack(pady=10)
    tk.Label(points_frame, text="Select number of data points:", font=("Arial", 12)).pack()
    points_var = tk.IntVar(value=10)
    points_menu = ttk.Combobox(points_frame, textvariable=points_var, values=list(range(1, 101)), state='readonly')
    points_menu.pack()

    # Submit button
    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), width=15, height=2, 
                              command=lambda: submit(file_entry.get(), param_vars, points_var.get()))
    submit_button.pack(pady=10)

    root.mainloop()

# Submit function to get selected parameters and file name
def submit(file_name, param_vars, num_points):
    global previously_read_file

    selected_params = [param for param, var in param_vars.items() if var.get()]

    # If no new file is entered, use the previously read file
    if file_name:
        previously_read_file = file_name
    else:
        file_name = previously_read_file

    # Plot the selected data
    plot_selected_data(selected_params, num_points, file_name)

    root.destroy()

# Run the Tkinter window
main_window()
