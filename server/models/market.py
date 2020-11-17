class Market:
    
    def __init__(self, runners = None):
        self.runners = runners if runners else []
    
    @property
    def favourite(self):
        return max(self.runners, key=lambda runner: runner.odds.as_probability())
        
    @property
    def overround(self):
        return sum(runner.odds.as_probability() * 100 for runner in self.runners)    
        
    def add_runner(self, runner):
        self.runners.append(runner)