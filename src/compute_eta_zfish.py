#!/usr/bin/env python3
import sys, numpy as np, pandas as pd
if len(sys.argv)!=3: sys.exit("usage: zfish.py <in.csv> <out.csv>")
df=pd.read_csv(sys.argv[1])
eta=df["Entropy_bits"]/df["Energy_J"]
pd.DataFrame({"scale":df["Window_min"],"eta":eta}).to_csv(sys.argv[2],index=False)
