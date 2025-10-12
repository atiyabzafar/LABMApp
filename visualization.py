"""
Visualization utilities for the migration simulation.
Creates plots and charts to analyze simulation results.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_linguistic_features(data, save_path=None):
    """
    Plot the evolution of linguistic features over time.
    
    Args:
        data: Dictionary of collected data from the model
        save_path: Optional path to save the figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Evolution of Brazilian Portuguese Features in Locals', fontsize=16, fontweight='bold')
    
    # Convert ticks to years
    years = np.array(data["tick"]) / 12
    
    # Vocabulary
    axes[0, 0].plot(years, data["mean_local_vocab"], 'b-', linewidth=2, label='Locals')
    axes[0, 0].set_xlabel('Years')
    axes[0, 0].set_ylabel('Brazilian Vocabulary (%)')
    axes[0, 0].set_title('Vocabulary (autocarro→ônibus, sumo→suco)')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    
    # Grammar
    axes[0, 1].plot(years, data["mean_local_grammar"], 'g-', linewidth=2, label='Locals')
    axes[0, 1].set_xlabel('Years')
    axes[0, 1].set_ylabel('Brazilian Grammar (%)')
    axes[0, 1].set_title('Grammar (nós vamos→a gente vai)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    
    # Phonetics
    axes[1, 0].plot(years, data["mean_local_phonetics"], 'r-', linewidth=2, label='Locals')
    axes[1, 0].set_xlabel('Years')
    axes[1, 0].set_ylabel('Brazilian Phonetics (%)')
    axes[1, 0].set_title('Phonetics (/t/→/tʃ/ before [i])')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    
    # Pronouns
    axes[1, 1].plot(years, data["mean_local_pronouns"], 'm-', linewidth=2, label='Locals')
    axes[1, 1].set_xlabel('Years')
    axes[1, 1].set_ylabel('Brazilian Pronouns (%)')
    axes[1, 1].set_title('Pronouns (amo-te→te amo)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved linguistic features plot to {save_path}")
    
    plt.show()


def plot_demographics(data, save_path=None):
    """
    Plot demographic changes over time.
    
    Args:
        data: Dictionary of collected data from the model
        save_path: Optional path to save the figure
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Demographic Dynamics', fontsize=16, fontweight='bold')
    
    years = np.array(data["tick"]) / 12
    
    # Population sizes
    axes[0].plot(years, data["total_locals"], 'b-', linewidth=2, label='Locals')
    axes[0].plot(years, data["total_migrants"], 'r-', linewidth=2, label='Migrants')
    axes[0].set_xlabel('Years')
    axes[0].set_ylabel('Population')
    axes[0].set_title('Population Sizes Over Time')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    
    # Proportion of migrants
    total_pop = np.array(data["total_locals"]) + np.array(data["total_migrants"])
    migrant_proportion = np.array(data["total_migrants"]) / total_pop * 100
    
    axes[1].plot(years, migrant_proportion, 'purple', linewidth=2)
    axes[1].set_xlabel('Years')
    axes[1].set_ylabel('Migrants (%)')
    axes[1].set_title('Proportion of Migrants in Total Population')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved demographics plot to {save_path}")
    
    plt.show()


def plot_all_features_comparison(data, save_path=None):
    """
    Plot all linguistic features on one chart for comparison.
    
    Args:
        data: Dictionary of collected data from the model
        save_path: Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    years = np.array(data["tick"]) / 12
    
    ax.plot(years, data["mean_local_vocab"], 'b-', linewidth=2, label='Vocabulary', marker='o', markersize=3)
    ax.plot(years, data["mean_local_grammar"], 'g-', linewidth=2, label='Grammar', marker='s', markersize=3)
    ax.plot(years, data["mean_local_pronouns"], 'm-', linewidth=2, label='Pronouns', marker='^', markersize=3)
    ax.plot(years, data["mean_local_phonetics"], 'r-', linewidth=2, label='Phonetics', marker='d', markersize=3)
    
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Adoption of Brazilian Features (%)', fontsize=12)
    ax.set_title('Comparative Adoption of Brazilian Portuguese Features by Locals', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved comparison plot to {save_path}")
    
    plt.show()


def plot_migrant_features(data, save_path=None):
    """
    Plot the evolution of linguistic features for migrants (convergence to Portuguese).
    
    Args:
        data: Dictionary of collected data from the model
        save_path: Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    years = np.array(data["tick"]) / 12
    
    ax.plot(years, data["mean_migrant_vocab"], 'b-', linewidth=2, label='Vocabulary', marker='o', markersize=3)
    ax.plot(years, data["mean_migrant_grammar"], 'g-', linewidth=2, label='Grammar', marker='s', markersize=3)
    ax.plot(years, data["mean_migrant_pronouns"], 'm-', linewidth=2, label='Pronouns', marker='^', markersize=3)
    ax.plot(years, data["mean_migrant_phonetics"], 'r-', linewidth=2, label='Phonetics', marker='d', markersize=3)
    
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Brazilian Features Retention (%)', fontsize=12)
    ax.set_title('Retention of Brazilian Portuguese Features by Migrants', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved migrant features plot to {save_path}")
    
    plt.show()


def create_summary_report(data, params):
    """
    Create a text summary of simulation results.
    
    Args:
        data: Dictionary of collected data from the model
        params: Dictionary of model parameters
    """
    print("\n" + "="*60)
    print("SIMULATION SUMMARY REPORT")
    print("="*60)
    
    print("\nModel Parameters:")
    print(f"  Initial Locals: {params.get('number_locals', 'N/A')}")
    print(f"  Initial Migrants: {params.get('number_migrants', 'N/A')}")
    print(f"  Annual Brazilian Inflow: {params.get('annual_br_inflow', 'N/A')}")
    print(f"  Base Media Influence: {params.get('base_media_influence', 'N/A')}")
    print(f"  Reveal Share (Locals): {params.get('reveal_share_locals', 'N/A')}")
    print(f"  Reveal Share (Migrants): {params.get('reveal_share_migrants', 'N/A')}")
    
    print("\nFinal Population:")
    print(f"  Locals: {data['total_locals'][-1]}")
    print(f"  Migrants: {data['total_migrants'][-1]}")
    print(f"  Total: {data['total_locals'][-1] + data['total_migrants'][-1]}")
    print(f"  Migrant Proportion: {data['total_migrants'][-1] / (data['total_locals'][-1] + data['total_migrants'][-1]) * 100:.2f}%")
    
    print("\nLinguistic Integration (Locals):")
    print(f"  Initial → Final Brazilian Vocabulary: {data['mean_local_vocab'][0]:.2f}% → {data['mean_local_vocab'][-1]:.2f}%")
    print(f"  Initial → Final Brazilian Grammar: {data['mean_local_grammar'][0]:.2f}% → {data['mean_local_grammar'][-1]:.2f}%")
    print(f"  Initial → Final Brazilian Phonetics: {data['mean_local_phonetics'][0]:.2f}% → {data['mean_local_phonetics'][-1]:.2f}%")
    print(f"  Initial → Final Brazilian Pronouns: {data['mean_local_pronouns'][0]:.2f}% → {data['mean_local_pronouns'][-1]:.2f}%")
    
    print("\nLinguistic Integration (Migrants):")
    print(f"  Initial → Final Brazilian Vocabulary: {data['mean_migrant_vocab'][0]:.2f}% → {data['mean_migrant_vocab'][-1]:.2f}%")
    print(f"  Initial → Final Brazilian Grammar: {data['mean_migrant_grammar'][0]:.2f}% → {data['mean_migrant_grammar'][-1]:.2f}%")
    print(f"  Initial → Final Brazilian Phonetics: {data['mean_migrant_phonetics'][0]:.2f}% → {data['mean_migrant_phonetics'][-1]:.2f}%")
    print(f"  Initial → Final Brazilian Pronouns: {data['mean_migrant_pronouns'][0]:.2f}% → {data['mean_migrant_pronouns'][-1]:.2f}%")
    
    print("\n" + "="*60)


def export_data_to_csv(data, filename="simulation_results.csv"):
    """
    Export simulation data to CSV file.
    
    Args:
        data: Dictionary of collected data from the model
        filename: Name of the CSV file to create
    """
    import csv
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow([
            'Tick', 'Year', 'Total_Locals', 'Total_Migrants',
            'Local_Vocab', 'Local_Grammar', 'Local_Phonetics', 'Local_Pronouns',
            'Migrant_Vocab', 'Migrant_Grammar', 'Migrant_Phonetics', 'Migrant_Pronouns'
        ])
        
        # Write data
        for i in range(len(data['tick'])):
            writer.writerow([
                data['tick'][i],
                data['tick'][i] / 12,
                data['total_locals'][i],
                data['total_migrants'][i],
                data['mean_local_vocab'][i],
                data['mean_local_grammar'][i],
                data['mean_local_phonetics'][i],
                data['mean_local_pronouns'][i],
                data['mean_migrant_vocab'][i],
                data['mean_migrant_grammar'][i],
                data['mean_migrant_phonetics'][i],
                data['mean_migrant_pronouns'][i],
            ])
    
    print(f"Data exported to {filename}")
