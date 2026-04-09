# import streamlit as st
# import pandas as pd
# from utils import extract_text, extract_abstract, preprocess_text, build_model

# st.set_page_config(page_title="Research Topic Analyzer", layout="wide")

# st.title("📚 Research Paper Topic Analyzer")
# st.write("Upload research papers and get topics automatically")

# uploaded_files = st.file_uploader(
#     "Upload PDF files",
#     type=["pdf"],
#     accept_multiple_files=True
# )

# if uploaded_files:

#     if st.button("🚀 Analyze Papers"):

#         texts = []
#         filenames = []

#         with st.spinner("Processing papers..."):

#             for file in uploaded_files:

#                 raw_text = extract_text(file)
#                 abstract = extract_abstract(raw_text)
#                 clean_text = preprocess_text(abstract)

#                 if len(clean_text.split()) < 20:
#                     continue

#                 texts.append(clean_text)
#                 filenames.append(file.name)

#         st.success(f"✅ Processed {len(texts)} papers")

#         # ---------------- MODEL ----------------
#         topic_model = build_model()
#         topics, _ = topic_model.fit_transform(texts)

#         # ---------------- TOPIC INFO ----------------
#         topic_info = topic_model.get_topic_info()

#         st.subheader("📊 Topics Overview")
#         st.dataframe(topic_info, use_container_width=True)

#         # ---------------- TOPIC DETAILS ----------------
#         st.subheader("🧠 Topics and Keywords")

#         for topic_id in topic_model.get_topics():
#             if topic_id == -1:
#                 continue

#             words = [word for word, _ in topic_model.get_topic(topic_id)]

#             st.markdown(f"### Topic {topic_id}")
#             st.write(", ".join(words))

#         # ---------------- DOCUMENT TABLE ----------------
#         df = topic_model.get_document_info(texts)
#         df["File Name"] = filenames

#         st.subheader("📄 Papers with Topics")
#         st.dataframe(df[["File Name", "Topic", "Name"]], use_container_width=True)

#         # ---------------- DOWNLOAD EXCEL ----------------
#         excel_data = df[["File Name", "Topic", "Name"]]

#         def convert_to_excel(df):
#             return df.to_csv(index=False).encode('utf-8')

#         st.download_button(
#             label="📥 Download Results (Excel)",
#             data=convert_to_excel(excel_data),
#             file_name="topic_results.csv",
#             mime="text/csv"
#         )





















# import streamlit as st
# import pandas as pd
# import streamlit.components.v1 as components
# from utils import extract_text, extract_abstract, preprocess_text, build_model

# st.set_page_config(page_title="Research Topic Analyzer", layout="wide")

# st.title("📚 Research Paper Topic Analyzer")
# st.write("Upload research papers and get topics automatically")

# uploaded_files = st.file_uploader(
#     "Upload PDF files",
#     type=["pdf"],
#     accept_multiple_files=True
# )


# def clean_label(raw_label):
#     # remove topic number
#     label = "_".join(raw_label.split("_")[1:])
    
#     # split words
#     words = label.split("_")
    
#     # remove duplicates while keeping order
#     seen = set()
#     unique_words = []
#     for w in words:
#         if w not in seen:
#             unique_words.append(w)
#             seen.add(w)
    
#     # keep only first 3–4 important words
#     final_words = unique_words[:4]
    
#     # join nicely
#     return " ".join(final_words).title()

# if uploaded_files:

#     if st.button("🚀 Analyze Papers"):

#         texts = []
#         filenames = []

#         with st.spinner("Processing papers..."):

#             for file in uploaded_files:

#                 raw_text = extract_text(file)
#                 abstract = extract_abstract(raw_text)
#                 clean_text = preprocess_text(abstract)

#                 if len(clean_text.split()) < 20:
#                     continue

#                 texts.append(clean_text)
#                 filenames.append(file.name)

#         st.success(f"✅ Processed {len(texts)} papers")

#         # ---------------- MODEL ----------------
#         topic_model = build_model()
#         topics, _ = topic_model.fit_transform(texts)

#         # Generate better labels
#         topic_model.generate_topic_labels()
#         labels = topic_model.topic_labels_

#         # ---------------- SUMMARY ----------------
#         st.subheader("📌 Summary")

#         df = topic_model.get_document_info(texts)
#         df["File Name"] = filenames

#         for topic_id in topic_model.get_topics():
#             if topic_id == -1:
#                 continue

#             count = (df["Topic"] == topic_id).sum()
#             st.write(f"👉 {labels[topic_id]} → {count} papers")
#         # st.subheader("📌 Summary")

#         # for topic_id in topic_model.get_topics():
#         #     if topic_id == -1:
#         #         continue

#         # raw_label = labels[topic_id]
#         # label = clean_label(raw_label)

#         # count = (df["Topic"] == topic_id).sum()

#         # st.write(f"👉 {label} → {count} papers")

#         st.divider()

#         # ---------------- TOPIC OVERVIEW ----------------
#         st.subheader("📊 Topics Overview")
#         topic_info = topic_model.get_topic_info()
#         st.dataframe(topic_info, use_container_width=True)

#         # ---------------- TOPIC DETAILS ----------------
#         st.subheader("🧠 Topics and Keywords")

#         for topic_id in topic_model.get_topics():
#             if topic_id == -1:
#                 continue

#             # label = labels[topic_id]
#             raw_label = labels[topic_id]
#             label = clean_label(raw_label)
#             # raw_label = labels[topic_id]
#             # clean_label = " ".join(raw_label.split("_")[1:4]).title()
#             words = [word for word, _ in topic_model.get_topic(topic_id)[:6]]  # ✅ 6 keywords

#             with st.container():
#                 st.markdown(f"### -> {label}")
#                 st.success(", ".join(words))

#         st.divider()

#         # ---------------- INTERTOPIC MAP ----------------
#         st.subheader("🗺️ Intertopic Distance Map")

#         fig = topic_model.visualize_topics()
#         components.html(fig.to_html(), height=600)

#         st.divider()

#         # ---------------- BARCHART ----------------
#         st.subheader("📊 Keyword Importance")

#         fig_bar = topic_model.visualize_barchart()
#         components.html(fig_bar.to_html(), height=600)

#         st.divider()

#         # ---------------- HEATMAP ----------------
#         st.subheader("🔥 Topic Similarity Heatmap")

#         fig_heatmap = topic_model.visualize_heatmap()
#         components.html(fig_heatmap.to_html(), height=600)

#         st.divider()

#         # ---------------- DOCUMENT TABLE ----------------
#         st.subheader("📄 Papers with Topics")

#         df = df[df["Topic"] != -1]  # ✅ remove outliers
#         df["Topic Label"] = df["Topic"].map(labels)

#         st.dataframe(df[["File Name", "Topic Label"]], use_container_width=True)

#         # ---------------- DOWNLOAD ----------------
#         def convert_to_excel(df):
#             return df.to_csv(index=False).encode('utf-8')

#         st.download_button(
#             label="📥 Download Results (Excel)",
#             data=convert_to_excel(df[["File Name", "Topic Label"]]),
#             file_name="topic_results.csv",
#             mime="text/csv"
#         )



























import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils import extract_text, extract_abstract, preprocess_text, build_model

st.set_page_config(page_title="Research Topic Analyzer", layout="wide")

st.title("📚 Research Paper Topic Analyzer")
st.write("Upload research papers and get topics automatically")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)


# ---------------- CLEAN LABEL FUNCTION ----------------
def clean_label(raw_label):
    words = raw_label.split("_")[1:]  # remove topic id

    # remove duplicates
    words = list(dict.fromkeys(words))

    # remove very repetitive words
    filtered = []
    for w in words:
        if w not in filtered:
            filtered.append(w)

    # take first 3 words
    words = filtered[:3]

    return " ".join(words).title()


# ---------------- MAIN ----------------
if uploaded_files:

    if st.button("🚀 Analyze Papers"):

        texts = []
        filenames = []

        with st.spinner("Processing papers..."):

            for file in uploaded_files:
                raw_text = extract_text(file)
                abstract = extract_abstract(raw_text)
                clean_text = preprocess_text(abstract)

                if len(clean_text.split()) < 20:
                    continue

                texts.append(clean_text)
                filenames.append(file.name)

        st.success(f"✅ Processed {len(texts)} papers")

        # ---------------- MODEL ----------------
        topic_model = build_model(len(texts))
        topics, _ = topic_model.fit_transform(texts)

        topic_model.generate_topic_labels()
        labels = topic_model.topic_labels_

        # ---------------- DATAFRAME ----------------
        df = topic_model.get_document_info(texts)
        df["File Name"] = filenames

        # ---------------- SUMMARY ----------------
        st.subheader("📌 Summary")

        for topic_id in topic_model.get_topics():
            if topic_id == -1:
                continue

            label = clean_label(labels[topic_id])
            count = (df["Topic"] == topic_id).sum()

            st.write(f"👉 {label} → {count} papers")

        st.divider()

        # ---------------- TOPIC OVERVIEW ----------------
        # st.subheader("📊 Topics Overview")
        # topic_info = topic_model.get_topic_info()
        # st.dataframe(topic_info, use_container_width=True)

        st.subheader("📊 Topics Overview")

        topic_info = topic_model.get_topic_info()

# remove outliers
        topic_info = topic_info[topic_info["Topic"] != -1]

# clean labels
        topic_info["Clean Name"] = topic_info["Name"].apply(clean_label)

# select useful columns only
        clean_table = topic_info[["Topic", "Clean Name", "Count"]]

# rename columns
        clean_table.columns = ["Topic ID", "Topic Name", "Number of Papers"]

        st.dataframe(clean_table, use_container_width=True)

        # ---------------- TOPICS ----------------
        st.subheader("🧠 Topics and Keywords")

        for topic_id in topic_model.get_topics():
            if topic_id == -1:
                continue

            label = clean_label(labels[topic_id])
            words = [word for word, _ in topic_model.get_topic(topic_id)[:6]]

            with st.container():
                st.markdown(f"### -> {label}")
                st.success(", ".join(words))

        st.divider()

        # ---------------- VISUALIZATIONS ----------------
        valid_topics = [t for t in topic_model.get_topics().keys() if t != -1]

        # Intertopic Map
        st.subheader("🗺️ Intertopic Distance Map")

        if len(valid_topics) > 1:
            try:
                fig = topic_model.visualize_topics()
                components.html(fig.to_html(), height=600)
            except:
                st.warning("⚠️ Could not generate intertopic map.")
        else:
            st.warning("⚠️ Not enough topics.")

        st.divider()

        # Barchart
        # st.subheader("📊 Keyword Importance")

        # try:
        #     fig_bar = topic_model.visualize_barchart()
        #     components.html(fig_bar.to_html(), height=600)
        # except:
        #     st.warning("⚠️ Could not generate barchart.")



        # st.subheader("📊 Keyword Importance")

        # try:
        #     fig_bar = topic_model.visualize_barchart(
        #     top_n_topics=5,   # 🔥 only show top 5 topics
        #     n_words=6         # limit words per topic
        #     )

        #     components.html(fig_bar.to_html(), height=800)

        # except:
        #     st.warning("⚠️ Could not generate barchart.")

#         st.subheader("📊 Keyword Importance")

# # apply clean labels
#         topic_model.set_topic_labels({
#         topic_id: clean_label(labels[topic_id])
#         for topic_id in topic_model.get_topics()
#             if topic_id != -1
#                 })

#         try:
#             fig_bar = topic_model.visualize_barchart(
#                 top_n_topics=5,
#                 n_words=6
#             )

#             components.html(fig_bar.to_html(), height=900)

#         except:
#             st.warning("⚠️ Could not generate barchart.")


        # import matplotlib.pyplot as plt

        # st.subheader("📊 Keyword Importance (Topic-wise)")

        # for topic_id in topic_model.get_topics():
        #     if topic_id == -1:
        #         continue

        #     label = clean_label(labels[topic_id])
        #     words_scores = topic_model.get_topic(topic_id)[:6]

        #     words = [w for w, _ in words_scores]
        #     scores = [s for _, s in words_scores]

        #     st.markdown(f"### 🧠 {label}")

        #     # fig, ax = plt.subplots()
        #     fig, ax = plt.subplots(figsize=(5, 3))
        #     ax.barh(words[::-1], scores[::-1])  # reverse for better display
        #     ax.set_xlabel("Importance")
        #     ax.set_title(label)

        #     # st.pyplot(fig)
        #     st.pyplot(fig, use_container_width=False)





        import matplotlib.pyplot as plt

        st.subheader("📊 Keyword Importance (Topic-wise)")

        topics = [t for t in topic_model.get_topics().keys() if t != -1]

# iterate in pairs (2 per row)
        for i in range(0, len(topics), 2):

            cols = st.columns(2)

            for j in range(2):
                if i + j >= len(topics):
                    break

                topic_id = topics[i + j]

                label = clean_label(labels[topic_id])
                words_scores = topic_model.get_topic(topic_id)[:6]

                words = [w for w, _ in words_scores]
                scores = [s for _, s in words_scores]

                fig, ax = plt.subplots(figsize=(4, 2.5))

                ax.barh(words[::-1], scores[::-1], height=0.4)
                ax.set_title(label, fontsize=9)
                ax.tick_params(axis='both', labelsize=7)

        # remove extra clutter
                ax.set_xlabel("")
                ax.grid(axis="x", linestyle="--", alpha=0.3)

                with cols[j]:
                    st.pyplot(fig, use_container_width=True)        
        st.divider()

        # Heatmap
        # st.subheader("🔥 Topic Similarity Heatmap")

        # if len(valid_topics) > 1:
        #     try:
        #         fig_heatmap = topic_model.visualize_heatmap()
        #         components.html(fig_heatmap.to_html(), height=3000)
        #     except:
        #         st.warning("⚠️ Could not generate heatmap.")


        import numpy as np
        import matplotlib.pyplot as plt

        st.subheader("🔥 Topic Similarity Heatmap")

        topics = [t for t in topic_model.get_topics().keys() if t != -1]

        if len(topics) > 1:

            try:
        # get topic embeddings
                embeddings = topic_model.topic_embeddings_

        # compute similarity matrix (cosine similarity)
                similarity_matrix = np.inner(embeddings, embeddings)

        # get clean labels
                labels_clean = [clean_label(labels[t]) for t in topics]

                fig, ax = plt.subplots(figsize=(6, 5))

                im = ax.imshow(similarity_matrix, aspect='auto')

        # ticks
                ax.set_xticks(range(len(labels_clean)))
                ax.set_yticks(range(len(labels_clean)))

                ax.set_xticklabels(labels_clean, rotation=45, ha='right', fontsize=8)
                ax.set_yticklabels(labels_clean, fontsize=8)

                ax.set_title("Topic Similarity Heatmap", fontsize=10)

        # add color bar
                fig.colorbar(im, ax=ax)

                st.pyplot(fig)

            except:
                st.warning("⚠️ Could not generate heatmap.")
        else:
            st.warning("⚠️ Not enough topics.")

        st.divider()

        # ---------------- TABLE ----------------
        # st.subheader("📄 Papers with Topics")

        # df = df[df["Topic"] != -1]
        # df["Topic Label"] = df["Topic"].map(lambda x: clean_label(labels[x]))

        # st.dataframe(df[["File Name", "Topic Label"]], use_container_width=True)


        st.subheader("📄 Papers with Topics")

# remove outliers
        df = df[df["Topic"] != -1].copy()

# add clean labels
        df["Topic Label"] = df["Topic"].map(lambda x: clean_label(labels[x]))

# add keywords column
        df["Keywords"] = df["Topic"].apply(
            lambda x: ", ".join([w for w, _ in topic_model.get_topic(x)[:5]])
        )

# sort by topic
        df = df.sort_values(by="Topic").reset_index(drop=True)

# select columns
        display_df = df[["File Name", "Topic", "Topic Label", "Keywords"]]
        display_df.columns = ["File Name", "Topic ID", "Topic Name", "Top Keywords"]

        st.dataframe(display_df, use_container_width=True)
        # ---------------- DOWNLOAD ----------------
        def convert_to_excel(df):
            return df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Download Detailed Results",
            data=convert_to_excel(display_df),
            file_name="topic_analysis_results.csv",
            mime="text/csv"
        )


        # def convert_to_excel(df):
        #     return df.to_csv(index=False).encode('utf-8')

        # st.download_button(
        #     label="📥 Download Results (Excel)",
        #     data=convert_to_excel(df[["File Name", "Topic Label"]]),
        #     file_name="topic_results.csv",
        #     mime="text/csv"
        # )