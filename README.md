# Data Plotter for "Legged Robots that Keep on Learning (fine-tuning-locomotion)"

This Python program allows you to visualize data related to the project "Legged Robots that Keep on Learning". It extracts relevant information from text files containing training data of legged robots and presents it through a user-friendly graphical interface using Tkinter and Matplotlib.

![Project Image](https://github.com/GiorgioClivio/DataPlotter_fine-tuning-locomotion/blob/main/DataPlotter.png?raw=true)

## Author

- **Name**: Giorgio Clivio
- **Email**: [giorgio@clivio.net](mailto:giorgio@clivio.net)
- **License**: [Creative Commons CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/legalcode)

## Version

- **Version**: 06.10.24
- **Status**: Development

## Installation

To run this program, ensure you have Python 3 installed on your system. You will also need the following libraries:

- Tkinter (usually included with Python)
- Matplotlib
- re (part of Python standard library)

You can install Matplotlib using pip:

```bash
pip install matplotlib
```

## How to use

When starting a training of the algorithm presented in [fine-tuning-locomotion](https://github.com/lauramsmith/fine-tuning-locomotion),
add " | tee filename.txt" at the end of the command, as in the example below:

```bash
python3 motion_imitation/run_sac.py --mode train --motion_file /home/giorgio/fine-tuning-locomotion/motion_imitation/data/motions/pace.txt --int_save_freq 1000 --visualize | tee output_0.txt
```

This will create an output_0.txt file in the fine-tuning-locomotion main folder. Make sure to place the DataPlotter.py file in the fine-tuning-locomotion main folder as well.
When the training is finished, run the DataPlotter.py file: a Tkinter window will allow you to input a file name (in this case, output_0.txt, select which parameter to visualize via checkboxes, and specify the number of data points to plot. This approach is simple and user-friendly and facilitates easy selection of data parameters.
The “extract_data” function in DataPlotter.py reads the chosen text file containing the training data and uses regular expressions to extract specific metrics related to the robot's training process. 
These metrics include iterations, wall time, samples, training returns, test returns, travel metrics, and various losses associated with the actor and critic agents.

Once the Matplotlib window appears, you can easily download an image of the plotted data.

I included in this Repository 4 examples of output.txt files, so you can try to run the DataPlotter.py program.







