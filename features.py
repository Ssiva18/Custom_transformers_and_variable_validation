import pandas as pd
import numpy as np
import os
from sklearn.base import BaseEstimator,TransformerMixin
from typing import List,Dict,str


class RareLabelTransformer(BaseEstimator,TransformerMixin):

    def __init__(self,variables: List[str]):
        self.variables = variables

    def fit(self,X:pd.DataFrame,y: pd.Series =None) -> pd.DataFrame:
        Tmp = X.copy()
        self.Dictionary = {}
        for col_ in self.variables:
            values_counts_ = Tmp[col_].value_counts()
            values_ = values_counts_[values_counts_ < 0.10 ]
            self.Dictionary[col_] = values_

        return self
    
    def transform(self,X: pd.DataFrame) -> pd.DataFrame:
        
        """loop over the variables and apply 
           the transformation in particular"""
        
        Tmp = X.copy()

        for columns_ in self.variables:
            Tmp[columns_] = np.where(Tmp[columns_].isin(self.Dictionary[columns_]),'Rare',Tmp[columns_])

        return Tmp