"""
Main simulation model for Brazilian Migration to Portugal.
Implements the agent-based model with demographic and linguistic dynamics.
"""

import random
from collections import defaultdict
from agents import LocalAgent, MigrantAgent, Sex
from districts import create_portugal_districts, select_migration_district


class MigrationModel:
    """Main model class for the Brazilian migration simulation."""
    
    def __init__(self, params):
        """
        Initialize the migration model.
        
        Args:
            params: Dictionary of model parameters
        """
        self.params = params
        self.tick = 0  # 1 tick = 1 month
        self.next_agent_id = 1
        
        # Create districts
        self.districts = create_portugal_districts()
        
        # Agent storage
        self.agents = []
        
        # Data collection
        self.data_collector = {
            "tick": [],
            "total_locals": [],
            "total_migrants": [],
            "mean_local_vocab": [],
            "mean_local_grammar": [],
            "mean_local_phonetics": [],
            "mean_local_pronouns": [],
            "mean_migrant_vocab": [],
            "mean_migrant_grammar": [],
            "mean_migrant_phonetics": [],
            "mean_migrant_pronouns": [],
        }
        
        # Death rates by age (age_range: annual_death_rate)
        self.death_rates = {
            (0, 1): 0.005,
            (1, 5): 0.0005,
            (5, 15): 0.0002,
            (15, 25): 0.0005,
            (25, 35): 0.0008,
            (35, 45): 0.0015,
            (45, 55): 0.003,
            (55, 65): 0.008,
            (65, 75): 0.02,
            (75, 85): 0.05,
            (85, 120): 0.15,
        }
        
        # Birth rates (annual probability for women in fertile age)
        self.birth_rate_locals = params.get("local_birth_rate", 0.04)
        self.birth_rate_migrants = params.get("migrant_birth_rate", 0.06)
        
        # Interaction parameters
        self.num_school_interactions = params.get("num_school_interactions", 5)
        self.num_workplace_interactions = params.get("num_workplace_interactions", 3)
        self.prob_interaction_market = params.get("prob_interaction_market", 0.3)
        
        # Linguistic influence rates (per interaction)
        self.influence_rates = {
            "vocab": params.get("vocab_influence_rate", 0.5),
            "grammar": params.get("grammar_influence_rate", 0.3),
            "pronouns": params.get("pronoun_influence_rate", 0.25),
            "phonetics": params.get("phonetic_influence_rate", 0.15),
        }
    
    def setup(self):
        """Initialize the model with starting populations."""
        print("Setting up model...")
        
        # Create initial local population
        num_locals = self.params.get("number_locals", 1000)
        self._create_initial_locals(num_locals)
        
        # Create initial migrant population
        num_migrants = self.params.get("number_migrants", 100)
        self._create_initial_migrants(num_migrants)
        
        print(f"Created {num_locals} locals and {num_migrants} migrants")
        print(f"Distributed across {len(self.districts)} districts")
    
    def _create_initial_locals(self, num_locals):
        """Create initial local population with realistic age distribution."""
        for _ in range(num_locals):
            # Age distribution (simplified - could use real demographic data)
            age = self._generate_age_from_distribution()
            sex = random.choice([Sex.MALE, Sex.FEMALE])
            
            # Distribute across districts (weighted by economic attractiveness)
            district_id = self._select_district_weighted()
            
            agent = LocalAgent(self.next_agent_id, age, sex, district_id, self)
            self.next_agent_id += 1
            
            self.agents.append(agent)
            self.districts[district_id].add_agent(agent)
    
    def _create_initial_migrants(self, num_migrants):
        """Create initial migrant population."""
        for _ in range(num_migrants):
            # Migrants tend to be younger
            age = random.randint(18, 45)
            sex = random.choice([Sex.MALE, Sex.FEMALE])
            
            # Migrants prefer economic centers or existing communities
            strategy = random.choice(["economic", "ethnic"])
            district_id = select_migration_district(self.districts, strategy)
            
            agent = MigrantAgent(self.next_agent_id, age, sex, district_id, self)
            self.next_agent_id += 1
            
            self.agents.append(agent)
            self.districts[district_id].add_agent(agent)
    
    def _generate_age_from_distribution(self):
        """Generate age from a realistic distribution."""
        # Simplified age distribution
        rand = random.random()
        if rand < 0.15:
            return random.randint(0, 14)
        elif rand < 0.25:
            return random.randint(15, 24)
        elif rand < 0.45:
            return random.randint(25, 44)
        elif rand < 0.65:
            return random.randint(45, 64)
        else:
            return random.randint(65, 90)
    
    def _select_district_weighted(self):
        """Select district weighted by economic attractiveness."""
        districts_list = list(self.districts.values())
        weights = [d.economic_attractiveness for d in districts_list]
        selected = random.choices(districts_list, weights=weights, k=1)[0]
        return selected.district_id
    
    def step(self):
        """Execute one time step (1 month) of the simulation."""
        self.tick += 1
        
        # Monthly processes
        self._process_immigration()
        self._process_social_interactions()
        self._process_media_exposure()
        
        # Annual processes (every 12 ticks)
        if self.tick % 12 == 0:
            self._process_annual_demographics()
        
        # Update district properties
        for district in self.districts.values():
            district.update_media_infrastructure()
        
        # Collect data
        self._collect_data()
    
    def _process_immigration(self):
        """Process monthly immigration of Brazilians."""
        annual_inflow = self.params.get("annual_br_inflow", 120)
        monthly_inflow = int(annual_inflow / 12)
        
        for _ in range(monthly_inflow):
            age = random.randint(18, 45)  # Working age migrants
            sex = random.choice([Sex.MALE, Sex.FEMALE])
            
            # Choose settlement location
            strategy = random.choice(["economic", "economic", "ethnic"])  # 2/3 economic
            district_id = select_migration_district(self.districts, strategy)
            
            agent = MigrantAgent(self.next_agent_id, age, sex, district_id, self)
            self.next_agent_id += 1
            
            self.agents.append(agent)
            self.districts[district_id].add_agent(agent)
    
    def _process_social_interactions(self):
        """Process social interactions within each district."""
        for district in self.districts.values():
            if len(district.agents) < 2:
                continue
            
            # School interactions (children and teens)
            students = district.get_agents_by_age_range(5, 18)
            for student in students:
                if not student.alive:
                    continue
                for _ in range(self.num_school_interactions):
                    if len(students) > 1:
                        other = random.choice([s for s in students if s != student and s.alive])
                        student.interact_linguistically(other, self.influence_rates)
            
            # Workplace interactions (working age)
            workers = district.get_agents_by_age_range(18, 67)
            for worker in workers:
                if not worker.alive:
                    continue
                for _ in range(self.num_workplace_interactions):
                    if len(workers) > 1:
                        other = random.choice([w for w in workers if w != worker and w.alive])
                        worker.interact_linguistically(other, self.influence_rates)
            
            # Market/public space interactions (random)
            for agent in district.agents:
                if not agent.alive:
                    continue
                if random.random() < self.prob_interaction_market:
                    if len(district.agents) > 1:
                        other = random.choice([a for a in district.agents if a != agent and a.alive])
                        agent.interact_linguistically(other, self.influence_rates)
    
    def _process_media_exposure(self):
        """Apply media influence to all agents."""
        base_media = self.params.get("base_media_influence", 0.5)
        
        for agent in self.agents:
            if not agent.alive:
                continue
            district = self.districts[agent.district_id]
            agent.apply_media_influence(base_media, district.media_infrastructure)
    
    def _process_annual_demographics(self):
        """Process annual demographic changes: aging, births, deaths."""
        # Aging
        for agent in self.agents:
            if agent.alive:
                agent.age_one_year()
        
        # Deaths
        agents_to_remove = []
        for agent in self.agents:
            if agent.alive and agent.check_mortality(self.death_rates):
                self.districts[agent.district_id].remove_agent(agent)
                agents_to_remove.append(agent)
        
        for agent in agents_to_remove:
            self.agents.remove(agent)
        
        # Births
        self._process_births()
    
    def _process_births(self):
        """Process births for fertile women."""
        fertile_age_min = 18
        fertile_age_max = 45
        
        for agent in self.agents:
            if not agent.alive:
                continue
            
            if agent.sex == Sex.FEMALE and fertile_age_min <= agent.age < fertile_age_max:
                # Determine birth rate based on agent type
                if isinstance(agent, LocalAgent):
                    birth_rate = self.birth_rate_locals
                else:
                    birth_rate = self.birth_rate_migrants
                
                if random.random() < birth_rate:
                    # Create a child
                    child_sex = random.choice([Sex.MALE, Sex.FEMALE])
                    
                    if isinstance(agent, LocalAgent):
                        child = LocalAgent(self.next_agent_id, 0, child_sex, agent.district_id, self)
                    else:
                        child = MigrantAgent(self.next_agent_id, 0, child_sex, agent.district_id, self)
                    
                    # Inherit linguistic features from mother
                    child.inherit_features_from_parent(agent)
                    
                    self.next_agent_id += 1
                    self.agents.append(child)
                    self.districts[agent.district_id].add_agent(child)
    
    def _collect_data(self):
        """Collect data for analysis."""
        locals_list = [a for a in self.agents if isinstance(a, LocalAgent) and a.alive]
        migrants_list = [a for a in self.agents if isinstance(a, MigrantAgent) and a.alive]
        
        self.data_collector["tick"].append(self.tick)
        self.data_collector["total_locals"].append(len(locals_list))
        self.data_collector["total_migrants"].append(len(migrants_list))
        
        # Mean linguistic features for locals
        if locals_list:
            self.data_collector["mean_local_vocab"].append(
                sum(a.brazilian_vocab for a in locals_list) / len(locals_list))
            self.data_collector["mean_local_grammar"].append(
                sum(a.brazilian_grammar for a in locals_list) / len(locals_list))
            self.data_collector["mean_local_phonetics"].append(
                sum(a.brazilian_phonetics for a in locals_list) / len(locals_list))
            self.data_collector["mean_local_pronouns"].append(
                sum(a.brazilian_pronouns for a in locals_list) / len(locals_list))
        else:
            self.data_collector["mean_local_vocab"].append(0)
            self.data_collector["mean_local_grammar"].append(0)
            self.data_collector["mean_local_phonetics"].append(0)
            self.data_collector["mean_local_pronouns"].append(0)
        
        # Mean linguistic features for migrants
        if migrants_list:
            self.data_collector["mean_migrant_vocab"].append(
                sum(a.brazilian_vocab for a in migrants_list) / len(migrants_list))
            self.data_collector["mean_migrant_grammar"].append(
                sum(a.brazilian_grammar for a in migrants_list) / len(migrants_list))
            self.data_collector["mean_migrant_phonetics"].append(
                sum(a.brazilian_phonetics for a in migrants_list) / len(migrants_list))
            self.data_collector["mean_migrant_pronouns"].append(
                sum(a.brazilian_pronouns for a in migrants_list) / len(migrants_list))
        else:
            self.data_collector["mean_migrant_vocab"].append(0)
            self.data_collector["mean_migrant_grammar"].append(0)
            self.data_collector["mean_migrant_phonetics"].append(0)
            self.data_collector["mean_migrant_pronouns"].append(0)
    
    def run(self, num_steps):
        """
        Run the simulation for a specified number of steps.
        
        Args:
            num_steps: Number of months to simulate
        """
        print(f"Running simulation for {num_steps} months ({num_steps/12:.1f} years)...")
        
        for step in range(num_steps):
            self.step()
            
            # Print progress every year
            if (step + 1) % 12 == 0:
                year = (step + 1) // 12
                num_locals = len([a for a in self.agents if isinstance(a, LocalAgent) and a.alive])
                num_migrants = len([a for a in self.agents if isinstance(a, MigrantAgent) and a.alive])
                print(f"Year {year}: {num_locals} locals, {num_migrants} migrants")
        
        print("Simulation complete!")
    
    def get_results(self):
        """Return collected data as a dictionary."""
        return self.data_collector
