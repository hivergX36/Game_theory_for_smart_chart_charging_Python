from  Agent_class_aggregator import aggregator
from Agent_class_player import player
from Abstract_player_modelling import Player_abstract_model

# Sample data for players, prices, and revenues
data = {
    None:{
    'players': ['P1', 'P2','P3'],  # List of players
    'price': {'P1': 10, 'P2': 15, 'P3': 20},  # Prices for each player
    'revenue': {  # Revenue for each player
        'P1': 100,
        'P2': 120,
        'P3': 140,
    }
    }
    
}

# Create and run the model
player_model = Player_abstract_model()
player_model.run_model(data)