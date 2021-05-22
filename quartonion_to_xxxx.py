# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:50:54 2021

Due to privacy and security reasons full code is not updated yet 

@author: avanish @ VirTex from CMMMG
"""

import pandas as pd
import numpy as np

def QuartToRotation(df):
    df['norm']=np.linalg.norm(df[['orientationx', 'orientationy', 'orientationz','orientationw']].values,axis=1)
    
    df['norm']=df['norm']+0.000001
     
    df['x2'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationx']/df['norm'])
    df['y2'] = 2.0 * (df['orientationy']/df['norm']) * (df['orientationy']/df['norm'])
    df['z2'] = 2.0 * (df['orientationz']/df['norm']) * (df['orientationz']/df['norm'])
     
    df['xy'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationy']/df['norm'])
    df['xz'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationz']/df['norm'])
    df['yz'] = 2.0 * (df['orientationy']/df['norm']) * (df['orientationz']/df['norm'])
     
    df['xw'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationw']/df['norm'])
    df['yw'] = 2.0 * (df['orientationy']/df['norm']) * (df['orientationw']/df['norm'])
    df['zw'] = 2.0 * (df['orientationz']/df['norm']) * (df['orientationw']/df['norm'])
   
    return(df)
