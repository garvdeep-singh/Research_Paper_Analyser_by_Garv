# import re
# import fitz
# from bertopic import BERTopic
# from umap import UMAP
# from sklearn.feature_extraction.text import CountVectorizer
# from bertopic.representation import KeyBERTInspired


# # ---------------- PDF TEXT ----------------
# def extract_text(file):
#     doc = fitz.open(stream=file.read(), filetype="pdf")
#     text = ""

#     for page in doc:
#         text += page.get_text()

#     return text


# # ---------------- ABSTRACT ----------------
# def extract_abstract(text):
#     text_lower = text.lower()

#     if "abstract" in text_lower:
#         start = text_lower.find("abstract")
#         end = text_lower.find("introduction")

#         if end == -1:
#             end = start + 1500

#         return text[start:end]

#     return text[:1500]


# # ---------------- PREPROCESS ----------------
# def preprocess_text(text):
#     text = text.lower()
#     text = text.split("references")[0]

#     text = re.sub(r'\d+', '', text)
#     text = re.sub(r'\W+', ' ', text)

#     words = text.split()

#     stop_words = {
#         "the", "and", "for", "with", "this", "that",
#         "from", "are", "was", "were", "have", "has",
#         "using", "based", "study", "paper", "research",
#         "university", "department", "journal", "published",
#         "article", "available", "received"
#     }

#     words = [w for w in words if len(w) > 3 and w not in stop_words]

#     return " ".join(words[:400])


# # ---------------- MODEL ----------------
# def build_model():

#     vectorizer_model = CountVectorizer(
#         ngram_range=(1, 2),
#         stop_words="english"
#     )

#     representation_model = KeyBERTInspired()

#     umap_model = UMAP(
#         n_neighbors=10,
#         n_components=5,
#         min_dist=0.0,
#         metric='cosine',
#         random_state=42
#     )

#     topic_model = BERTopic(
#         umap_model=umap_model,
#         vectorizer_model=vectorizer_model,
#         representation_model=representation_model,
#         min_topic_size=2,
#         nr_topics=5,
#         verbose=False
#     )

#     return topic_model














# import re
# import fitz
# from bertopic import BERTopic
# from umap import UMAP
# from sklearn.feature_extraction.text import CountVectorizer
# from bertopic.representation import KeyBERTInspired


# # ---------------- PDF TEXT ----------------
# def extract_text(file):
#     doc = fitz.open(stream=file.read(), filetype="pdf")
#     text = ""

#     for page in doc:
#         text += page.get_text()

#     return text


# # ---------------- ABSTRACT ----------------
# def extract_abstract(text):
#     text_lower = text.lower()

#     if "abstract" in text_lower:
#         start = text_lower.find("abstract")
#         end = text_lower.find("introduction")

#         if end == -1:
#             end = start + 1500

#         return text[start:end]

#     return text[:1500]


# # ---------------- PREPROCESS ----------------
# def preprocess_text(text):
#     text = text.lower()
#     text = text.split("references")[0]

#     text = re.sub(r'\d+', '', text)
#     text = re.sub(r'\W+', ' ', text)

#     words = text.split()

#     stop_words = {
#         "the", "and", "for", "with", "this", "that",
#         "from", "are", "was", "were", "have", "has",
#         "using", "based", "study", "paper", "research",
#         "university", "department", "journal", "published",
#         "article", "available", "received"
#     }

#     words = [w for w in words if len(w) > 3 and w not in stop_words]

#     return " ".join(words[:400])


# # ---------------- MODEL ----------------
# def build_model():

#     vectorizer_model = CountVectorizer(
#         ngram_range=(1, 2),
#         stop_words="english"
#     )

#     representation_model = KeyBERTInspired()

#     umap_model = UMAP(
#         n_neighbors=10,
#         n_components=5,
#         min_dist=0.0,
#         metric='cosine',
#         random_state=42
#     )

#     topic_model = BERTopic(
#         umap_model=umap_model,
#         vectorizer_model=vectorizer_model,
#         representation_model=representation_model,
#         min_topic_size=2,
#         nr_topics=12,   # ✅ UPDATED
#         verbose=False
#     )

#     return topic_model



import re
import fitz
from bertopic import BERTopic
from umap import UMAP
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.representation import KeyBERTInspired


# ---------------- PDF TEXT ----------------
def extract_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    return text


# ---------------- ABSTRACT ----------------
def extract_abstract(text):
    text_lower = text.lower()

    if "abstract" in text_lower:
        start = text_lower.find("abstract")
        end = text_lower.find("introduction")

        if end == -1:
            end = start + 1500

        return text[start:end]

    return text[:1500]


# ---------------- PREPROCESS ----------------
def preprocess_text(text):
    text = text.lower()
    text = text.split("references")[0]

    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\W+', ' ', text)

    words = text.split()

    stop_words = {
        "the", "and", "for", "with", "this", "that",
        "from", "are", "was", "were", "have", "has",
        "using", "based", "study", "paper", "research",
        "university", "department", "journal", "published",
        "article", "available", "received"
    }

    words = [w for w in words if len(w) > 3 and w not in stop_words]

    return " ".join(words[:400])


# ---------------- MODEL ----------------
def build_model(num_docs):

    vectorizer_model = CountVectorizer(
        ngram_range=(1, 2),
        stop_words="english"
    )

    representation_model = KeyBERTInspired()

    umap_model = UMAP(
        n_neighbors=15,
        n_components=5,
        min_dist=0.2,
        metric='cosine',
        random_state=42
    )

    # 🔥 Dynamic topic logic
    if num_docs < 20:
        nr_topics = None
        min_topic_size = 2
    else:
        nr_topics = 12
        min_topic_size = 5

    topic_model = BERTopic(
        umap_model=umap_model,
        vectorizer_model=vectorizer_model,
        representation_model=representation_model,
        min_topic_size=min_topic_size,
        nr_topics=nr_topics,
        verbose=False
    )

    return topic_model