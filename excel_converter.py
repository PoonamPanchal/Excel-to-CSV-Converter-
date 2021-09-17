import glob, os
import pandas as pd
for file in glob.glob("*.xlsx"):
    df=pd.read_excel(file)
    df.to_csv(os.path.splitext(file)[0]+'.csv',index=None)