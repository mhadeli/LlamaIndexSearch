# Document Query Interface

This project provides a document query interface using Streamlit, Llama Index, and a vector store index for querying documents. The application supports loading documents, creating a vectorized index, and querying the index with natural language queries.

## Table of Contents

- [How It Works](#How It Works)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## How It Works

This application provides a user-friendly interface for querying a collection of documents using natural language. Here’s a step-by-step guide on how the app works:

1. **Document Loading and Index Creation:**

    - The application starts by checking if a persistent storage directory (`storage/`) exists.
    - If the storage directory does not exist, it loads documents from the `data/` directory using `SimpleDirectoryReader`.
    - It then creates a vectorized index from these documents using `VectorStoreIndex`.
    - The created index is saved in the `storage/` directory for future use.
    - If the storage directory already exists, the application loads the existing index from this directory using `StorageContext`.

2. **Setting Up the Query Engine:**

    - The application sets up a retriever (`VectorIndexRetriever`) to fetch the most relevant documents based on similarity.
    - A postprocessor (`SimilarityPostprocessor`) is used to filter the results based on a similarity cutoff.
    - The `RetrieverQueryEngine` is initialized with the retriever and postprocessor to handle the querying process.

3. **User Interaction via Streamlit:**

    - The application uses Streamlit to provide a web-based interface.
    - Users enter their query in the input field provided on the Streamlit app.
    - Upon clicking the "Submit" button, the application processes the query using the query engine.
    - The results are displayed on the Streamlit interface, showing both the response and the sources.

4. **Detailed Steps in the Code:**

    - **Loading Environment Variables:**
      ```python
      load_dotenv()
      OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
      os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
      ```

    - **Creating or Loading the Index:**
      ```python
      if not os.path.exists(PERSIST_DIR):
          documents = SimpleDirectoryReader("data").load_data()
          index = VectorStoreIndex.from_documents(documents, show_progress=True)
          index.storage_context.persist(persist_dir=PERSIST_DIR)
      else:
          storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
          index = load_index_from_storage(storage_context)
      ```

    - **Setting Up the Query Engine:**
      ```python
      retriever = VectorIndexRetriever(index=index, similarity_top_k=4)
      postprocessor = SimilarityPostprocessor(similarity_cutoff=0.80)
      query_engine = RetrieverQueryEngine(retriever=retriever, node_postprocessors=[postprocessor])
      ```

    - **Streamlit Interface:**
      ```python
      st.title("Document Query Interface")

      query = st.text_input("Enter your query:", "")

      if st.button("Submit"):
          if query:
              response = query_engine.query(query)
              st.write("### Response")
              st.write(response)
              st.write("### Sources")
              st.write(pprint_response(response, show_source=True))
          else:
              st.error("Please enter a query.")
      ```

This application leverages the power of vectorized search and natural language processing to provide efficient and accurate document retrieval, all wrapped in a simple and intuitive web interface.

## Features

- Load documents and create a vectorized index.
- Persist the vectorized index for efficient querying.
- Query the document index using natural language.
- Streamlit-based user interface for interaction.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Set up environment variables:**

    Create a `.env` file in the root of the project directory and add your OpenAI API key:

    ```sh
    OPENAI_API_KEY=your_openai_api_key_here
    ```

2. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

3. **Interact with the interface:**

    - Enter your query in the provided input field.
    - Click the "Submit" button to get a response from the document index.

## Configuration

- **Environment Variables:** The application uses environment variables for sensitive information. Ensure you have a `.env` file with the necessary keys.
- **Persistent Storage:** The vectorized index is stored in the `storage/` directory. This directory is included in the `.gitignore` file to avoid uploading large and unnecessary files to the repository.

## Project Structure

```
my_app/
├── data/ # Directory for storing documents
│ └── (Save your documents here)
├── storage/ # Directory for storing vectorized index (ignored by git)
├── app.py # Main Streamlit application file
├── utils.py # Utility functions
├── requirements.txt # List of required packages
└── .env # Environment variables (ignored by git)
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
