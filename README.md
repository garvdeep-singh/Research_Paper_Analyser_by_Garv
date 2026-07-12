# Research Paper Topic Analyzer

## Overview

This project is a Streamlit-based web application that helps users analyze multiple research paper PDFs and automatically discover the main topics present in them. It uses BERTopic, a modern topic modeling technique, to group papers into meaningful themes based on the content of their abstracts.

The app is especially useful for:
- researchers who want to quickly understand the themes in a collection of papers
- students working on literature reviews
- academic teams organizing large sets of publications
- anyone who wants to explore topics hidden inside PDF documents

---

## What This Project Does

The application performs the following steps:

1. Accepts one or more PDF files from the user.
2. Extracts the text from each uploaded PDF.
3. Identifies the abstract section (when available) and uses it as the main source of content.
4. Cleans and preprocesses the text to remove noise and irrelevant words.
5. Builds a topic model using BERTopic.
6. Displays the discovered topics, their keywords, and a summary of which papers belong to which topic.
7. Allows the user to download the results in CSV format.

---

## Main Features

- Upload multiple PDF research papers at once
- Automatic text extraction from PDFs using PyMuPDF
- Smart abstract detection from each paper
- Text cleaning and preprocessing for topic modeling
- Topic discovery using BERTopic
- Topic summary with paper counts
- Clean topic labels for easier understanding
- Downloadable results for further analysis

---

## Project Structure

The repository contains the following files:

- app.py: the main Streamlit web application
- utils.py: contains the text extraction, preprocessing, and BERTopic model building logic
- requirements.txt: all Python dependencies required for the project
- README.md: documentation for the project

---

## Detailed Explanation of Each File

### 1. app.py

This is the frontend and main application logic.

It is responsible for:
- creating the Streamlit web interface
- allowing the user to upload PDF files
- processing each uploaded file
- calling the helper functions from utils.py
- running the topic model
- displaying the results in a user-friendly format

In this file, the user interacts with the app through a file uploader and an analysis button. Once the button is clicked, the app processes the uploaded documents and shows:
- a summary of the discovered topics
- a topic overview table
- topic names and important keywords
- a list of papers associated with each topic
- a download option for the results

### 2. utils.py

This file contains the core backend logic.

It includes several important helper functions:

#### extract_text(file)
This function opens a PDF file and extracts all visible text from its pages using PyMuPDF.

#### extract_abstract(text)
This function tries to locate the abstract section in the paper text. If it finds the word "abstract", it extracts the content from that point until the introduction section begins. If no abstract is found, it uses the first 1500 characters as a fallback.

#### preprocess_text(text)
This function cleans the extracted text by:
- converting it to lowercase
- removing references section content
- removing numbers
- removing special characters and symbols
- removing very short words
- removing common stop words that do not add much meaning
- keeping only a manageable portion of the text for topic modeling

This step is necessary because raw academic text contains a lot of noise that can reduce the quality of topic modeling.

#### build_model(num_docs)
This function creates and configures the BERTopic model.

It uses:
- CountVectorizer for text vectorization
- KeyBERTInspired for keyword generation
- UMAP for dimensionality reduction
- BERTopic for topic extraction

The model is also adjusted depending on the number of documents. If the user uploads fewer documents, the topic model uses fewer constraints; if the user uploads many documents, it creates a larger set of topics.

### 3. requirements.txt

This file lists all the Python packages required to run the app successfully. These include:
- streamlit for the web app interface
- PyMuPDF for PDF reading
- BERTopic for topic modeling
- scikit-learn for text processing and vectorization
- umap-learn for dimensionality reduction
- sentence-transformers and transformers for language-based capabilities
- pandas for result handling

---

## How the Application Works

The workflow of the project can be summarized as follows:

1. The user uploads research papers in PDF format.
2. The system reads the PDF text.
3. The abstract section is extracted and cleaned.
4. The cleaned text is passed into BERTopic.
5. BERTopic identifies clusters of related content.
6. The app presents these clusters as topics with associated keywords.
7. Each uploaded paper is assigned to one of the discovered topics.
8. The results can be downloaded for review.

---

## Technologies Used

This project uses the following technologies:

- Python
- Streamlit
- PyMuPDF
- BERTopic
- UMAP
- scikit-learn
- pandas
- Plotly (indirectly through topic visualization support)

---

## Installation Instructions

Follow these steps to set up the project locally:

1. Clone or download the repository.
2. Open the project folder in your terminal.
3. Create a Python virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
streamlit run app.py
```

6. Open the local URL provided by Streamlit in your browser.

---

## How to Use the App

1. Launch the app using Streamlit.
2. Upload one or more PDF files.
3. Click the analysis button.
4. Wait while the app processes the papers.
5. Review the summary and topic outputs.
6. Download the results if needed.

---

## What the Output Means

After analysis, the app shows:

- Topic summary: a list of topics found in the uploaded papers
- Topic names: machine-generated labels based on words and patterns in the documents
- Keywords: important terms associated with each topic
- Paper-topic mapping: which papers are grouped under each topic

This helps users understand how the uploaded documents are related and what themes they share.

---

## Example Use Case

Suppose a user uploads 20 research papers about machine learning, healthcare, and cybersecurity. The app can discover topics such as:
- deep learning
- medical image analysis
- intrusion detection
- natural language processing

Each paper will be grouped into the most relevant topic cluster.

---

## Important Notes and Limitations

Although this project is powerful, it has some limitations:

- The quality of topic modeling depends heavily on the quality of the source text.
- PDFs with poor text extraction may produce weaker results.
- The model performs best when the papers are related to each other.
- Abstract-only analysis may miss useful information from the full paper body.
- Topic labels are automatically generated and may not always be perfect.

---

## Future Improvements

Possible improvements for this project include:
- supporting full-paper text extraction instead of only abstract-based analysis
- adding better topic visualization charts
- adding a sidebar for model parameters
- supporting TXT, DOCX, and HTML file uploads
- improving topic label quality with custom naming rules
- adding export options such as Excel or JSON
- improving performance for very large document collections

---

## Summary

This project is a practical and intelligent document analysis tool for research papers. It transforms uploaded PDFs into a structured topic overview, making it easier to explore academic content, organize literature, and discover hidden themes. By combining Streamlit with BERTopic, the app offers a simple but powerful experience for topic-based document analysis.
