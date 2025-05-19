#!/usr/bin/env python3
import sys, numpy as np, pandas as pd
if len(sys.argv)!=3: sys.exit("usage: gpu.py <in.csv> <out.csv>")
df=pd.read_csv(sys.argv[1])
bits=384*32
eta=(bits*df.iloc[:,0])/df.iloc[:,1]
pd.DataFrame({"scale":np.arange(len(eta))+1,"eta":eta}).to_csv(sys.argv[2],index=False)
