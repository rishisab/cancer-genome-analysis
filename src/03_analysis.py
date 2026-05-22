import pandas as pd

mm = pd.read_csv("results/table/mutation_matrix.csv", index_col=0)

mutation_count = mm.sum().sort_values(ascending=False)

print(mutation_count.head(10))

# Save
mutation_count.to_csv("results/table/top_genes.csv")
