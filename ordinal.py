import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from typing import List,Dict,str

class OrdinalEncoder(BaseEstimator,TransformerMixin):

    """ Considering list of elements are passed through the defined variable.
       Here we actually ordering the categorical labels based on the mean 
       value of reference varibale i.e., continuous variable  """
    
    def __init__(self,variables:List[str],referencevariable:str):
        self.variables = variables
        self.referencevariable = referencevariable

    def fit(self,X:pd.DataFrame,y:pd.Series = None):
        df = X.copy()
        self.Dictionary = {}
        for column in self.variables:
            self.grouped = df.groupby([column])[self.referencevariable].agg('mean').sort_values(ascending = True)
            self.Dictionary[column] = {enumerate_value:label for enumerate_value,label in enumerate(list(self.grouped.index))}
        return self
    
    def transform(self,X:pd.DataFrame)-> pd.DataFrame:
        df = X.copy()
        for column in self.variables:
            df[column] = df[column].map(self.Dictionary[column])

        return df


