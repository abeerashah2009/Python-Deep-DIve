# Lab 35: Quick Data Visualization with Matplotlib

## Objective

Learn how to install Matplotlib, create simple plots, customize graphs, and save visualizations as image files.

## Tools Used

- Python 3.12.3
- Ubuntu 24.04.5 LTS
- Matplotlib 3.9.2
- NumPy 2.5.5
- Virtual Environment (venv)

## Concepts Learned

### 1. Install Matplotlib

Matplotlib is a Python library used to create graphs and visualizations.

```bash
python3 -m venv venv
source venv/bin/activate
pip install matplotlib==3.9.2
```

### 2. Import Required Modules

- `matplotlib`: Main visualization library.
- `matplotlib.pyplot`: Provides functions for creating plots.
- `Agg`: Non-interactive backend for saving plots without a desktop.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

### 3. Define Sample Data

Two lists represent the X and Y coordinates.

```python
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
```

### 4. Create a Line Plot

`plt.plot()` creates a line graph using the supplied data.

```python
plt.plot(x, y)
```

### 5. Customize the Plot

- `plt.title()` adds a graph title.
- `plt.xlabel()` adds the X-axis label.
- `plt.ylabel()` adds the Y-axis label.

```python
plt.title('Simple Line Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
```

### 6. Save the Plot

`plt.savefig()` saves the graph as an image file.

```python
plt.savefig('plot.png')
print('Saved plot.png')
```

## Practical Tasks Completed

1. Installed Matplotlib version 3.9.2.
2. Created and activated a Python virtual environment.
3. Imported Matplotlib and pyplot.
4. Selected the Agg backend.
5. Defined sample X and Y data.
6. Created a simple line plot.
7. Added a title and axis labels.
8. Saved the graph as `plot.png`.
9. Verified the generated PNG image.

## Execution

Run the script:

```bash
python3 quick_plot.py
```

Expected output:

```text
Saved plot.png
```

## Verification Results

- Python version: 3.12.3
- Matplotlib version: 3.9.2
- Backend: Agg
- Python syntax check: PASSED
- Data points: 6 X values and 6 Y values
- PNG image: Generated successfully
- Image dimensions: 640 × 480
- PNG file integrity: Verified

See `evidence/verification.txt` for verification details.

## Importance of Quick Data Visualization

- **Visualizing Trends:** Helps understand changes in data.
- **Identifying Patterns:** Makes relationships and patterns easier to recognize.
- **Comparing Datasets:** Helps compare different sets of information.
- **Decision-Making:** Communicates useful insights quickly.

## Conclusion

Successfully completed a Python data visualization lab using Matplotlib. Learned to install the library, prepare data, create and customize a line graph, and save the result as a PNG image.

**LMS Result: 100 / 100 — Passed**
