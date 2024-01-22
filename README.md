# AI Author: A Scientific Text Writing Tool Based on ChatGPT APIs

Welcome to AI AUTHOR, an innovative tool designed to revolutionize the process of scientific writing. This platform seamlessly integrates cutting-edge technologies, including OpenAI's ChatGPT API, FastAPI, and ReactJS, to offer a comprehensive solution for researchers, students, and scientific writers.

<p align="center">
  <img src="https://github.com/AyaElAmari/AI_AUTHOR_FINAL_PROJECT/blob/main/AI_AUTHOR-logo.png" alt="Project logo" height="100px">
</p>

## System Architecture and Communication Flow

AI AUTHOR is built on a modular architecture that facilitates seamless communication between its key components:

- **OpenAI Service (main.py):** Interfaces with OpenAI's ChatGPT API for linguistic analysis and text generation.
- **FastAPI-based REST API (restapifastapi):** Acts as a bridge between the frontend and the OpenAI service.
- **Uvicorn:** Serves as the ASGI server, handling HTTP requests and directing them to the FastAPI application.

On the frontend:

- **ReactJS, Next.js, and Material-UI:** Collaborate to create a dynamic user interface.

Users interact with the frontend, initiating requests for linguistic analysis or text generation. The communication flow begins with user interactions triggering HTTP requests to the FastAPI backend. The backend orchestrates communication with the OpenAI service, and the processed results are dynamically presented on the user interface.

This modular architecture ensures efficiency and responsiveness, offering a robust platform for linguistic analysis and text generation. Explore the repository for installation instructions and detailed documentation.

<p align="center">
  <img src="https://github.com/AyaElAmari/AI_AUTHOR_FINAL_PROJECT/blob/main/architecture_AI_Author.png" alt="Project Architecture" height="600px">
</p>

## Link to Video Demo

Explore the powerful features of AI AUTHOR in action through our comprehensive video demo. See how AI AUTHOR transforms the scientific writing experience for researchers, students, and scientific writers. The demo showcases key functionalities:

- **Article Generation:** Effortlessly create high-quality scientific articles.
- **ChatPDF:** Seamlessly upload a PDF file, pose specific questions, and receive detailed information directly extracted from the document.
- **Grammatical Correction:** Identify and rectify grammatical errors within texts, ensuring the final output meets the highest standards of academic writing.
- **Vocabulary Enhancement Assistance:** Explore intelligent suggestions that enrich the vocabulary used in texts, fostering more nuanced and precise expression.
- **Text Summarization:** Experience AI AUTHOR's capability to generate concise summaries while preserving the essence of the original content.
- **Translation Functionality:** See the precise translation capabilities in action, facilitating the conversion of texts into English.

This video provides a firsthand look at how AI AUTHOR serves as a comprehensive and indispensable tool for enhancing the scientific writing experience. [Watch the Video Demo](https://drive.google.com/file/d/1YV13-MRoontcunXIbTmx0Xpa_E-Bb5q8/view?usp=drive_link)
