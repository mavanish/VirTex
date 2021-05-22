# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:50:54 2021

@author: avani
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
 
    df['R11']= 1 - df['y2'] - df['z2']
    df['R12']= df['xy'] +  df['zw']
    df['R13']= df['xz'] -  df['yw']
    
    df['R21']= df['xy'] -  df['zw']
    df['R22']= 1 - df['x2'] - df['z2']
    df['R23']= df['yz'] +  df['xw']
    
    df['R31']= df['xz'] +  df['yw']
    df['R32']= df['yz'] -  df['xw']
    df['R33']= 1 - df['x2'] - df['y2']
    
    df['A11']=(np.arccos(df.R11)/0.0174533)
    df['A12']=(np.arccos(df.R12)/0.0174533)
    df['A13']=(np.arccos(df.R13)/0.0174533)
    
    df['A21']=(np.arccos(df.R21)/0.0174533)
    df['A22']=(np.arccos(df.R22)/0.0174533)
    df['A23']=(np.arccos(df.R23)/0.0174533)
    
    df['A31']=(np.arccos(df.R31)/0.0174533)
    df['A32']=(np.arccos(df.R32)/0.0174533)
    df['A33']=(np.arccos(df.R33)/0.0174533)

    df['theta']=np.arccos((df['R11']+df['R22']+df['R33']-1)/2)
    df['atheta']=np.rad2deg(df['theta'])

    df['r1']=(df['R23']-df['R32'])/(2*np.sin(df['theta']))
    df['r2']=(df['R31']-df['R13'])/(2*np.sin(df['theta']))
    df['r3']=(df['R12']-df['R21'])/(2*np.sin(df['theta']))
    
    # df['ntheta']=np.arccos(np.abs(df['R11']+df['R22']+df['R33']-1)/2)
    # df['natheta']=np.rad2deg(df['ntheta'])
    
    # df['ar1']=(df['R23']-df['R32'])/(2*np.sin(df['ntheta']))
    # df['ar2']=(df['R31']-df['R13'])/(2*np.sin(df['ntheta']))
    # df['ar3']=(df['R12']-df['R21'])/(2*np.sin(df['ntheta']))
    
   
    return(df)

def QuartToEuler(df):

    df['x2'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationx']/df['norm'])
    df['y2'] = 2.0 * (df['orientationy']/df['norm']) * (df['orientationy']/df['norm'])
    df['z2'] = 2.0 * (df['orientationz']/df['norm']) * (df['orientationz']/df['norm'])
     
    df['xy'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationy']/df['norm'])
    df['xz'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationz']/df['norm'])
    df['yz'] = 2.0 * (df['orientationy']/df['norm']) * (df['orientationz']/df['norm'])
     
    df['xw'] = 2.0 * (df['orientationx']/df['norm']) * (df['orientationw']/df['norm'])
    df['yw'] = 2.0 * (df['orientationy']/df['norm']) * (df['orientationw']/df['norm'])
    df['zw'] = 2.0 * (df['orientationz']/df['norm']) * (df['orientationw']/df['norm'])

    df['phi1']=np.arctan2((df['xw']+df['yz']), (1-(df['x2']+df['y2'])))
    df['cphi']=np.arcsin(df['yw']-df['xz'])
    df['phi2']=np.arctan2((df['zw']+df['xy']), (1-(df['y2']+df['z2'])))

    df['R11']=((np.cos(df['phi1'])*np.cos(df['phi2']))-(np.sin(df['phi1'])*np.sin(df['phi2'])*np.cos(df['cphi'])))
    df['R12']=((np.sin(df['phi1'])*np.cos(df['phi2']))+(np.cos(df['phi1'])*np.sin(df['phi2'])*np.cos(df['cphi'])))
    df['R13']=(np.sin(df['phi2'])*np.sin(df['cphi']))
    
    df['R21']=((-np.cos(df['phi1'])*np.sin(df['phi2']))-(np.sin(df['phi1'])*np.cos(df['phi2'])*np.cos(df['cphi'])))
    df['R22']=((-np.sin(df['phi1'])*np.sin(df['phi2']))+(np.cos(df['phi1'])*np.cos(df['phi2'])*np.cos(df['cphi'])))
    df['R23']=((np.cos(df['phi2']))*np.sin(df['cphi']))
    
    df['R31']=((np.sin(df['phi1']))*np.sin(df['cphi']))
    df['R32']=((-np.cos(df['phi1']))*np.sin(df['cphi']))
    df['R33']=(np.cos(df['cphi']))
    
    df['A11']=(np.arccos(df.R11)/0.0174533)
    df['A12']=(np.arccos(df.R12)/0.0174533)
    df['A13']=(np.arccos(df.R13)/0.0174533)
    
    df['A21']=(np.arccos(df.R21)/0.0174533)
    df['A22']=(np.arccos(df.R22)/0.0174533)
    df['A23']=(np.arccos(df.R23)/0.0174533)
    
    df['A31']=(np.arccos(df.R31)/0.0174533)
    df['A32']=(np.arccos(df.R32)/0.0174533)
    df['A33']=(np.arccos(df.R33)/0.0174533)

    df['theta']=np.arccos((df['R11']+df['R22']+df['R33']-1)/2)
    df['atheta']=np.rad2deg(df['theta'])

    df['r1']=(df['R23']-df['R32'])/(2*np.sin(df['theta']))
    df['r2']=(df['R31']-df['R13'])/(2*np.sin(df['theta']))
    df['r3']=(df['R12']-df['R21'])/(2*np.sin(df['theta']))
    
    df['ntheta']=np.arccos((np.abs(df['R11']+df['R22']+df['R33'])-1)/2)
    df['natheta']=np.rad2deg(df['ntheta'])
    
    df['ar1']=(df['R23']-df['R32'])/(2*np.sin(df['ntheta']))
    df['ar2']=(df['R31']-df['R13'])/(2*np.sin(df['ntheta']))
    df['ar3']=(df['R12']-df['R21'])/(2*np.sin(df['ntheta']))
    
    return(df)

use_df=qdf2.copy()
def RMissorientation(use_df,Go):
    inGo=np.linalg.inv(Go)
    
    use_df['C11']=inGo[0][0]*use_df['R11'] + inGo[0][1]*use_df['R21'] + inGo[0][2]*use_df['R31']
    use_df['C12']=inGo[0][0]*use_df['R12'] + inGo[0][1]*use_df['R22'] + inGo[0][2]*use_df['R32']
    use_df['C13']=inGo[0][0]*use_df['R13'] + inGo[0][1]*use_df['R23'] + inGo[0][2]*use_df['R33']
    
    use_df['C21']=inGo[1][0]*use_df['R11'] + inGo[1][1]*use_df['R21'] + inGo[1][2]*use_df['R31']
    use_df['C22']=inGo[1][0]*use_df['R12'] + inGo[1][1]*use_df['R22'] + inGo[1][2]*use_df['R32']
    use_df['C23']=inGo[1][0]*use_df['R13'] + inGo[1][1]*use_df['R23'] + inGo[1][2]*use_df['R33']
    
    use_df['C31']=inGo[2][0]*use_df['R11'] + inGo[2][1]*use_df['R21'] + inGo[2][2]*use_df['R31']
    use_df['C32']=inGo[2][0]*use_df['R12'] + inGo[2][1]*use_df['R22'] + inGo[2][2]*use_df['R32']
    use_df['C33']=inGo[2][0]*use_df['R13'] + inGo[2][1]*use_df['R23'] + inGo[2][2]*use_df['R33']
    
    use_df['Miss']=np.arccos((use_df['C11']+use_df['C22']+use_df['C33']-1)/2)
    use_df['RAMiss']=np.rad2deg(use_df['Miss'])
    
    use_df['oamis']=np.arccos(np.abs(use_df['C11']+use_df['C22']+use_df['C33']-1)/2)
    use_df['oAMiss']=np.rad2deg(use_df['oamis'])
    

    return(use_df) 
    
def Missorientation(use_df,Go):
    inGo=np.abs(np.linalg.inv(Go))
    
    use_df['C11']=inGo[0][0]*use_df['R11'].abs() + inGo[0][1]*use_df['R21'].abs() + inGo[0][2]*use_df['R31'].abs()
    use_df['C12']=inGo[0][0]*use_df['R12'].abs() + inGo[0][1]*use_df['R22'].abs() + inGo[0][2]*use_df['R32'].abs()
    use_df['C13']=inGo[0][0]*use_df['R13'].abs() + inGo[0][1]*use_df['R23'].abs() + inGo[0][2]*use_df['R33'].abs()
    
    use_df['C21']=inGo[1][0]*use_df['R11'].abs() + inGo[1][1]*use_df['R21'].abs() + inGo[1][2]*use_df['R31'].abs()
    use_df['C22']=inGo[1][0]*use_df['R12'].abs() + inGo[1][1]*use_df['R22'].abs() + inGo[1][2]*use_df['R32'].abs()
    use_df['C23']=inGo[1][0]*use_df['R13'].abs() + inGo[1][1]*use_df['R23'].abs() + inGo[1][2]*use_df['R33'].abs()
    
    use_df['C31']=inGo[2][0]*use_df['R11'].abs() + inGo[2][1]*use_df['R21'].abs() + inGo[2][2]*use_df['R31'].abs()
    use_df['C32']=inGo[2][0]*use_df['R12'].abs() + inGo[2][1]*use_df['R22'].abs() + inGo[2][2]*use_df['R32'].abs()
    use_df['C33']=inGo[2][0]*use_df['R13'].abs() + inGo[2][1]*use_df['R23'].abs() + inGo[2][2]*use_df['R33'].abs()
    
    use_df['amis']=np.arccos(np.abs(use_df['C11']+use_df['C22']+use_df['C33']-1)/2)
    use_df['AMiss']=np.rad2deg(use_df['amis'])
    
    return(use_df) 
