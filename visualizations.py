import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(data):
    charts = {}

    # Example: ROI by Channel
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x="channel", y="roi")
    plt.title("ROI by Marketing Channel")
    plt.savefig("static/roi_by_channel.png")
    charts["roi_by_channel"] = "static/roi_by_channel.png"

    return charts
