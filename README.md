# Document Query Interface

This project provides a document query interface using Streamlit, Llama Index, and a vector store index for querying documents. The application supports loading documents, creating a vectorized index, and querying the index with natural language queries.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

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
│ └── (your documents here)
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
