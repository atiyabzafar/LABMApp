# Language Evolution Through Immigration Dynamics - Interactive Application

## 🌍 Application Overview

This interactive application allows you to explore **Language Evolution Through Immigration Dynamics** using agent-based modeling. It simulates how cultural norms evolve when populations with different linguistic features come into sustained contact through immigration.

## 🔬 What the App Does

The application models the evolution of Portuguese language features under the influence of Brazilian immigration to Portugal. Using agent-based modeling, it tracks how 4 key linguistic features (vocabulary, grammar, phonetics, pronouns) change over time across two populations (locals and migrants) distributed across 18 Portuguese districts.

### Core Research Question
How do cultural traits evolve when immigrant and host populations interact? Does immigration lead to cultural assimilation, hybrid forms, or bidirectional influence?

## 🎛️ Application Features

### Two Interface Options

1. **🌐 Streamlit Web Application** (`streamlit_app.py`)
   - Browser-based interface
   - Interactive parameter controls
   - Real-time visualization
   - Data export capabilities
   - Mobile-friendly responsive design

2. **🖥️ Tkinter Desktop Application** (`gui_app.py`)
   - Native desktop window
   - Comprehensive parameter panel
   - Multi-tab results display
   - Advanced visualization options

## 📊 Simulation Parameters

### Population Parameters
- **Initial Locals**: Starting number of local Portuguese agents (default: 1,000)
- **Initial Migrants**: Starting number of Brazilian migrant agents (default: 100)
- **Annual Immigration**: Number of new Brazilian immigrants per year (default: 120)

### Demographic Rates
- **Local Birth Rate**: Annual birth rate for local population (default: 0.04)
- **Migrant Birth Rate**: Annual birth rate for migrant population (default: 0.06)

### Social Interactions
- **School Interactions**: Monthly peer interactions in educational settings (default: 5)
- **Workplace Interactions**: Monthly colleague interactions at work (default: 3)
- **Public Interaction Probability**: Monthly probability of random public encounters (default: 0.3)

### Media & Identity Factors
- **Media Influence**: Base influence of media exposure on language features (default: 0.5)
- **Locals Reveal %**: Proportion of locals revealing Brazilian features in interactions (default: 0.3)
- **Migrants Reveal %**: Proportion of migrants revealing Brazilian features in interactions (default: 0.7)

### Linguistic Influence Rates
- **Vocabulary Rate**: Influence rate for vocabulary adoption per interaction (default: 0.5)
- **Grammar Rate**: Influence rate for grammar adoption per interaction (default: 0.3)
- **Pronoun Rate**: Influence rate for pronoun adoption per interaction (default: 0.25)
- **Phonetic Rate**: Influence rate for phonetic adoption per interaction (default: 0.15)

### Simulation Settings
- **Simulation Years**: Duration of simulation in years (default: 20)

## 🎯 Model Components

### Agent Types
- **Local Agents**: Represent native Portuguese population
- **Migrant Agents**: Represent Brazilian immigrant population
- **New Immigrants**: Annual inflow of Brazilian migrants

### Linguistic Features Tracked
1. **Vocabulary**: Individual words and expressions (easiest to adopt)
2. **Grammar**: Syntactic structures and rules (moderate difficulty)
3. **Pronouns**: Pronoun usage patterns (moderate difficulty)
4. **Phonetics**: Pronunciation patterns (most resistant to change)

### Spatial Structure
- **18 Portuguese Districts**: Realistic geographical distribution
- **Urban/Rural Classification**: Different districts have different economic attractiveness
- **Migration Patterns**: Based on economic opportunities and ethnic networks

### Interaction Contexts
- **School**: Educational environment interactions
- **Workplace**: Professional environment interactions
- **Public Spaces**: Random encounters in public areas
- **Media Exposure**: Mass media influence on language features

## 📈 Output Metrics

### Demographic Evolution
- Population sizes over time (locals vs migrants)
- Migrant proportion trends
- Age structure changes
- Birth and death dynamics

### Linguistic Integration
- Adoption rates by locals for each linguistic feature
- Heritage retention rates by migrants for each feature
- Differential diffusion patterns across feature types
- Critical mass effects and tipping points

### Spatial Distribution
- Final population distribution across districts
- Urban concentration patterns
- Consistency of migrant proportions across regions

## 🔧 Technical Implementation

### Model Architecture
- **Agent-Based**: Individual agents with unique characteristics and behaviors
- **Spatially Explicit**: Agents distributed across 18 Portuguese districts
- **Demographically Realistic**: Includes aging, birth, death, and migration processes
- **Multi-Feature**: Tracks 4 distinct linguistic features simultaneously

### Simulation Engine
- **Time-Stepped**: Monthly time steps over specified years
- **Stochastic**: Probabilistic interactions and outcomes
- **Calibrated Parameters**: Based on empirical Portuguese-Brazilian data
- **Performance Optimized**: Efficient computation for interactive use

### Visualization System
- **Real-Time Plots**: Dynamic generation of charts and graphs
- **Interactive Controls**: Parameter adjustment with immediate feedback
- **Multiple Views**: Demographics, linguistic features, and statistics tabs
- **Export Capabilities**: CSV data export for external analysis

## 🎮 How to Use the Application

### Getting Started
1. **Choose Interface**: Web app (recommended) or desktop app
2. **Adjust Parameters**: Modify any of the parameters described above
3. **Run Simulation**: Click the run button to start the simulation
4. **Explore Results**: View results across multiple tabs
5. **Export Data**: Download results for further analysis

### Parameter Experimentation
- **Test Scenarios**: Try different immigration rates, interaction frequencies, or time periods
- **Compare Outcomes**: See how parameter changes affect linguistic evolution
- **Identify Patterns**: Look for critical thresholds and tipping points
- **Validate Hypotheses**: Test theoretical predictions about cultural evolution

### Understanding Results
- **Demographics Tab**: Track population changes and migrant proportions
- **Linguistic Features Tab**: Monitor adoption and retention of Brazilian features
- **Statistics Tab**: View comprehensive numerical summaries
- **Export Tab**: Download data for statistical analysis

## 📊 Expected Outcomes

### Typical Simulation Results (20-year default)
- **Local Population**: Declines from 1,000 to ~741 (-26% due to aging)
- **Migrant Population**: Grows from 100 to ~2,962 (+2,862% due to immigration + births)
- **Migrant Proportion**: Increases from 9% to 80%
- **Critical Threshold**: Migrant influence accelerates around 30-40% migrant proportion

### Linguistic Evolution Patterns
- **Vocabulary**: Highest adoption by locals (~45% Brazilian features)
- **Grammar**: Moderate adoption (~41% Brazilian features)
- **Pronouns**: Moderate adoption (~46% Brazilian features)
- **Phonetics**: Lowest adoption (~35% Brazilian features)

### Heritage Retention by Migrants
- **Vocabulary**: ~95% retention (slight decline due to local influence)
- **Grammar**: ~94% retention
- **Phonetics**: ~92% retention (most stable)
- **Pronouns**: ~89% retention

## 🔬 Research Applications

### For Cultural Evolution Studies
- Test hypotheses about cultural transmission mechanisms
- Explore conditions for successful cultural integration
- Investigate critical mass effects in cultural change
- Compare different cultural contact scenarios

### For Linguistics Research
- Model language contact and change processes
- Study differential diffusion of linguistic features
- Examine heritage language maintenance patterns
- Investigate spatial patterns of linguistic variation

### For Migration Studies
- Understand cultural integration dynamics
- Model bidirectional cultural influence
- Explore policy implications for immigrant integration
- Study spatial settlement patterns and their effects

## 🚀 Advanced Features

### Interactive Exploration
- Real-time parameter adjustment
- Immediate visual feedback
- Comparative scenario testing
- Sensitivity analysis capabilities

### Data Analysis
- Comprehensive statistical summaries
- Trend analysis and pattern identification
- Export for external statistical software
- Visualization of complex interactions

### Educational Use
- Intuitive interface for students
- Immediate feedback for learning
- Exploration of complex systems concepts
- Demonstration of agent-based modeling

---

**This application provides an interactive gateway to understanding cultural evolution through immigration dynamics, making complex agent-based modeling accessible and explorable.**
