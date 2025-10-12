"""
Agent classes for the Brazilian Migration to Portugal ABM.
Defines Locals (Portuguese natives) and Migrants (Brazilian immigrants).
"""

import random
from enum import Enum


class Sex(Enum):
    """Biological sex of agents."""
    MALE = "male"
    FEMALE = "female"


class PersonAgent:
    """Base class for all person agents in the simulation."""
    
    def __init__(self, agent_id, age, sex, district_id, model):
        """
        Initialize a person agent.
        
        Args:
            agent_id: Unique identifier for the agent
            age: Age in years
            sex: Sex (male/female)
            district_id: ID of the district where agent lives
            model: Reference to the main model
        """
        self.agent_id = agent_id
        self.age = age
        self.sex = sex
        self.district_id = district_id
        self.model = model
        
        # Linguistic features (0-100 scale)
        self.brazilian_vocab = 0
        self.brazilian_grammar = 0
        self.brazilian_phonetics = 0
        self.brazilian_pronouns = 0
        
        # Social factors
        self.reveal_identity = False
        self.media_exposure = random.uniform(30, 80)
        self.interaction_frequency = random.uniform(0.5, 1.0)
        self.educated = random.random() < 0.5  # 50% educated by default
        
        # Years in Portugal
        self.years_in_portugal = 0
        
        # Track if agent is alive
        self.alive = True
    
    def age_one_year(self):
        """Increase age by one year."""
        self.age += 1
        self.years_in_portugal += 1
    
    def check_mortality(self, death_rate_by_age):
        """
        Check if agent dies based on age-dependent mortality.
        
        Args:
            death_rate_by_age: Dictionary mapping age ranges to death rates
        """
        # Find appropriate death rate for this age
        death_rate = 0.001  # Default very low rate
        for age_range, rate in death_rate_by_age.items():
            if age_range[0] <= self.age < age_range[1]:
                death_rate = rate
                break
        
        if random.random() < death_rate:
            self.alive = False
            return True
        return False
    
    def interact_linguistically(self, other_agent, influence_rates):
        """
        Linguistic interaction between two agents.
        
        Args:
            other_agent: Another PersonAgent to interact with
            influence_rates: Dictionary of influence rates for each feature
        """
        # Determine influence direction and strength
        if isinstance(self, MigrantAgent) and self.reveal_identity:
            # Revealing migrant influences local
            if isinstance(other_agent, LocalAgent):
                self._influence_features(other_agent, influence_rates, direction="migrant_to_local")
        
        if isinstance(other_agent, MigrantAgent) and other_agent.reveal_identity:
            # Revealing migrant influences local
            if isinstance(self, LocalAgent):
                other_agent._influence_features(self, influence_rates, direction="migrant_to_local")
        
        # Locals have small reverse effect on migrants
        if isinstance(self, LocalAgent) and isinstance(other_agent, MigrantAgent):
            self._influence_features(other_agent, influence_rates, direction="local_to_migrant")
    
    def _influence_features(self, target_agent, influence_rates, direction):
        """
        Apply linguistic influence from one agent to another.
        
        Args:
            target_agent: Agent being influenced
            influence_rates: Dictionary of influence rates
            direction: "migrant_to_local" or "local_to_migrant"
        """
        if direction == "migrant_to_local":
            # Migrants influence locals to adopt Brazilian features
            target_agent.brazilian_vocab = min(100, target_agent.brazilian_vocab + 
                                              influence_rates["vocab"] * self.interaction_frequency)
            target_agent.brazilian_grammar = min(100, target_agent.brazilian_grammar + 
                                                 influence_rates["grammar"] * self.interaction_frequency)
            target_agent.brazilian_phonetics = min(100, target_agent.brazilian_phonetics + 
                                                   influence_rates["phonetics"] * self.interaction_frequency)
            target_agent.brazilian_pronouns = min(100, target_agent.brazilian_pronouns + 
                                                 influence_rates["pronouns"] * self.interaction_frequency)
        
        elif direction == "local_to_migrant":
            # Locals have small reverse effect (reduce Brazilian features)
            reverse_rate = 0.1  # Much weaker effect
            target_agent.brazilian_vocab = max(0, target_agent.brazilian_vocab - 
                                              influence_rates["vocab"] * reverse_rate * self.interaction_frequency)
            target_agent.brazilian_grammar = max(0, target_agent.brazilian_grammar - 
                                                 influence_rates["grammar"] * reverse_rate * self.interaction_frequency)
            target_agent.brazilian_phonetics = max(0, target_agent.brazilian_phonetics - 
                                                   influence_rates["phonetics"] * reverse_rate * self.interaction_frequency)
            target_agent.brazilian_pronouns = max(0, target_agent.brazilian_pronouns - 
                                                 influence_rates["pronouns"] * reverse_rate * self.interaction_frequency)
    
    def apply_media_influence(self, base_media_influence, district_media_infrastructure):
        """
        Apply media exposure effects on linguistic features.
        
        Args:
            base_media_influence: Global media influence parameter
            district_media_infrastructure: Media infrastructure level in district (0-100)
        """
        # Media influence is strongest on vocabulary, weaker on other features
        total_media = (self.media_exposure / 100) * (district_media_infrastructure / 100) * base_media_influence
        
        # Apply differential effects
        vocab_effect = total_media * 0.05  # Strongest
        grammar_effect = total_media * 0.03
        pronoun_effect = total_media * 0.02
        phonetics_effect = total_media * 0.01  # Weakest
        
        if isinstance(self, LocalAgent):
            # Media increases Brazilian features for locals
            self.brazilian_vocab = min(100, self.brazilian_vocab + vocab_effect)
            self.brazilian_grammar = min(100, self.brazilian_grammar + grammar_effect)
            self.brazilian_pronouns = min(100, self.brazilian_pronouns + pronoun_effect)
            self.brazilian_phonetics = min(100, self.brazilian_phonetics + phonetics_effect)
    
    def inherit_features_from_parent(self, parent):
        """
        Inherit linguistic features from parent (mother tongue effect).
        
        Args:
            parent: Parent agent to inherit from
        """
        # Children inherit with some variation
        variation = 5
        self.brazilian_vocab = max(0, min(100, parent.brazilian_vocab + random.uniform(-variation, variation)))
        self.brazilian_grammar = max(0, min(100, parent.brazilian_grammar + random.uniform(-variation, variation)))
        self.brazilian_phonetics = max(0, min(100, parent.brazilian_phonetics + random.uniform(-variation, variation)))
        self.brazilian_pronouns = max(0, min(100, parent.brazilian_pronouns + random.uniform(-variation, variation)))


class LocalAgent(PersonAgent):
    """Agent representing a native Portuguese person."""
    
    def __init__(self, agent_id, age, sex, district_id, model):
        super().__init__(agent_id, age, sex, district_id, model)
        
        # Locals start with low Brazilian Portuguese features
        self.brazilian_vocab = random.uniform(5, 10)  # 5-10%
        self.brazilian_grammar = random.uniform(2, 5)  # 2-5%
        self.brazilian_phonetics = random.uniform(1, 3)  # 1-3%
        self.brazilian_pronouns = random.uniform(8, 15)  # 8-15%
        
        # Years in Portugal = age (born here)
        self.years_in_portugal = age
        
        # Reveal identity based on model parameter
        self.reveal_identity = random.random() < model.params["reveal_share_locals"]


class MigrantAgent(PersonAgent):
    """Agent representing a Brazilian immigrant."""
    
    def __init__(self, agent_id, age, sex, district_id, model):
        super().__init__(agent_id, age, sex, district_id, model)
        
        # Migrants start with high Brazilian Portuguese features
        self.brazilian_vocab = random.uniform(95, 100)  # 95-100%
        self.brazilian_grammar = random.uniform(90, 100)  # 90-100%
        self.brazilian_phonetics = random.uniform(85, 100)  # 85-100%
        self.brazilian_pronouns = random.uniform(80, 100)  # 80-100%
        
        # Just arrived
        self.years_in_portugal = 0
        
        # Reveal identity based on model parameter
        self.reveal_identity = random.random() < model.params["reveal_share_migrants"]
