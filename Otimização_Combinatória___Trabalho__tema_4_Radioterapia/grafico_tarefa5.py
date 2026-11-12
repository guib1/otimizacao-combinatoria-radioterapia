from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# Dados dos relatórios do LINDO, arredondados a seis casas decimais.
# Primeiro trecho: Z = 5.50 - 0.40 * (limite - 20).
# Seus extremos são 20 - 6.071429 e 20 + 1.346154.
# A execução com limite 26 fornece Z = 4.444444.
# Seu Allowable Decrease é 4.653846: 26 - 4.653846 = 21.346154.
limites_pulmao = [13.928571, 21.346154, 26.0]
doses_sadio = [7.928571, 4.961538, 4.444444]

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(x=limites_pulmao, y=doses_sadio, marker="o", linewidth=2, ax=ax)
ax.set(
    title="Dose ótima no tecido sadio e limite pulmonar",
    xlabel="Limite de dose média no pulmão (Gy)",
    ylabel="Dose média mínima no tecido sadio (Gy)",
    xlim=(13.7, 26.3),
)
fig.tight_layout()
saida = Path(__file__).with_name("grafico_tarefa5.png")
fig.savefig(saida, dpi=300)
plt.close(fig)
print(f"Gráfico salvo em: {saida}")
