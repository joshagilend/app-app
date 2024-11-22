from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipedia

def create_wordcloud(topic):
    """
    Creates a word cloud from the content of a Wikipedia page.
    :param topic: Topic to generate word cloud for
    """
    try:
        page_content = wikipedia.page(topic).content
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(page_content)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    topic = "Python programming language"
    create_wordcloud(topic)
