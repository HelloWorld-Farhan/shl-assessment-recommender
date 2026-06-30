# Approach Document: Conversational SHL Assessment Recommender

## 1. Design Choices and Architecture
To build a highly responsive and accurate conversational agent for the SHL catalog, I utilized a **Retrieval-Augmented Generation (RAG)** architecture powered by **Python**, **FastAPI**, and the **Gemini LLM**. 

- **Language & Framework:** Python was chosen due to its extensive ecosystem for AI and data processing. FastAPI was selected for the web framework because it is modern, high-performance, and natively supports Pydantic models, which ensures our API precisely adheres to the strict JSON schema required by the evaluator.
- **LLM Choice:** I utilized Google's Gemini API (`gemini-1.5-flash`). It offers a generous free tier, is exceptionally fast, and natively supports JSON-mode outputs (`response_mime_type="application/json"`), virtually eliminating schema compliance issues.
- **Stateless Design:** The API (`POST /chat`) relies entirely on the `messages` array passed in the payload, ensuring no per-conversation state is held in the server's memory, as required by the specification.

## 2. Retrieval Setup (RAG)
Given the size of the SHL product catalog, I implemented a semantic search retrieval system.
- **Embeddings:** I used the `sentence-transformers` library (specifically the lightweight `all-MiniLM-L6-v2` model) to convert catalog items into high-dimensional vector embeddings. 
- **Index:** I utilized `faiss-cpu` (Facebook AI Similarity Search) to index these embeddings. 
- **Data Ingestion:** During cold-start, the application parses `shl_product_catalog.json`. It constructs a rich textual representation of each assessment by combining its Name, Description, Job Levels, Languages, and Keys.
- **Querying:** When a user sends a message, the system concatenates the user's historical prompts to capture full context. This context is embedded and queried against the FAISS index to retrieve the top 10 most relevant assessments.

## 3. Prompt Design
The prompt is the crucial bridge that forces the LLM to adhere to conversational constraints.
- **Persona & Boundaries:** The System Prompt explicitly defines the agent's role ("SHL Conversational Assessment Recommender") and strictly forbids hallucinating products or discussing out-of-scope topics like legal advice.
- **Dynamic Context Injection:** The retrieved items from the FAISS index are dynamically injected into the prompt under a section titled `AVAILABLE SHL CATALOG ITEMS`. 
- **Formatting Rules:** The prompt explicitly outlines the required JSON schema and maps the catalog's `keys` to the required `test_type` single-letter format (e.g., "Knowledge & Skills" -> "K").

## 4. Evaluation Method
Evaluation was handled through a dual approach:
- **Local Sandbox Replays:** I built a simple automated script (`evaluate.py`) that sends structured payloads mimicking the public trace files (`C1.md` - `C10.md`) to the local FastAPI instance. This allowed me to visually verify tone, accuracy, and schema compliance.
- **Metric Tracking:** The primary metric focused on was **Recall@10**. By ensuring the FAISS vector search always pulls a healthy mix of top candidates based on semantic meaning (rather than rigid keyword matching), the agent consistently had access to the correct assessments required to formulate the final shortlist.

## 5. What Didn't Work & Improvements
- **Initial Setup (What didn't work):** Initially, I attempted to pass the *entire* JSON catalog into the LLM context window. While modern context windows can handle this, it significantly degraded response times and occasionally confused the LLM when comparing highly similar products. 
- **Improvement:** Introducing the FAISS semantic retriever drastically reduced the token payload sent to the LLM, lowering latency and significantly improving the model's focus on the most relevant 10-15 items. Furthermore, enforcing JSON mode natively in the Gemini API SDK entirely eliminated earlier issues with malformed JSON strings or markdown block formatting.
