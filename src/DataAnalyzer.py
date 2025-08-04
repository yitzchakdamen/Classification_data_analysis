import pandas as pd

class DataAnalyzer:
    
    def __init__(self, data: pd.DataFrame, antisemitic=1, non_antisemitic=0, classification_col_name="Biased")-> None:
        self.df_data:pd.DataFrame = data
        self.antisemitic = antisemitic
        self.non_antisemitic = non_antisemitic
        self.classification_col_name = classification_col_name
        self.df_antisemitic , self.df_non_antisemitic , self.df_unspecified = self.split_into_categories()
    
    def split_into_categories(self) -> tuple:
        return (
            self.df_data[self.df_data[self.classification_col_name] == self.antisemitic],
            self.df_data[self.df_data[self.classification_col_name] == self.non_antisemitic],
            self.df_data[
                (self.df_data[self.classification_col_name] != self.antisemitic)
                & 
                (self.df_data[self.classification_col_name] != self.non_antisemitic)],
        )
    
    def _average_word_length(self, df:pd.DataFrame) -> float:
        sum_df:pd.Series = df.Text.str.split()
        return sum_df.str.len().mean()
    
    def _most_3_longest_tweets_text(self, df:pd.DataFrame) -> list:
        most_3_longest_tweets = df.Text.str.len().sort_values(ascending=False).head(3)
        return df.iloc[most_3_longest_tweets.index].Text.to_list()

    def _most_10_common_words(self, df:pd.DataFrame) -> list:
        return pd.Series(" ".join(df.Text).split()).value_counts().head(10).to_list()
    
    def _sum_uppercase_words(self, df:pd.DataFrame) -> int:
        return pd.Series(" ".join(df.Text).split()).str.isupper().sum()
    
    
    def sum_tweets(self) -> dict:
        return {
            "total_tweets":{
                "total":self.df_data.shape[0],
                "antisemitic":self.df_antisemitic.shape[0],
                "non_antisemitic":self.df_non_antisemitic.shape[0], 
                "unspecified":self.df_unspecified.shape[0]
            }
        }
            
    def average_word_length_by_category(self) -> dict:
        return {
            "average_length":{
                "total": self._average_word_length(self.df_data), 
                "antisemitic": self._average_word_length(self.df_antisemitic),
                "non_antisemitic": self._average_word_length(self.df_non_antisemitic), 
                "unspecified": self._average_word_length(self.df_unspecified)
            }
        }

    def most_3_longest_tweets_text_by_category(self) -> dict:
        return {
            "longest_3_tweets":{
                "total": self._most_3_longest_tweets_text(self.df_data),
                "antisemitic": self._most_3_longest_tweets_text(self.df_antisemitic),
                "non_antisemitic": self._most_3_longest_tweets_text(self.df_non_antisemitic),
                "unspecified": self._most_3_longest_tweets_text(self.df_unspecified),
            }
        }
    
    def most_10_common_words_by_category(self) -> dict:
        return {
            "common_words":{
                "total": self._most_10_common_words(self.df_data),
                "antisemitic": self._most_10_common_words(self.df_antisemitic),
                "non_antisemitic": self._most_10_common_words(self.df_non_antisemitic),
                "unspecified": self._most_10_common_words(self.df_unspecified),
            }
        }

    def sum_uppercase_words_by_category(self) -> dict:
        return {
            "uppercase_words":{
                "total": self._sum_uppercase_words(self.df_data),
                "antisemitic": self._sum_uppercase_words(self.df_antisemitic),
                "non_antisemitic": self._sum_uppercase_words(self.df_non_antisemitic),
                "unspecified": self._sum_uppercase_words(self.df_unspecified),
            }
        }
