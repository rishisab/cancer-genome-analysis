import pandas as pd
from itertools import combinations

mm = pd.read_csv("results/table/mutation_matrix.csv", index_col=0)

pair_count={}
for sample,row in mm.iterrows():
	genes=row[row==1].index.tolist()
	for pair in combinations(genes,2):
		pair=tuple(sorted(pair))

		if pair in pair_count:
			pair_count[pair]+=1
		else:
			pair_count[pair]=1
#to print convert the tuple
pair_series=pd.Series(pair_count)
pair_series=pair_series.sort_values(ascending=False)

#Save results
pair_series.to_csv("results/table/pair_series.csv")

