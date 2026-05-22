import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mm = pd.read_csv("results/table/mutation_matrix.csv",index_col=0)

top_gene=mm.sum().sort_values(ascending=False).head(10).index
sub_mm=mm[top_gene]
co_matrix=sub_mm.T.dot(sub_mm)
plt.figure(figsize=(8,6))
sns.heatmap(co_matrix,annot=True,cmap="Reds")
plt.title("Gene_Cooccurrance_heatmap")


#Save results
plt.savefig("results/plots/Gene_Cooccurrance_heatmap.png",dpi=300,bbox_inches="tight")
plt.show()