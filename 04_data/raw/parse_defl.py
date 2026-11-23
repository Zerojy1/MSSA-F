import pandas as pd, numpy as np, sys
x=pd.ExcelFile(sys.argv[1])
out=[]
for s,val in [('中心点弯沉-行车道','D0_0.01mm'),('弯沉盆面积-行车道','basin_area_mm2')]:
    d=pd.read_excel(x,s,header=None)
    body=d.iloc[3:].reset_index(drop=True)
    body[0]=body[0].ffill()
    recs=[]
    for k in range(19):
        c=5+3*k
        t=pd.DataFrame({'Year':body[0],'Loading_Date':body[1],'Cycle_ID':body[2],'Cum_Load_10k':pd.to_numeric(body[3],errors='coerce'),
            'FWD_Load_kN':pd.to_numeric(body[4],errors='coerce'),'STR':f'STR{k+1}',
            'T_surface_C':pd.to_numeric(body[c],errors='coerce'),'T_air_C':pd.to_numeric(body[c+1],errors='coerce'),val:pd.to_numeric(body[c+2],errors='coerce')})
        recs.append(t)
    out.append(pd.concat(recs))
a,b=out
key=['Year','Loading_Date','Cycle_ID','Cum_Load_10k','FWD_Load_kN','STR']
a['row']=a.groupby('STR').cumcount(); b['row']=b.groupby('STR').cumcount()
m=a.merge(b[['STR','row','basin_area_mm2','T_surface_C','T_air_C']],on=['STR','row'],suffixes=('','_b'))
print('temp mismatch:',((m.T_surface_C-m.T_surface_C_b).abs()>1e-6).sum(),((m.T_air_C-m.T_air_C_b).abs()>1e-6).sum())
m=m.drop(columns=['T_surface_C_b','T_air_C_b'])
m.to_csv('defl/deflection_long.csv',index=False,encoding='utf-8-sig')
print(m.shape); print(m.FWD_Load_kN.value_counts(dropna=False))
per=a[a.STR=='STR1']
print('rows per STR',len(per),'nonnull D0',per['D0_0.01mm'].notna().sum())
print('cycle ids sample',per.Cycle_ID.dropna().unique()[:10],'...',per.Cycle_ID.dropna().unique()[-10:])
print('n unique cycle',per.Cycle_ID.nunique(), 'unique cum load',per.Cum_Load_10k.nunique())
print(per[['Year','Loading_Date','Cycle_ID','Cum_Load_10k','FWD_Load_kN']].iloc[[0,1,50,100,200,300,400,-3,-2,-1]].to_string())
print('missing D0 by STR', a.groupby('STR')['D0_0.01mm'].apply(lambda s:s.isna().sum()).to_dict())
print(m.describe().T[['count','mean','min','max']])
