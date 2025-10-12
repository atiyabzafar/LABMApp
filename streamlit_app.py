"""
Streamlit Web App for Brazilian-Portuguese Migration ABM
Easy-to-share web interface for running simulations
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time

from model import MigrationModel
from visualization import export_data_to_csv

# Page configuration
st.set_page_config(
    page_title="Brazilian-Portuguese Migration ABM",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🌍 Brazilian-Portuguese Migration ABM")
st.markdown("""
Explore how cultural norms evolve through immigration using an agent-based model. 
Adjust parameters, run simulations, and visualize results in real-time.
""")

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None
if 'model' not in st.session_state:
    st.session_state.model = None

# Sidebar: Parameters
st.sidebar.header("📊 Simulation Parameters")

# Population parameters
st.sidebar.subheader("Population")
number_locals = st.sidebar.number_input("Initial Locals", min_value=100, max_value=10000, value=1000, step=100)
number_migrants = st.sidebar.number_input("Initial Migrants", min_value=10, max_value=1000, value=100, step=10)
annual_br_inflow = st.sidebar.number_input("Annual Immigration", min_value=10, max_value=500, value=120, step=10)

# Demographic rates
st.sidebar.subheader("Demographic Rates")
local_birth_rate = st.sidebar.slider("Local Birth Rate", 0.01, 0.10, 0.04, 0.01)
migrant_birth_rate = st.sidebar.slider("Migrant Birth Rate", 0.01, 0.10, 0.06, 0.01)

# Social interactions
st.sidebar.subheader("Social Interactions")
num_school_interactions = st.sidebar.slider("School Interactions/Month", 1, 20, 5, 1)
num_workplace_interactions = st.sidebar.slider("Workplace Interactions/Month", 1, 10, 3, 1)
prob_interaction_market = st.sidebar.slider("Public Interaction Probability", 0.0, 1.0, 0.3, 0.05)

# Media and identity
st.sidebar.subheader("Media & Identity")
base_media_influence = st.sidebar.slider("Media Influence", 0.0, 1.0, 0.5, 0.1)
reveal_share_locals = st.sidebar.slider("Locals Reveal %", 0.0, 1.0, 0.3, 0.05)
reveal_share_migrants = st.sidebar.slider("Migrants Reveal %", 0.0, 1.0, 0.7, 0.05)

# Linguistic influence rates
st.sidebar.subheader("Linguistic Influence Rates")
vocab_influence_rate = st.sidebar.slider("Vocabulary Rate", 0.1, 1.0, 0.5, 0.05)
grammar_influence_rate = st.sidebar.slider("Grammar Rate", 0.1, 1.0, 0.3, 0.05)
pronoun_influence_rate = st.sidebar.slider("Pronoun Rate", 0.1, 1.0, 0.25, 0.05)
phonetic_influence_rate = st.sidebar.slider("Phonetic Rate", 0.05, 0.5, 0.15, 0.05)

# Simulation duration
st.sidebar.subheader("Simulation")
simulation_years = st.sidebar.slider("Simulation Years", 1, 50, 20, 1)

# Run button
st.sidebar.markdown("---")
run_button = st.sidebar.button("🚀 Run Simulation", type="primary", use_container_width=True)
reset_button = st.sidebar.button("🔄 Reset to Defaults", use_container_width=True)

# Reset functionality
if reset_button:
    st.rerun()

# Main content area
if run_button:
    # Collect parameters
    params = {
        "number_locals": int(number_locals),
        "number_migrants": int(number_migrants),
        "annual_br_inflow": int(annual_br_inflow),
        "local_birth_rate": local_birth_rate,
        "migrant_birth_rate": migrant_birth_rate,
        "num_school_interactions": int(num_school_interactions),
        "num_workplace_interactions": int(num_workplace_interactions),
        "prob_interaction_market": prob_interaction_market,
        "base_media_influence": base_media_influence,
        "reveal_share_locals": reveal_share_locals,
        "reveal_share_migrants": reveal_share_migrants,
        "vocab_influence_rate": vocab_influence_rate,
        "grammar_influence_rate": grammar_influence_rate,
        "pronoun_influence_rate": pronoun_influence_rate,
        "phonetic_influence_rate": phonetic_influence_rate,
    }
    
    # Run simulation
    with st.spinner(f"Running simulation for {simulation_years} years..."):
        # Create progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Initialize model
        model = MigrationModel(params)
        model.setup()
        
        # Run simulation with progress updates
        total_steps = simulation_years * 12
        for step in range(total_steps):
            model.step()
            
            # Update progress
            progress = (step + 1) / total_steps
            progress_bar.progress(progress)
            status_text.text(f"Year {step//12 + 1}/{simulation_years}, Month {step%12 + 1}")
        
        # Get results
        st.session_state.results = model.get_results()
        st.session_state.model = model
        
        progress_bar.empty()
        status_text.empty()
        st.success("✅ Simulation complete!")

# Display results if available
if st.session_state.results is not None:
    results = st.session_state.results
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Demographics", "📈 Linguistic Features", "📋 Statistics", "💾 Export"])
    
    with tab1:
        st.header("Population Dynamics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Population sizes
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            years = [t/12 for t in results["tick"]]
            ax1.plot(years, results["total_locals"], label="Locals", color="blue", linewidth=2)
            ax1.plot(years, results["total_migrants"], label="Migrants", color="red", linewidth=2)
            ax1.set_xlabel("Year", fontsize=12)
            ax1.set_ylabel("Population", fontsize=12)
            ax1.set_title("Population Over Time", fontsize=14, fontweight='bold')
            ax1.legend(fontsize=10)
            ax1.grid(True, alpha=0.3)
            st.pyplot(fig1)
        
        with col2:
            # Migrant proportion
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            total_pop = [l + m for l, m in zip(results["total_locals"], results["total_migrants"])]
            migrant_prop = [m / t * 100 if t > 0 else 0 for m, t in zip(results["total_migrants"], total_pop)]
            ax2.plot(years, migrant_prop, color="purple", linewidth=2)
            ax2.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label="50% threshold")
            ax2.set_xlabel("Year", fontsize=12)
            ax2.set_ylabel("Migrant Proportion (%)", fontsize=12)
            ax2.set_title("Migrant Proportion Over Time", fontsize=14, fontweight='bold')
            ax2.legend(fontsize=10)
            ax2.grid(True, alpha=0.3)
            st.pyplot(fig2)
    
    with tab2:
        st.header("Linguistic Feature Evolution")
        
        # Create 2x2 subplot
        fig3, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        years = [t/12 for t in results["tick"]]
        
        # Vocabulary
        ax1.plot(years, results["mean_local_vocab"], label="Locals", color="blue", linewidth=2)
        ax1.plot(years, results["mean_migrant_vocab"], label="Migrants", color="red", linewidth=2)
        ax1.set_title("Vocabulary", fontsize=12, fontweight='bold')
        ax1.set_ylabel("Brazilian Feature (%)", fontsize=10)
        ax1.legend(fontsize=9)
        ax1.grid(True, alpha=0.3)
        
        # Grammar
        ax2.plot(years, results["mean_local_grammar"], label="Locals", color="blue", linewidth=2)
        ax2.plot(years, results["mean_migrant_grammar"], label="Migrants", color="red", linewidth=2)
        ax2.set_title("Grammar", fontsize=12, fontweight='bold')
        ax2.legend(fontsize=9)
        ax2.grid(True, alpha=0.3)
        
        # Phonetics
        ax3.plot(years, results["mean_local_phonetics"], label="Locals", color="blue", linewidth=2)
        ax3.plot(years, results["mean_migrant_phonetics"], label="Migrants", color="red", linewidth=2)
        ax3.set_title("Phonetics", fontsize=12, fontweight='bold')
        ax3.set_xlabel("Year", fontsize=10)
        ax3.set_ylabel("Brazilian Feature (%)", fontsize=10)
        ax3.legend(fontsize=9)
        ax3.grid(True, alpha=0.3)
        
        # Pronouns
        ax4.plot(years, results["mean_local_pronouns"], label="Locals", color="blue", linewidth=2)
        ax4.plot(years, results["mean_migrant_pronouns"], label="Migrants", color="red", linewidth=2)
        ax4.set_title("Pronouns", fontsize=12, fontweight='bold')
        ax4.set_xlabel("Year", fontsize=10)
        ax4.legend(fontsize=9)
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig3)
        
        # Feature comparison
        st.subheader("Feature Adoption Comparison (Locals)")
        fig4, ax = plt.subplots(figsize=(12, 6))
        ax.plot(years, results["mean_local_vocab"], label="Vocabulary", linewidth=2)
        ax.plot(years, results["mean_local_grammar"], label="Grammar", linewidth=2)
        ax.plot(years, results["mean_local_phonetics"], label="Phonetics", linewidth=2)
        ax.plot(years, results["mean_local_pronouns"], label="Pronouns", linewidth=2)
        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Brazilian Feature (%)", fontsize=12)
        ax.set_title("Comparative Feature Adoption by Locals", fontsize=14, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig4)
    
    with tab3:
        st.header("Summary Statistics")
        
        # Calculate statistics
        initial_locals = results["total_locals"][0]
        final_locals = results["total_locals"][-1]
        initial_migrants = results["total_migrants"][0]
        final_migrants = results["total_migrants"][-1]
        
        # Demographics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Final Local Population",
                f"{final_locals:,}",
                f"{(final_locals-initial_locals)/initial_locals*100:+.1f}%"
            )
        
        with col2:
            st.metric(
                "Final Migrant Population",
                f"{final_migrants:,}",
                f"{(final_migrants-initial_migrants)/initial_migrants*100:+.1f}%"
            )
        
        with col3:
            st.metric(
                "Final Migrant Proportion",
                f"{final_migrants/(final_locals+final_migrants)*100:.1f}%",
                f"{final_migrants/(final_locals+final_migrants)*100 - initial_migrants/(initial_locals+initial_migrants)*100:+.1f}pp"
            )
        
        st.markdown("---")
        
        # Linguistic integration
        st.subheader("Linguistic Integration (Locals)")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Vocabulary",
                f"{results['mean_local_vocab'][-1]:.1f}%",
                f"{results['mean_local_vocab'][-1] - results['mean_local_vocab'][0]:+.1f}%"
            )
        
        with col2:
            st.metric(
                "Grammar",
                f"{results['mean_local_grammar'][-1]:.1f}%",
                f"{results['mean_local_grammar'][-1] - results['mean_local_grammar'][0]:+.1f}%"
            )
        
        with col3:
            st.metric(
                "Phonetics",
                f"{results['mean_local_phonetics'][-1]:.1f}%",
                f"{results['mean_local_phonetics'][-1] - results['mean_local_phonetics'][0]:+.1f}%"
            )
        
        with col4:
            st.metric(
                "Pronouns",
                f"{results['mean_local_pronouns'][-1]:.1f}%",
                f"{results['mean_local_pronouns'][-1] - results['mean_local_pronouns'][0]:+.1f}%"
            )
        
        st.markdown("---")
        
        # Heritage retention
        st.subheader("Heritage Retention (Migrants)")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Vocabulary",
                f"{results['mean_migrant_vocab'][-1]:.1f}%",
                f"{results['mean_migrant_vocab'][-1] - results['mean_migrant_vocab'][0]:+.1f}%"
            )
        
        with col2:
            st.metric(
                "Grammar",
                f"{results['mean_migrant_grammar'][-1]:.1f}%",
                f"{results['mean_migrant_grammar'][-1] - results['mean_migrant_grammar'][0]:+.1f}%"
            )
        
        with col3:
            st.metric(
                "Phonetics",
                f"{results['mean_migrant_phonetics'][-1]:.1f}%",
                f"{results['mean_migrant_phonetics'][-1] - results['mean_migrant_phonetics'][0]:+.1f}%"
            )
        
        with col4:
            st.metric(
                "Pronouns",
                f"{results['mean_migrant_pronouns'][-1]:.1f}%",
                f"{results['mean_migrant_pronouns'][-1] - results['mean_migrant_pronouns'][0]:+.1f}%"
            )
    
    with tab4:
        st.header("Export Data")
        
        st.markdown("""
        Download the simulation results as a CSV file for further analysis in Excel, R, Python, or other tools.
        """)
        
        # Convert to DataFrame
        df = pd.DataFrame(results)
        df['year'] = df['tick'] / 12
        
        # Show preview
        st.subheader("Data Preview")
        st.dataframe(df.head(10), use_container_width=True)
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="simulation_results.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        st.info(f"**Total data points:** {len(df)} months ({len(df)/12:.1f} years)")

else:
    # Show welcome message
    st.info("👈 Adjust parameters in the sidebar and click **Run Simulation** to start!")
    
    st.markdown("""
    ### About This Model
    
    This agent-based model simulates the evolution of cultural norms through Brazilian immigration to Portugal, 
    using language as a proxy for broader cultural change.
    
    **Key Features:**
    - 🎯 Track 4 linguistic features (vocabulary, grammar, phonetics, pronouns)
    - 👥 Model 2 populations (locals and migrants)
    - 🏘️ Simulate across 18 Portuguese districts
    - 📊 Realistic demographics (aging, births, deaths)
    - 🤝 Multiple interaction contexts (school, workplace, public)
    - 📺 Media exposure effects
    
    **How to Use:**
    1. Adjust parameters in the sidebar
    2. Click "Run Simulation"
    3. Explore results in the tabs above
    4. Export data for further analysis
    
    ### Example Scenarios
    
    **High Immigration:** Increase "Annual Immigration" to 300  
    **Low Media Influence:** Decrease "Media Influence" to 0.1  
    **Intensive Interactions:** Increase school and workplace interactions  
    **Short-term Analysis:** Set "Simulation Years" to 5
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Brazilian-Portuguese Migration ABM | Agent-Based Model for Cultural Evolution</p>
    <p><small>Developed for research on immigration dynamics and cultural integration</small></p>
</div>
""", unsafe_allow_html=True)
