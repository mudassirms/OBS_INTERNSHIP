import matplotlib.pyplot as plt


def plot_votes(candidate_votes):
    candidates = list(candidate_votes.keys())
    votes = list(candidate_votes.values())

    plt.figure(figsize=(8, 5))
    plt.bar(candidates, votes, color=['blue', 'green', 'red', 'purple', 'orange'])

    plt.xlabel("Candidates")
    plt.ylabel("Votes")
    plt.title("Election Vote Count")
    plt.xticks(rotation=30)  

    for i, v in enumerate(votes):
        plt.text(i, v + 1, str(v), ha='center', fontsize=12)
        
    plt.show()
candidate_votes = {
    "Pooja": 250,
    "Khushi": 180,
    "Vein Diagram": 300,
    "Kunaal": 220,
    "mudassir": 150,
    "nagraj" : 189
}
plot_votes(candidate_votes)
