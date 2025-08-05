import pandas as pd

class DataAnalyzer:
    
    def __init__(self, data: pd.DataFrame, antisemitic=1, non_antisemitic=0, classification_col_name="Biased")-> None:
        self.df_data:pd.DataFrame = data
        self.antisemitic = antisemitic
        self.non_antisemitic = non_antisemitic
        self.classification_col_name = classification_col_name
        self.df_antisemitic , self.df_non_antisemitic , self.df_unspecified = self.split_into_categories()
    
    def split_into_categories(self) -> tuple:
        """
        Divides the data frame into 4 parts: anti-Semitic - not anti-Semitic - other - and all
        The division is done by extracting the relevant parts from the entire data frame (using the equals and conditions)
        """
        return (
            self.df_data[self.df_data[self.classification_col_name] == self.antisemitic],
            self.df_data[self.df_data[self.classification_col_name] == self.non_antisemitic],
            self.df_data[
                (self.df_data[self.classification_col_name] != self.antisemitic)
                & 
                (self.df_data[self.classification_col_name] != self.non_antisemitic)],
        )
    
    def _average_word_length(self, df:pd.DataFrame) -> float:
        """
        Returns the origin of the word lengths of a data frame.
        Executed by a new Series containing a list of words,
        and iterates and calculates the length for each and the final average for that.
        """
        sum_df:pd.Series = df.Text.str.split()
        mean_length = sum_df.str.len().mean()
        return 0 if pd.isna(mean_length) else mean_length
    
    def _most_3_longest_tweets_text(self, df:pd.DataFrame) -> list:
        """
        Returns the 3 longest tweets.
        By creating a list containing the list of words - checking the length - and sorting by size and returning the first 3, 
        and from their index extracts the text and converts it to a list
        """
        most_3_longest_tweets = df.Text.str.len().sort_values(ascending=False).head(3)
        return self.df_data.iloc[most_3_longest_tweets.index].Text.to_list()

    def _most_10_common_words(self, df:pd.DataFrame) -> list:
        """
        Returns the 10 most common words.
        By combining all the text into one and converting it to a Series,
        and then counting the words and getting the 10 with the most and converting it to a List
        """
        return pd.Series(" ".join(df.Text).split()).value_counts().head(10).index.to_list()
    
    def _sum_uppercase_words(self, df:pd.DataFrame) -> int:
        """
        Returns the sum of the upper word count
        by combining all the text into one and converting it to a Series,
        and counting the words that are larger
        """
        return int(pd.Series(" ".join(df.Text).split()).str.isupper().sum())
    
    
    def sum_tweets(self) -> dict:
        """
        Returns the length of the data frame for each category.
        """
        return {
            "total_tweets":{
                "total":self.df_data.shape[0],
                "antisemitic":self.df_antisemitic.shape[0],
                "non_antisemitic":self.df_non_antisemitic.shape[0], 
                "unspecified":self.df_unspecified.shape[0]
            }
        }
            
    def average_word_length_by_category(self) -> dict:
        """
        Returns the _average_word_length for each category as a dictionary
        """
        return {
            "average_length":{
                "total": self._average_word_length(self.df_data), 
                "antisemitic": self._average_word_length(self.df_antisemitic),
                "non_antisemitic": self._average_word_length(self.df_non_antisemitic), 
                "unspecified": self._average_word_length(self.df_unspecified)
            }
        }

    def most_3_longest_tweets_text_by_category(self) -> dict:
        """
        Returns the _most_3_longest_tweets_text for each category as a dictionary
        """
        return {
            "longest_3_tweets":{
                "total": self._most_3_longest_tweets_text(self.df_data),
                "antisemitic": self._most_3_longest_tweets_text(self.df_antisemitic),
                "non_antisemitic": self._most_3_longest_tweets_text(self.df_non_antisemitic),
                "unspecified": self._most_3_longest_tweets_text(self.df_unspecified),
            }
        }
    
    def most_10_common_words_by_category(self) -> dict:
        """
        Returns the _most_10_common_words for each category as a dictionary
        """
        return {
            "common_words":{
                "total": self._most_10_common_words(self.df_data),
                "antisemitic": self._most_10_common_words(self.df_antisemitic),
                "non_antisemitic": self._most_10_common_words(self.df_non_antisemitic),
                "unspecified": self._most_10_common_words(self.df_unspecified),
            }
        }

    def sum_uppercase_words_by_category(self) -> dict:
        """
        Returns the _sum_uppercase_words for each category as a dictionary
        """
        return {
            "uppercase_words":{
                "total": self._sum_uppercase_words(self.df_data),
                "antisemitic": self._sum_uppercase_words(self.df_antisemitic),
                "non_antisemitic": self._sum_uppercase_words(self.df_non_antisemitic),
                "unspecified": self._sum_uppercase_words(self.df_unspecified),
            }
        }
