# Agentic AI Engineering Bootcamp Capstone Project – SDA

### WAIN AI Agent Capstone Project

### **Project Name:** WAIN (وين؟)

### **Team Members:**

1- Reema Almutawa (Data Collection & Preparation - AI & Agent Engineer)

2- Fatimah Alqahtani (PostgreSQL Database Engineer)

3- Alanoud Alotaibi (UI Engineer)

### **Project Title & Description:**

**WAIN: AI-Powered Place Recommendation Agent**

AI-powered place recommendation agent that helps users discover and choose places in Riyadh, Saudi Arabia.

### **Problem Statement:**

Planning a trip or deciding where to go often requires searching across multiple websites and applications. This can make it difficult and time-consuming for users to:

* Find places that fit their budget
* Choose activities that match their available time
* Discover places that match their interests and preferences
* Compare different options efficiently
* Make quick and informed decisions

#### Our Solution:

**WAIN** is an AI-powered place recommendation agent designed specifically for **Riyadh, Saudi Arabia**. It understands user preferences and combines them with structured travel information to filter, rank, and provide relevant and personalized place recommendations in one place, helping users make faster and easier travel decisions.




# How to Run the WAIN‑AI‑Agent Capstone Project
Follow the steps below to set up the environment, configure the database and API key, and run the WAIN application.

#### **1- Clone the Repository:**
Download the project to your machine:

```bash
git clone https://github.com/ReemaSaif/WAIN-AI-Agent-Capstone-Project-SDA.git
cd WAIN-AI-Agent-Capstone-Project-SDA
```

#### **2- Create & Activate a Virtual Environment:**
This keeps dependencies clean and isolated.

**On Windows:**
```
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

#### **3- Install Project Dependencies:**
Make sure your virtual environment is active, then run:

```
pip install -r requirements.txt
```
If you are using UV:

```
uv pip install -r requirements.txt
```

#### **4- Configure Environment Variables (Required to run the agent):**
WAIN requires an OpenAI API key and PostgreSQL database credentials.
Create a .env file in the project root:

```
OPENAI_API_KEY=your_api_key_here

DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_postgresql_username
DB_PASSWORD=your_postgresql_password
```
Replace the database values with your PostgreSQL configuration.

**How to Get Your `OPENAI_API_KEY`:**

- Go to the OpenAI dashboard:  
   https://platform.openai.com/login

- Sign in with your OpenAI account.

- Click -**“Create new secret key”**.

- Copy the generated API key.

- Create a `.env` file in the project root and add:
```
OPENAI_API_KEY=your_api_key_here
```

- Save the file — your project will now load the key automatically.


**Important Note:**  
Your API key is generated only once. Make sure to copy the key and save it in the .env file immediately, because you will not be able to view it again after it is created.


#### **5- Set Up the PostgreSQL Database:**
* Make sure PostgreSQL is installed and running on your computer.

* Create the WAIN database and the required tables using the SQL files provided in the project. Then import the WAIN dataset into the ``` places``` table.

* The database should contain the place information used by WAIN for retrieval and recommendations.


#### **6- Test the Database Connection:**
* Before running the application, you can verify that WAIN can connect to PostgreSQL:

```
python test_db_connection.py
```

You should see a successful connection message.

* You can also test retrieving places from the database:

```
python test_read_places_table.py
```

#### **7- Run the WAIN Application:**
From the project root directory, run:

```
streamlit run app.py
```

Streamlit will launch the WAIN interface in your browser.

The application allows users to enter natural-language requests such as:
```
I want an Indian restaurant with a rating above 4.5.
```

**WAIN will:**

* Extract the user's preferences using the OpenAI LLM.
* Retrieve matching places from PostgreSQL.
* Rank the retrieved places according to the user's preferences.
* Generate a final personalized response.
* Display the recommendations through the Streamlit interface.

#### **8- Open WAIN in the Browser:**
If Streamlit does not open automatically, open the local address shown in the terminal, usually:
```
http://localhost:8501
```
You can then interact with WAIN and enter your place-related requests.


