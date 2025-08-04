import pandas as pd

class DataCleaning:
    
    def __init__(self, data: pd.DataFrame) -> None:
        pass
    
    def _removing_punctuation_marks(self) -> None:
        pass
    
    def _convert_to_lowercase(self) -> None:
        pass
    
    def _removing_uncategorized_tweets(self) -> None:
        pass
    
    def activation(self) -> pd.DataFrame:
        self._removing_uncategorized_tweets()
        self._removing_punctuation_marks()
        self._convert_to_lowercase()