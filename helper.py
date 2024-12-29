import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores, elapsed_time=None):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    
    # Title showing elapsed time
    if elapsed_time is not None:
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        plt.title(f"Training... Elapsed Time: {minutes}m {seconds}s")
    else:
        plt.title("Training...")
    
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)

    if len(scores) > 0:
        plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    if len(mean_scores) > 0:
        plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.pause(0.001)
