import pandas as pd

mm = pd.read_csv("results/table/mutation_matrix.csv", index_col=0)

import matplotlib.pyplot as plt
import seaborn as sns
subset=mm.iloc[:50,:20]
plt.figure(figsize=(10,5))
sns.heatmap(subset,cmap="coolwarm")
plt.title("Mutated_gene_heatmap")


#Save results
plt.savefig("results/plots/mutated_genes_heatmap.png",dpi=300,bbox_inches="tight")
plt.show()
