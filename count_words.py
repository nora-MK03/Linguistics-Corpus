from pypdf import pdfreader
import re
from collection import counter
reader = pdfreader("case theory.pdf")
text = ""
for page in reader. pages:
    text += (page.extract_text() or "") + "\n"
    words = re.findall(r"\w+", text.lower ())
    freq = counter(words)
    print ("pages;", len(reader.pages))
    print("total words (tokens):", len(words))
    print("different words (types):", len(freq))
    print("top 15 words:")
    for word, count in freq.most_common(15):
        print(word, count)
        