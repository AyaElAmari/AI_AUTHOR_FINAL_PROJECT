## System Architecture and Communication Flow

AI AUTHOR is built on a modular architecture that facilitates seamless communication between its key components. The OpenAI service (main.py) interfaces with OpenAI's ChatGPT API for linguistic analysis and text generation. This service communicates with the FastAPI-based REST API (restapifastapi), acting as a bridge between the frontend and the OpenAI service. Uvicorn serves as the ASGI server, handling HTTP requests and directing them to the FastAPI application.

On the frontend, ReactJS, Next.js, and Material-UI collaborate to create a dynamic user interface. Users interact with the frontend, initiating requests for linguistic analysis or text generation. The communication flow begins with user interactions triggering HTTP requests to the FastAPI backend. The backend orchestrates communication with the OpenAI service, and the processed results are dynamically presented on the user interface.

This modular architecture ensures efficiency and responsiveness, offering a robust platform for linguistic analysis and text generation. Explore the repository for installation instructions and detailed documentation.

![Project Architecture](https://github.com/AyaElAmari/AI_AUTHOR_FINAL_PROJECT/blob/main/architecture_AI_Author.png)

## Link to Video Demo

Explore the powerful features of AI AUTHOR in action through our comprehensive video demo. See how AI AUTHOR transforms the scientific writing experience for researchers, students, and scientific writers. The demo showcases key functionalities, including:

- **Article Generation:** Effortlessly create high-quality scientific articles, providing a swift and efficient solution for authors.
  
- **ChatPDF:** Seamlessly upload a PDF file, pose specific questions, and receive detailed information directly extracted from the document, adding an interactive dimension to the research process.

- **Grammatical Correction:** Witness how AI AUTHOR excels in identifying and rectifying grammatical errors within texts, ensuring the final output meets the highest standards of academic writing.

- **Vocabulary Enhancement Assistance:** Explore intelligent suggestions that enrich the vocabulary used in texts, fostering more nuanced and precise expression.

- **Text Summarization:** Experience AI AUTHOR's capability to generate concise summaries while preserving the essence of the original content, facilitating efficient information extraction and comprehension.

- **Translation Functionality:** See the precise translation capabilities in action, facilitating the conversion of texts into English and promoting effective interlinguistic communication in academic and research contexts.

This video provides a firsthand look at how AI AUTHOR serves as a comprehensive and indispensable tool for enhancing the scientific writing experience. Watch now to discover the transformative potential of our platform.


[Link to Video Demo](https://drive.google.com/file/d/1YV13-MRoontcunXIbTmx0Xpa_E-Bb5q8/view?usp=drive_link)
