import pandas as pd

mm = pd.read_csv("results/table/mutation_matrix.csv", index_col=0)

gene_count=mm.sum().sort_values(ascending=False).head(10)
import matplotlib.pyplot as plt
gene_count.plot(kind="bar")
plt.title("Top Mutated Genes")
plt.xlabel("Gene")
plt.ylabel("Mutation Count")



#Save results
plt.savefig("results/plots/top_mutated_gene.png",dpi=300,bbox_inches="tight")
plt.show()
