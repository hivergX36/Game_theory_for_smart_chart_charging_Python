class aggregator:
    
    """_summary_
    This class represents an aggregator in the smart charging system.
    This the pyomo abstract model of the aggregator 
    """
    
    def __init__(self) -> None:
        self.instance = {
             "a1x^2": 0,
            "b1x": 0,
            "c1": 0,
            "a2x^2": 0,
            "b2x": 0,
            "c2": 0,
        } 
  
        