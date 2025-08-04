import pandas as pd

class DataCleaning:
    
    def __init__(self, data: pd.DataFrame, relevant_columns:list) -> None:
        self.data:pd.DataFrame = data
        self.relevant_columns = relevant_columns
    
    def _removing_punctuation_marks(self) -> None:
        """
        Goes through the data frame and removes all punctuation marks
        """
        self.data.Text.replace(to_replace=".",  value="",inplace=True)
    
    def _convert_to_lowercase(self) -> None:
        """
        Goes through the data frame and converts everything to lowercase
        """
        self.data.Text = self.data.Text.str.lower()
    
    def _removing_uncategorized_tweets(self) -> None:
        """
        Goes through the data frame and removes irrelevant positions (everything except what is defined in the class)
        """
        self.data = self.data[self.relevant_columns]
    
    def activation(self) -> pd.DataFrame:
        """ 
        Runs all cleaning functions and returns the cleaned data. 
        """
        self._removing_uncategorized_tweets()
        self._removing_punctuation_marks()
        self._convert_to_lowercase()
        return self.data