import pandas as pd
import numpy as np

mm = pd.read_csv("results/table/mutation_matrix.csv", index_col=0)

top_gene = mm.sum().sort_values(ascending=False).head(10).index
sub_mm = mm[top_gene]
co_matrix = sub_mm.T.dot(sub_mm)

# Mask the diagonal using pure Pandas 
co_matrix_no_diagonal = co_matrix.astype(float)
diagonal_mask = np.eye(len(co_matrix_no_diagonal), dtype=bool)
co_matrix_no_diagonal = co_matrix_no_diagonal.mask(diagonal_mask)

# Save results
co_matrix_no_diagonal.to_csv("results/table/co_matrix_no_diagonal.csv")
