import re
from collections import Counter


# ---------------------------------------------------------------------------
# Article text
# ---------------------------------------------------------------------------

ARTICLE = """ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the "Apple Pie Master," this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. "This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results," Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, "The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one."

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. "We want to cater to all taste preferences, from the traditional to the adventurous," said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master's environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. "Sustainability is at the core of all our product designs," emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, "It's like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings."

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. "The Apple Pie Master is just the beginning," said CEO Jane Doe. "We're exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking."

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations."""

# ---------------------------------------------------------------------------

# Functions
def count_specific_word(text: str, word: str) -> int:
    if not text or not word:
        return 0

    # Extract all words, stripping punctuation, then compare lower-case
    words = re.findall(r"[a-zA-Z']+", text.lower())
    target = word.lower().strip()
    return words.count(target)


def identify_most_common_word(text: str) -> str | None:
    if not text or not text.strip():
        return None

    words = re.findall(r"[a-zA-Z']+", text.lower())
    if not words:
        return None

    most_common_word, _ = Counter(words).most_common(1)[0]
    return most_common_word


def calculate_average_word_length(text: str) -> float:
    if not text or not text.strip():
        return 0.0

    # Keep only alphabetic characters within each word token
    words = re.findall(r"[a-zA-Z]+", text)
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)


def count_paragraphs(text: str) -> int:
    if not text or not text.strip():
        return 1

    # Split on one or more blank lines; filter out empty segments
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    return len(paragraphs)


def count_sentences(text: str) -> int:
    if not text or not text.strip():
        return 1

    # Split on sentence-ending punctuation
    segments = re.split(r"[.!?]+", text.strip())
    sentences = [s for s in segments if s.strip()]
    return len(sentences)



# Main — run analysis and display results
def main():
    search_word = "apple"

    print("=" * 60)
    print("        NEWS ARTICLE TEXT ANALYSIS REPORT")
    print("=" * 60)

    # 1. Count specific word
    word_count = count_specific_word(ARTICLE, search_word)
    print(f"\n1. Occurrences of the word '{search_word}': {word_count}")

    # 2. Most common word
    most_common = identify_most_common_word(ARTICLE)
    print(f"\n2. Most common word: '{most_common}'")

    # 3. Average word length
    avg_length = calculate_average_word_length(ARTICLE)
    print(f"\n3. Average word length: {avg_length} characters")

    # 4. Number of paragraphs
    paragraph_count = count_paragraphs(ARTICLE)
    print(f"\n4. Number of paragraphs: {paragraph_count}")

    # 5. Number of sentences
    sentence_count = count_sentences(ARTICLE)
    print(f"\n5. Number of sentences: {sentence_count}")

    print("\n" + "=" * 60)
    print("                  END OF REPORT")
    print("=" * 60)


if __name__ == "__main__":
    main()