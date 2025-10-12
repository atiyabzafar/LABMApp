# GUI Application for Brazilian-Portuguese Migration ABM

## Overview

This interactive GUI application allows you to run the agent-based simulation with custom parameters and view results in real-time. No coding required!

## Features

### 🎛️ **Interactive Parameter Control**
- Adjust all simulation parameters through an intuitive interface
- Organized parameter groups (Population, Demographics, Interactions, etc.)
- Tooltips explaining each parameter
- Reset to default values with one click

### 📊 **Real-Time Visualization**
- **Demographics Tab**: Population dynamics and migrant proportion
- **Linguistic Features Tab**: Evolution of all 4 linguistic features
- **Summary Statistics Tab**: Detailed numerical results

### 🚀 **Easy Operation**
- Run simulations with custom parameters
- Progress bar showing simulation status
- Stop simulation at any time
- Export results to CSV

## Quick Start

### 1. Launch the GUI

```bash
cd "/Users/pancho/Library/CloudStorage/Dropbox/25 - CSG/02 - Languaje and migration"
python3 gui_app.py
```

### 2. Adjust Parameters (Optional)

The left panel contains all simulation parameters organized into groups:

**Population:**
- Initial Locals (default: 1000)
- Initial Migrants (default: 100)
- Annual Immigration (default: 120)

**Demographic Rates:**
- Local Birth Rate (default: 0.04)
- Migrant Birth Rate (default: 0.06)

**Social Interactions:**
- School Interactions (default: 5)
- Workplace Interactions (default: 3)
- Public Interaction Probability (default: 0.3)

**Media & Identity:**
- Media Influence (default: 0.5)
- Locals Reveal % (default: 0.3)
- Migrants Reveal % (default: 0.7)

**Linguistic Influence Rates:**
- Vocabulary Rate (default: 0.5)
- Grammar Rate (default: 0.3)
- Pronoun Rate (default: 0.25)
- Phonetic Rate (default: 0.15)

**Simulation:**
- Simulation Years (default: 20)

### 3. Run Simulation

Click the **"Run Simulation"** button. The simulation will:
- Initialize the model
- Run for the specified number of years
- Update progress bar in real-time
- Display results automatically when complete

### 4. View Results

Switch between tabs to view different aspects:

**Demographics Tab:**
- Left plot: Population sizes over time (Locals vs Migrants)
- Right plot: Migrant proportion percentage

**Linguistic Features Tab:**
- Four subplots showing evolution of each feature
- Blue lines: Locals adopting Brazilian features
- Red lines: Migrants retaining Brazilian features

**Summary Statistics Tab:**
- Demographic outcomes (population changes)
- Linguistic integration (feature adoption by locals)
- Migrant heritage retention
- All simulation parameters used

### 5. Export Data

Click **"Export Data"** to save results to CSV format for further analysis.

## GUI Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Brazilian-Portuguese Migration ABM                             │
├──────────────────────┬──────────────────────────────────────────┤
│  Parameters          │  Results                                 │
│  ┌────────────────┐  │  ┌────────────────────────────────────┐ │
│  │ Population     │  │  │ [Demographics] [Features] [Stats]  │ │
│  │  - Locals      │  │  │                                    │ │
│  │  - Migrants    │  │  │                                    │ │
│  │  - Immigration │  │  │                                    │ │
│  │                │  │  │        [Plots/Statistics]          │ │
│  │ Demographics   │  │  │                                    │ │
│  │  - Birth rates │  │  │                                    │ │
│  │                │  │  │                                    │ │
│  │ Interactions   │  │  │                                    │ │
│  │  - School      │  │  │                                    │ │
│  │  - Workplace   │  │  └────────────────────────────────────┘ │
│  │  - Public      │  │                                          │
│  │                │  │                                          │
│  │ Media          │  │                                          │
│  │                │  │                                          │
│  │ Influence      │  │                                          │
│  │  - Vocabulary  │  │                                          │
│  │  - Grammar     │  │                                          │
│  │  - Phonetics   │  │                                          │
│  │  - Pronouns    │  │                                          │
│  │                │  │                                          │
│  │ Simulation     │  │                                          │
│  │  - Years       │  │                                          │
│  └────────────────┘  │                                          │
│  [Run] [Stop]        │                                          │
│  [Reset] [Export]    │                                          │
│  [Progress Bar]      │                                          │
│  Status: Ready       │                                          │
└──────────────────────┴──────────────────────────────────────────┘
```

## Example Use Cases

### 1. Baseline Scenario
Use default parameters to replicate the results from the paper.

### 2. High Immigration Scenario
- Increase "Annual Immigration" to 300
- Observe faster demographic shift and linguistic change

### 3. Low Media Influence
- Decrease "Media Influence" to 0.1
- See how linguistic change depends more on interpersonal interaction

### 4. High Social Interaction
- Increase "School Interactions" to 10
- Increase "Workplace Interactions" to 6
- Observe accelerated linguistic diffusion

### 5. Short-Term Dynamics
- Set "Simulation Years" to 5
- Examine early-stage integration patterns

## Tips

### Performance
- Simulations with default parameters take ~10 seconds
- Larger populations or longer durations take proportionally longer
- Progress bar shows real-time status

### Parameter Exploration
- Use "Reset to Defaults" to restore baseline parameters
- Change one parameter at a time to understand its effect
- Run multiple scenarios and compare results

### Data Export
- Export data after each run to preserve results
- Use different filenames for different scenarios
- Analyze exported CSV files in Excel, R, or Python

### Stopping Simulations
- Click "Stop" to halt a running simulation
- Useful for very long simulations or if you want to change parameters

## Troubleshooting

### GUI doesn't launch
```bash
# Make sure you have tkinter installed
python3 -m tkinter
# Should open a small test window
```

### "Invalid Input" error
- Check that all parameter values are numbers
- Population parameters must be integers (no decimals)
- Rates and probabilities must be between 0 and 1

### Plots not showing
- Make sure matplotlib is installed: `pip install matplotlib`
- Try running the simulation again

### Slow performance
- Reduce population sizes (e.g., 500 locals, 50 migrants)
- Reduce simulation years (e.g., 10 years)
- Close other applications to free up memory

## Keyboard Shortcuts

- **Enter** in any parameter field: Start simulation
- **Escape**: Stop simulation (if running)

## Advanced Features

### Hover Tooltips
Hover over parameter labels to see descriptions in the status bar at the bottom.

### Multi-Tab Results
Switch between tabs while simulation is running to prepare for viewing different aspects.

### Threaded Execution
Simulations run in background threads, so the GUI remains responsive.

## Technical Details

### Dependencies
- Python 3.8+
- tkinter (usually included with Python)
- matplotlib
- numpy
- All simulation modules (agents.py, model.py, etc.)

### Architecture
- **GUI Layer**: Tkinter interface
- **Simulation Layer**: MigrationModel class
- **Visualization Layer**: Matplotlib embedded in tkinter
- **Threading**: Background execution for responsiveness

### File Output
Exported CSV files contain:
- Time step (months)
- Population sizes
- Mean linguistic features for both populations
- All data points from the simulation

## Comparison with Command-Line

| Feature | GUI | Command-Line |
|---------|-----|--------------|
| Ease of use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Parameter adjustment | Interactive | Edit code |
| Real-time progress | Yes | No |
| Visualization | Embedded | Separate windows |
| Data export | Built-in | Manual |
| Batch runs | Manual | Easy (scripting) |
| Customization | Limited | Full |

**Use GUI for:** Interactive exploration, teaching, presentations  
**Use command-line for:** Batch processing, automation, custom analysis

## Future Enhancements

Possible additions (not yet implemented):
- Save/load parameter presets
- Compare multiple scenarios side-by-side
- Animation of simulation progress
- Spatial visualization (district-level maps)
- Sensitivity analysis tools
- Parameter optimization

## Screenshots

### Main Window
The main window shows parameters on the left and results on the right.

### Demographics Tab
Population dynamics with two plots showing absolute numbers and proportions.

### Linguistic Features Tab
Four subplots showing the evolution of vocabulary, grammar, phonetics, and pronouns.

### Summary Statistics Tab
Detailed numerical results in an easy-to-read format.

## Support

For issues or questions:
1. Check this README
2. Review the main project README.md
3. Examine the code comments in gui_app.py

## Credits

GUI developed for the Brazilian-Portuguese Migration ABM project.

---

**Enjoy exploring cultural evolution through immigration with the interactive GUI!** 🎉
