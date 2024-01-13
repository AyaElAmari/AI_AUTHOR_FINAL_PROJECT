## System Architecture and Communication Flow

AI AUTHOR is built on a modular architecture that facilitates seamless communication between its key components. The OpenAI service (main.py) interfaces with OpenAI's ChatGPT API for linguistic analysis and text generation. This service communicates with the FastAPI-based REST API (restapifastapi), acting as a bridge between the frontend and the OpenAI service. Uvicorn serves as the ASGI server, handling HTTP requests and directing them to the FastAPI application.

On the frontend, ReactJS, Next.js, and Material-UI collaborate to create a dynamic user interface. Users interact with the frontend, initiating requests for linguistic analysis or text generation. The communication flow begins with user interactions triggering HTTP requests to the FastAPI backend. The backend orchestrates communication with the OpenAI service, and the processed results are dynamically presented on the user interface.

This modular architecture ensures efficiency and responsiveness, offering a robust platform for linguistic analysis and text generation. Explore the repository for installation instructions and detailed documentation.

![Project Architecture](https://github.com/AyaElAmari/AI_AUTHOR_FINAL_PROJECT/blob/main/architecture_AI_Author.png)

## Link to Video Demo

[Link to Video Demo](https://drive.google.com/file/d/1YV13-MRoontcunXIbTmx0Xpa_E-Bb5q8/view?usp=drive_link)
