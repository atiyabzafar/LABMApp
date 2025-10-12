# Quick Start: GUI Application

## 🚀 Launch the GUI

```bash
cd "/Users/pancho/Library/CloudStorage/Dropbox/25 - CSG/02 - Languaje and migration"
python3 gui_app.py
```

A window will open with the interactive interface!

## 📋 Using the GUI

### Step 1: Review Parameters (Left Panel)
The left side shows all simulation parameters organized in groups:
- **Population**: Initial populations and immigration rate
- **Demographic Rates**: Birth rates for locals and migrants
- **Social Interactions**: How often agents interact
- **Media & Identity**: Media influence and reveal behavior
- **Linguistic Influence Rates**: How fast each feature spreads
- **Simulation**: How many years to simulate

### Step 2: Adjust Parameters (Optional)
- Click in any field to change values
- Hover over labels to see descriptions in the status bar
- Click "Reset to Defaults" to restore original values

### Step 3: Run Simulation
1. Click **"Run Simulation"** button
2. Watch the progress bar
3. Wait for completion (default: ~10 seconds)

### Step 4: View Results (Right Panel)
Switch between three tabs:

**📊 Demographics Tab**
- Population growth over time
- Migrant proportion percentage

**📈 Linguistic Features Tab**
- Evolution of all 4 features
- Blue = Locals, Red = Migrants

**📋 Summary Statistics Tab**
- Detailed numerical results
- Population changes
- Feature adoption rates

### Step 5: Export Data (Optional)
- Click **"Export Data"** button
- Choose location and filename
- Data saved as CSV for further analysis

## 💡 Quick Examples

### Example 1: Baseline (Default)
Just click "Run Simulation" with default parameters.

### Example 2: High Immigration
1. Change "Annual Immigration" to **300**
2. Click "Run Simulation"
3. See faster demographic shift

### Example 3: Low Media
1. Change "Media Influence" to **0.1**
2. Click "Run Simulation"
3. See reduced linguistic change

### Example 4: Short Simulation
1. Change "Simulation Years" to **5**
2. Click "Run Simulation"
3. See early dynamics (faster execution)

## 🎯 Key Features

✅ **Interactive**: Adjust all parameters through GUI  
✅ **Real-time**: Progress bar shows simulation status  
✅ **Visual**: Embedded plots update automatically  
✅ **Export**: Save results to CSV with one click  
✅ **Stop**: Halt simulation at any time  
✅ **Reset**: Restore default parameters instantly  

## 🛠️ Troubleshooting

**GUI doesn't open?**
- Make sure tkinter is installed: `python3 -m tkinter`
- Check that you're in the correct directory

**"Invalid Input" error?**
- Ensure all values are numbers
- Population values must be whole numbers (no decimals)
- Rates must be between 0 and 1

**Simulation too slow?**
- Reduce population sizes (e.g., 500 locals, 50 migrants)
- Reduce simulation years (e.g., 10 years)

## 📚 More Information

- **Full documentation**: See `GUI_README.md`
- **Model details**: See `README.md`
- **Usage guide**: See `USAGE_GUIDE.md`

---

**Enjoy exploring the model interactively!** 🎉
