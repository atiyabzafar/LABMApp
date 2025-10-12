"""
District management for the Portuguese migration simulation.
Handles spatial distribution and district-level properties.
"""

import random


class District:
    """Represents a Portuguese administrative district."""
    
    def __init__(self, district_id, name, is_urban=False):
        """
        Initialize a district.
        
        Args:
            district_id: Unique identifier for the district
            name: Name of the district
            is_urban: Whether this is an urban district
        """
        self.district_id = district_id
        self.name = name
        self.is_urban = is_urban
        
        # Population counters
        self.num_locals = 0
        self.num_migrants = 0
        
        # Economic attractiveness (0-100 scale)
        self.economic_attractiveness = random.uniform(40, 90) if is_urban else random.uniform(20, 60)
        
        # Media infrastructure (urban: 80-95, rural: 35-55)
        if is_urban:
            self.media_infrastructure = random.uniform(80, 95)
        else:
            self.media_infrastructure = random.uniform(35, 55)
        
        # Lists to track agents in this district
        self.agents = []
    
    def add_agent(self, agent):
        """Add an agent to this district."""
        self.agents.append(agent)
        if agent.__class__.__name__ == "LocalAgent":
            self.num_locals += 1
        else:
            self.num_migrants += 1
    
    def remove_agent(self, agent):
        """Remove an agent from this district."""
        if agent in self.agents:
            self.agents.remove(agent)
            if agent.__class__.__name__ == "LocalAgent":
                self.num_locals -= 1
            else:
                self.num_migrants -= 1
    
    def get_brazilian_speaker_density(self):
        """
        Calculate the density of Brazilian Portuguese speakers.
        
        Returns:
            Proportion of migrants in the district (0-1)
        """
        total = self.num_locals + self.num_migrants
        if total == 0:
            return 0
        return self.num_migrants / total
    
    def update_media_infrastructure(self):
        """Update media infrastructure (can change monthly)."""
        # Small random walk
        change = random.uniform(-2, 2)
        self.media_infrastructure = max(0, min(100, self.media_infrastructure + change))
    
    def get_agents_by_type(self, agent_type):
        """
        Get all agents of a specific type in this district.
        
        Args:
            agent_type: Class name ("LocalAgent" or "MigrantAgent")
        
        Returns:
            List of agents of the specified type
        """
        return [agent for agent in self.agents if agent.__class__.__name__ == agent_type]
    
    def get_agents_by_age_range(self, min_age, max_age):
        """
        Get agents within a specific age range.
        
        Args:
            min_age: Minimum age (inclusive)
            max_age: Maximum age (exclusive)
        
        Returns:
            List of agents in the age range
        """
        return [agent for agent in self.agents if min_age <= agent.age < max_age]


def create_portugal_districts():
    """
    Create a simplified representation of Portuguese districts.
    
    Returns:
        Dictionary mapping district IDs to District objects
    """
    # Simplified list of Portuguese districts
    # In reality, Portugal has 18 districts + 2 autonomous regions
    districts_data = [
        (1, "Lisboa", True),
        (2, "Porto", True),
        (3, "Braga", True),
        (4, "Setúbal", True),
        (5, "Aveiro", False),
        (6, "Coimbra", False),
        (7, "Faro", True),
        (8, "Leiria", False),
        (9, "Santarém", False),
        (10, "Viseu", False),
        (11, "Viana do Castelo", False),
        (12, "Vila Real", False),
        (13, "Bragança", False),
        (14, "Guarda", False),
        (15, "Castelo Branco", False),
        (16, "Portalegre", False),
        (17, "Évora", False),
        (18, "Beja", False),
    ]
    
    districts = {}
    for district_id, name, is_urban in districts_data:
        districts[district_id] = District(district_id, name, is_urban)
    
    return districts


def select_migration_district(districts, strategy="economic"):
    """
    Select a district for a new migrant to settle in.
    
    Args:
        districts: Dictionary of District objects
        strategy: Selection strategy ("economic" or "ethnic")
    
    Returns:
        District ID where migrant will settle
    """
    if strategy == "economic":
        # Choose from top 5 economically attractive districts
        sorted_districts = sorted(districts.values(), 
                                 key=lambda d: d.economic_attractiveness, 
                                 reverse=True)
        top_5 = sorted_districts[:5]
        return random.choice(top_5).district_id
    
    elif strategy == "ethnic":
        # Choose district with high Brazilian speaker density
        sorted_districts = sorted(districts.values(), 
                                 key=lambda d: d.get_brazilian_speaker_density(), 
                                 reverse=True)
        # Choose from top districts with existing Brazilian community
        candidates = [d for d in sorted_districts[:5] if d.num_migrants > 0]
        if candidates:
            return random.choice(candidates).district_id
        else:
            # Fall back to economic strategy if no Brazilian communities exist
            return select_migration_district(districts, "economic")
    
    else:
        # Random selection
        return random.choice(list(districts.keys()))
