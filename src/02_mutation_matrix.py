import pandas as pd

df = pd.read_csv("data/raw/data_mutations.txt", sep="\t", comment="#")

mm=pd.crosstab(df["Tumor_Sample_Barcode"],df["Hugo_Symbol"])
mm=mm.map(lambda x:1 if x>0 else 0) #slower for larger data so
mm=(mm>0).astype(int)
mutation_count=mm.sum(axis=0)  # to get the column wise total (genes0)
mutation_count.sort_values(ascending=False).head()
mm.shape
mm.head()
exi=mm.sum(axis=1) # row wise total, count mhow many muttion in sample
exi.sort_values(ascending=False).head()

# Save result
mm.to_csv("results/table/mutation_matrix.csv")