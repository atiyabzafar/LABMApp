"""
GUI Application for Brazilian-Portuguese Migration ABM
Interactive interface for running simulations with custom parameters
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

from model import MigrationModel
from visualization import plot_all_features_comparison, export_data_to_csv


class MigrationModelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Brazilian-Portuguese Migration ABM")
        self.root.geometry("1400x900")
        
        # Model and results
        self.model = None
        self.results = None
        self.is_running = False
        
        # Create main layout
        self.create_widgets()
        
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Main container with two columns
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # Left panel: Parameters
        self.create_parameter_panel(main_frame)
        
        # Right panel: Results
        self.create_results_panel(main_frame)
        
    def create_parameter_panel(self, parent):
        """Create parameter input panel"""
        
        param_frame = ttk.LabelFrame(parent, text="Simulation Parameters", padding="10")
        param_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        
        # Scrollable frame for parameters
        canvas = tk.Canvas(param_frame, width=400)
        scrollbar = ttk.Scrollbar(param_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Parameter dictionary to store entry widgets
        self.param_entries = {}
        
        # Define parameter groups
        param_groups = [
            ("Population", [
                ("number_locals", "Initial Locals", 1000, "Number of initial local agents"),
                ("number_migrants", "Initial Migrants", 100, "Number of initial migrant agents"),
                ("annual_br_inflow", "Annual Immigration", 120, "Brazilian immigrants per year"),
            ]),
            ("Demographic Rates", [
                ("local_birth_rate", "Local Birth Rate", 0.04, "Annual birth rate for locals"),
                ("migrant_birth_rate", "Migrant Birth Rate", 0.06, "Annual birth rate for migrants"),
            ]),
            ("Social Interactions", [
                ("num_school_interactions", "School Interactions", 5, "Monthly peer interactions"),
                ("num_workplace_interactions", "Workplace Interactions", 3, "Monthly colleague interactions"),
                ("prob_interaction_market", "Public Interaction Prob", 0.3, "Monthly probability of public encounter"),
            ]),
            ("Media & Identity", [
                ("base_media_influence", "Media Influence", 0.5, "Base media influence (0-1)"),
                ("reveal_share_locals", "Locals Reveal %", 0.3, "Proportion of locals revealing BR features"),
                ("reveal_share_migrants", "Migrants Reveal %", 0.7, "Proportion of migrants revealing BR features"),
            ]),
            ("Linguistic Influence Rates", [
                ("vocab_influence_rate", "Vocabulary Rate", 0.5, "Vocabulary influence per interaction"),
                ("grammar_influence_rate", "Grammar Rate", 0.3, "Grammar influence per interaction"),
                ("pronoun_influence_rate", "Pronoun Rate", 0.25, "Pronoun influence per interaction"),
                ("phonetic_influence_rate", "Phonetic Rate", 0.15, "Phonetic influence per interaction"),
            ]),
            ("Simulation", [
                ("simulation_years", "Simulation Years", 20, "Number of years to simulate"),
            ]),
        ]
        
        row = 0
        for group_name, params in param_groups:
            # Group header
            group_label = ttk.Label(scrollable_frame, text=group_name, font=("Arial", 10, "bold"))
            group_label.grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
            row += 1
            
            # Parameters in group
            for param_key, param_label, default_value, tooltip in params:
                label = ttk.Label(scrollable_frame, text=param_label + ":")
                label.grid(row=row, column=0, sticky=tk.W, pady=2, padx=(10, 5))
                
                entry = ttk.Entry(scrollable_frame, width=15)
                entry.insert(0, str(default_value))
                entry.grid(row=row, column=1, sticky=tk.W, pady=2)
                
                # Store entry widget
                self.param_entries[param_key] = entry
                
                # Tooltip (simplified - just show on label)
                self.create_tooltip(label, tooltip)
                
                row += 1
        
        # Control buttons
        button_frame = ttk.Frame(param_frame)
        button_frame.pack(side="bottom", fill="x", pady=(10, 0))
        
        self.run_button = ttk.Button(button_frame, text="Run Simulation", command=self.run_simulation)
        self.run_button.pack(side="left", padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_simulation, state="disabled")
        self.stop_button.pack(side="left", padx=5)
        
        reset_button = ttk.Button(button_frame, text="Reset to Defaults", command=self.reset_parameters)
        reset_button.pack(side="left", padx=5)
        
        export_button = ttk.Button(button_frame, text="Export Data", command=self.export_data, state="disabled")
        export_button.pack(side="left", padx=5)
        self.export_button = export_button
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(param_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(side="bottom", fill="x", pady=(5, 0))
        
        # Status label
        self.status_label = ttk.Label(param_frame, text="Ready", foreground="green")
        self.status_label.pack(side="bottom", pady=(5, 0))
        
    def create_results_panel(self, parent):
        """Create results display panel"""
        
        results_frame = ttk.LabelFrame(parent, text="Simulation Results", padding="10")
        results_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        
        # Notebook for different views
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill="both", expand=True)
        
        # Tab 1: Demographics
        self.demo_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.demo_tab, text="Demographics")
        
        # Tab 2: Linguistic Features
        self.features_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.features_tab, text="Linguistic Features")
        
        # Tab 3: Summary Statistics
        self.stats_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_tab, text="Summary Statistics")
        
        # Initialize with placeholder
        self.show_placeholder()
        
    def create_tooltip(self, widget, text):
        """Create a simple tooltip for a widget"""
        def on_enter(event):
            self.status_label.config(text=text, foreground="blue")
        
        def on_leave(event):
            if not self.is_running:
                self.status_label.config(text="Ready", foreground="green")
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
        
    def show_placeholder(self):
        """Show placeholder text before simulation runs"""
        for tab in [self.demo_tab, self.features_tab, self.stats_tab]:
            for widget in tab.winfo_children():
                widget.destroy()
            
            label = ttk.Label(tab, text="Run a simulation to see results", 
                            font=("Arial", 12), foreground="gray")
            label.pack(expand=True)
    
    def get_parameters(self):
        """Get parameters from entry widgets"""
        params = {}
        
        # Get all parameters
        for key, entry in self.param_entries.items():
            try:
                value = entry.get()
                # Convert to appropriate type
                if key in ["number_locals", "number_migrants", "annual_br_inflow", 
                          "num_school_interactions", "num_workplace_interactions", "simulation_years"]:
                    params[key] = int(value)
                else:
                    params[key] = float(value)
            except ValueError:
                messagebox.showerror("Invalid Input", f"Invalid value for {key}: {value}")
                return None
        
        return params
    
    def reset_parameters(self):
        """Reset all parameters to defaults"""
        defaults = {
            "number_locals": 1000,
            "number_migrants": 100,
            "annual_br_inflow": 120,
            "local_birth_rate": 0.04,
            "migrant_birth_rate": 0.06,
            "num_school_interactions": 5,
            "num_workplace_interactions": 3,
            "prob_interaction_market": 0.3,
            "base_media_influence": 0.5,
            "reveal_share_locals": 0.3,
            "reveal_share_migrants": 0.7,
            "vocab_influence_rate": 0.5,
            "grammar_influence_rate": 0.3,
            "pronoun_influence_rate": 0.25,
            "phonetic_influence_rate": 0.15,
            "simulation_years": 20,
        }
        
        for key, value in defaults.items():
            if key in self.param_entries:
                self.param_entries[key].delete(0, tk.END)
                self.param_entries[key].insert(0, str(value))
    
    def run_simulation(self):
        """Run the simulation in a separate thread"""
        
        # Get parameters
        params = self.get_parameters()
        if params is None:
            return
        
        # Extract simulation years
        simulation_years = params.pop("simulation_years")
        
        # Disable run button, enable stop button
        self.run_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.export_button.config(state="disabled")
        self.is_running = True
        
        # Update status
        self.status_label.config(text="Initializing simulation...", foreground="orange")
        self.progress_var.set(0)
        
        # Run in thread
        thread = threading.Thread(target=self._run_simulation_thread, args=(params, simulation_years))
        thread.daemon = True
        thread.start()
    
    def _run_simulation_thread(self, params, simulation_years):
        """Run simulation in background thread"""
        try:
            # Create model
            self.model = MigrationModel(params)
            self.model.setup()
            
            # Run simulation with progress updates
            total_steps = simulation_years * 12
            for step in range(total_steps):
                if not self.is_running:
                    self.root.after(0, self.update_status, "Simulation stopped", "red")
                    break
                
                self.model.step()
                
                # Update progress
                progress = (step + 1) / total_steps * 100
                self.root.after(0, self.progress_var.set, progress)
                self.root.after(0, self.update_status, 
                              f"Running: Year {step//12 + 1}/{simulation_years}, Month {step%12 + 1}", 
                              "orange")
            
            if self.is_running:
                # Get results
                self.results = self.model.get_results()
                
                # Update GUI with results
                self.root.after(0, self.display_results)
                self.root.after(0, self.update_status, "Simulation complete!", "green")
            
        except Exception as e:
            self.root.after(0, messagebox.showerror, "Simulation Error", str(e))
            self.root.after(0, self.update_status, f"Error: {str(e)}", "red")
        
        finally:
            # Re-enable buttons
            self.root.after(0, self.run_button.config, {"state": "normal"})
            self.root.after(0, self.stop_button.config, {"state": "disabled"})
            self.root.after(0, self.export_button.config, {"state": "normal"})
            self.is_running = False
    
    def stop_simulation(self):
        """Stop the running simulation"""
        self.is_running = False
        self.stop_button.config(state="disabled")
    
    def update_status(self, text, color):
        """Update status label"""
        self.status_label.config(text=text, foreground=color)
    
    def display_results(self):
        """Display simulation results in tabs"""
        
        # Clear existing widgets
        for tab in [self.demo_tab, self.features_tab, self.stats_tab]:
            for widget in tab.winfo_children():
                widget.destroy()
        
        # Tab 1: Demographics
        self.plot_demographics(self.demo_tab)
        
        # Tab 2: Linguistic Features
        self.plot_features(self.features_tab)
        
        # Tab 3: Summary Statistics
        self.show_statistics(self.stats_tab)
    
    def plot_demographics(self, parent):
        """Plot demographic dynamics"""
        fig = Figure(figsize=(8, 6), dpi=100)
        
        # Two subplots
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        
        years = [t/12 for t in self.results["tick"]]
        
        # Population sizes
        ax1.plot(years, self.results["total_locals"], label="Locals", color="blue", linewidth=2)
        ax1.plot(years, self.results["total_migrants"], label="Migrants", color="red", linewidth=2)
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Population")
        ax1.set_title("Population Dynamics")
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Migrant proportion
        total_pop = [l + m for l, m in zip(self.results["total_locals"], self.results["total_migrants"])]
        migrant_prop = [m / t * 100 if t > 0 else 0 for m, t in zip(self.results["total_migrants"], total_pop)]
        ax2.plot(years, migrant_prop, color="purple", linewidth=2)
        ax2.set_xlabel("Year")
        ax2.set_ylabel("Migrant Proportion (%)")
        ax2.set_title("Migrant Proportion Over Time")
        ax2.grid(True, alpha=0.3)
        ax2.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label="50% threshold")
        ax2.legend()
        
        fig.tight_layout()
        
        # Embed in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def plot_features(self, parent):
        """Plot linguistic features"""
        fig = Figure(figsize=(8, 6), dpi=100)
        
        # Four subplots
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)
        
        years = [t/12 for t in self.results["tick"]]
        
        # Vocabulary
        ax1.plot(years, self.results["mean_local_vocab"], label="Locals", color="blue", linewidth=2)
        ax1.plot(years, self.results["mean_migrant_vocab"], label="Migrants", color="red", linewidth=2)
        ax1.set_title("Vocabulary")
        ax1.set_ylabel("Brazilian Feature (%)")
        ax1.legend(fontsize=8)
        ax1.grid(True, alpha=0.3)
        
        # Grammar
        ax2.plot(years, self.results["mean_local_grammar"], color="blue", linewidth=2)
        ax2.plot(years, self.results["mean_migrant_grammar"], color="red", linewidth=2)
        ax2.set_title("Grammar")
        ax2.grid(True, alpha=0.3)
        
        # Phonetics
        ax3.plot(years, self.results["mean_local_phonetics"], color="blue", linewidth=2)
        ax3.plot(years, self.results["mean_migrant_phonetics"], color="red", linewidth=2)
        ax3.set_title("Phonetics")
        ax3.set_xlabel("Year")
        ax3.set_ylabel("Brazilian Feature (%)")
        ax3.grid(True, alpha=0.3)
        
        # Pronouns
        ax4.plot(years, self.results["mean_local_pronouns"], color="blue", linewidth=2)
        ax4.plot(years, self.results["mean_migrant_pronouns"], color="red", linewidth=2)
        ax4.set_title("Pronouns")
        ax4.set_xlabel("Year")
        ax4.grid(True, alpha=0.3)
        
        fig.tight_layout()
        
        # Embed in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def show_statistics(self, parent):
        """Show summary statistics"""
        
        # Create scrollable text widget
        text_frame = ttk.Frame(parent)
        text_frame.pack(fill="both", expand=True)
        
        text = tk.Text(text_frame, wrap="word", font=("Courier", 10))
        scrollbar = ttk.Scrollbar(text_frame, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set)
        
        text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Calculate statistics
        initial_locals = self.results["total_locals"][0]
        final_locals = self.results["total_locals"][-1]
        initial_migrants = self.results["total_migrants"][0]
        final_migrants = self.results["total_migrants"][-1]
        
        initial_vocab = self.results["mean_local_vocab"][0]
        final_vocab = self.results["mean_local_vocab"][-1]
        initial_grammar = self.results["mean_local_grammar"][0]
        final_grammar = self.results["mean_local_grammar"][-1]
        initial_phonetics = self.results["mean_local_phonetics"][0]
        final_phonetics = self.results["mean_local_phonetics"][-1]
        initial_pronouns = self.results["mean_local_pronouns"][0]
        final_pronouns = self.results["mean_local_pronouns"][-1]
        
        # Format statistics
        stats_text = f"""
SIMULATION SUMMARY STATISTICS
{'='*60}

DEMOGRAPHIC OUTCOMES
{'-'*60}
Initial Population:
  Locals:    {initial_locals:,}
  Migrants:  {initial_migrants:,}
  Total:     {initial_locals + initial_migrants:,}

Final Population:
  Locals:    {final_locals:,} ({(final_locals-initial_locals)/initial_locals*100:+.1f}%)
  Migrants:  {final_migrants:,} ({(final_migrants-initial_migrants)/initial_migrants*100:+.1f}%)
  Total:     {final_locals + final_migrants:,}

Migrant Proportion:
  Initial:   {initial_migrants/(initial_locals+initial_migrants)*100:.1f}%
  Final:     {final_migrants/(final_locals+final_migrants)*100:.1f}%

LINGUISTIC INTEGRATION (LOCALS)
{'-'*60}
Brazilian Vocabulary:
  Initial:   {initial_vocab:.2f}%
  Final:     {final_vocab:.2f}%
  Change:    {final_vocab - initial_vocab:+.2f}%

Brazilian Grammar:
  Initial:   {initial_grammar:.2f}%
  Final:     {final_grammar:.2f}%
  Change:    {final_grammar - initial_grammar:+.2f}%

Brazilian Phonetics:
  Initial:   {initial_phonetics:.2f}%
  Final:     {final_phonetics:.2f}%
  Change:    {final_phonetics - initial_phonetics:+.2f}%

Brazilian Pronouns:
  Initial:   {initial_pronouns:.2f}%
  Final:     {final_pronouns:.2f}%
  Change:    {final_pronouns - initial_pronouns:+.2f}%

MIGRANT HERITAGE RETENTION
{'-'*60}
Brazilian Vocabulary:  {self.results["mean_migrant_vocab"][-1]:.2f}%
Brazilian Grammar:     {self.results["mean_migrant_grammar"][-1]:.2f}%
Brazilian Phonetics:   {self.results["mean_migrant_phonetics"][-1]:.2f}%
Brazilian Pronouns:    {self.results["mean_migrant_pronouns"][-1]:.2f}%

SIMULATION PARAMETERS
{'-'*60}
Duration:              {len(self.results["tick"])/12:.1f} years
Time Steps:            {len(self.results["tick"])} months
"""
        
        text.insert("1.0", stats_text)
        text.config(state="disabled")
    
    def export_data(self):
        """Export simulation data to CSV"""
        if self.results is None:
            messagebox.showwarning("No Data", "Run a simulation first before exporting data.")
            return
        
        # Ask for file location
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile="simulation_results.csv"
        )
        
        if filename:
            try:
                export_data_to_csv(self.results, filename)
                messagebox.showinfo("Export Successful", f"Data exported to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export data:\n{str(e)}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = MigrationModelGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
