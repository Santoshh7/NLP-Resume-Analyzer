import matplotlib.pyplot as plt

def plot_scores(df):
    plt.figure(figsize=(10, 6))
    plt.barh(df['name'], df['final_score'], color='skyblue')
    plt.xlabel('Final Score')
    plt.title('Resume Match Score')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
