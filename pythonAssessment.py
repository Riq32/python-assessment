import re
from collections import Counter

def count_specific_word(text: str, search_word: str) -> int:
    """
    Counts the number of occurrences of a specific word in the text.
    Case-insensitive and ignores surrounding punctuation.
    """
    if not text or not search_word:
        return 0
    
    # Find all words matching the target word, ignoring case and punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(search_word.lower())


def identify_most_common_word(text: str) -> str:
    """
    Identifies the most common word in the text.
    Returns None if the text is empty.
    """
    if not text.strip():
        return None
    
    # Extract all words, lowercase them to ensure accurate counting
    words = re.findall(r'\b\w+\b', text.lower())
    
    if not words:
        return None
    
    word_counts = Counter(words)
    # most_common(1) returns a list of tuples: [('word', count)]
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text: str) -> float:
    """
    Calculates the average length of words in the text,
    excluding punctuation marks and special characters.
    """
    if not text.strip():
        return 0.0
    
    # Extract only alphanumeric words (excludes punctuation)
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def count_paragraphs(text: str) -> int:
    """
    Counts the number of paragraphs based on empty lines between blocks of text.
    An empty string returns 1.
    """
    if not text.strip():
        return 1
    
    # Split by two or more newlines to identify paragraph breaks
    paragraphs = [p for p in re.split(r'\n\s*\n', text) if p.strip()]
    return len(paragraphs)


def count_sentences(text: str) -> int:
    """
    Counts the number of sentences based on terminal punctuation (. ! ?)
    An empty string returns 1.
    """
    if not text.strip():
        return 1
    
    # Find all occurrences of terminal punctuation marks
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    
    # Fallback case: if text exists but has no terminal punctuation, count it as 1 sentence
    return max(1, len(sentences))


# --- Main Execution Block ---
if __name__ == "__main__":
    # Sample News Article Content (Replace this string with the exact content from your link)
    news_article = """
    In a major breakthrough for natural language processing, researchers have developed 
    more efficient algorithms. These tools allow startups to analyze data faster than ever.
    
    The industry is shifting quickly. Will your company adapt to these changes? 
    Only time will tell!
    """
    
    # Target word to search for
    target_word = "analyze"
    
    print("=" * 40)
    print(" NLP TEXT ANALYSIS REPORT ")
    print("=" * 40)
    
    # 1. Count specific word
    spec_count = count_specific_word(news_article, target_word)
    print(f"Occurrences of the word '{target_word}': {spec_count}")
    
    # 2. Identify most common word
    common_word = identify_most_common_word(news_article)
    print(f"Most common word: '{common_word}'")
    
    # 3. Calculate average word length
    avg_length = calculate_average_word_length(news_article)
    print(f"Average word length: {avg_length:.2f} characters")
    
    # 4. Count paragraphs
    paragraph_count = count_paragraphs(news_article)
    print(f"Total paragraphs: {paragraph_count}")
    
    # 5. Count sentences
    sentence_count = count_sentences(news_article)
    print(f"Total sentences: {sentence_count}")
    
    print("=" * 40)