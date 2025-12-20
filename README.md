<div align="center">

# 🥗 Diet Recommendation System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.88.0-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.16.0-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**An AI-powered nutrition companion that provides personalized diet recommendations using content-based filtering with 500,000+ recipes**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
  - [Docker Setup](#docker-setup-recommended)
  - [Local Setup](#local-setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Dataset](#-dataset)
- [API Documentation](#-api-documentation)
- [Performance Optimizations](#-performance-optimizations)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

The **Diet Recommendation System** is a modern web application that helps users discover personalized meal plans and recipes tailored to their nutritional needs, dietary restrictions, and budget constraints. Using advanced machine learning algorithms and a comprehensive database of over 500,000 recipes from Food.com, the system provides intelligent recommendations that make healthy eating accessible and enjoyable.

### Why This Project?

In today's fast-paced world, maintaining a balanced diet is challenging. This system addresses common pain points:

- ❓ **Confusion about nutrition** - Get science-backed recommendations
- ⏰ **Time constraints** - Quick meal planning with shopping lists
- 💰 **Budget limitations** - Cost-effective recipe filtering
- 🍽️ **Dietary restrictions** - Support for allergies and preferences
- 🎯 **Personalization** - Tailored to your unique health goals

---

## ✨ Features

### 🎯 Core Functionality

- **💪 Personalized Diet Plans** - Custom recommendations based on age, weight, height, activity level, and health goals
- **🔍 Smart Recipe Search** - Find recipes by nutritional values and ingredients
- **🍽️ Weekly Meal Planner** - AI-powered meal planning with automated shopping lists
- **💰 Budget Tracking** - Filter recipes by cost and track expenses
- **🛒 Shopping List Generator** - Consolidated grocery lists with cost estimates
- **⚡ Instant Chat Assistant** - Quick FAQ responses or optional AI chat for personalized advice

### 🎨 User Experience

- **Modern UI** - Beautiful gradient design with smooth animations
- **Responsive Design** - Works seamlessly on desktop and mobile
- **Fast Performance** - Instant responses with optional AI mode
- **Interactive Visualizations** - Nutritional charts and meal breakdowns
- **Easy Navigation** - Intuitive interface with clear guidance

### 🔧 Technical Features

- **Content-Based Filtering** - ML-powered recipe matching using scikit-learn
- **RESTful API** - FastAPI backend with automatic documentation
- **Scalable Architecture** - Microservices design with Docker support
- **Caching** - Optimized performance with smart caching
- **Extensible** - Modular design for easy feature additions

---

## 🎬 Demo

### Live Application

🌐 **Try it now:** [Diet Recommendation System](https://huggingface.co/spaces/saiteja1817/dietrecommendationsystem)

**🚀 Live Demo:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/saiteja1817/dietrecommendationsystem)

The application is deployed on Hugging Face Spaces with full TinyLlama LLM chat functionality for intelligent recipe recommendations and meal planning assistance.

### Key Features in Action:

- **Personalized Diet Plans** - Get custom meal recommendations
- **Smart Recipe Search** - Find recipes matching your nutritional needs
- **Weekly Meal Planner** - Plan your entire week with shopping lists
- **Budget Tracking** - Stay within your meal budget
- **Instant Chat** - Get quick answers to nutrition questions

---

## 🛠️ Technology Stack

### Backend
- **FastAPI** (0.88.0) - Modern, fast web framework for building APIs
- **Uvicorn** (0.20.0) - Lightning-fast ASGI server
- **Scikit-learn** (1.1.3) - Machine learning for recommendation engine
- **Pandas** (1.5.1) - Data manipulation and analysis
- **NumPy** (1.24.1) - Numerical computing

### Frontend
- **Streamlit** (1.16.0) - Interactive web application framework
- **Streamlit-Echarts** (0.4.0) - Beautiful data visualizations
- **BeautifulSoup4** (4.11.1) - Web scraping for recipe images
- **Requests** (2.28.1) - HTTP library for API calls

### ML & AI
- **Nearest Neighbors Algorithm** - Content-based filtering
- **Cosine Similarity** - Recipe matching metric
- **TinyLlama** (Optional) - Local LLM for chat assistance

### DevOps
- **Docker** & **Docker Compose** - Containerization
- **Git** - Version control

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[Streamlit UI]
        B[Hello.py - Welcome]
        C[Diet Recommendation]
        D[Custom Search]
        E[Meal Planner]
    end
    
    subgraph "API Layer"
        F[FastAPI Server]
        G["predict Endpoint"]
    end
    
    subgraph "ML Layer"
        H[Recommendation Engine]
        I[Nearest Neighbors]
        J[Cosine Similarity]
    end
    
    subgraph "Data Layer"
        K[(Recipe Database)]
        L[500K+ Recipes]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    C --> F
    D --> F
    E --> F
    F --> G
    G --> H
    H --> I
    H --> J
    I --> K
    J --> K
    K --> L
```

### System Flow

1. **User Input** → User provides preferences (nutrition, budget, restrictions)
2. **API Request** → Frontend sends request to FastAPI backend
3. **ML Processing** → Recommendation engine processes using Nearest Neighbors
4. **Recipe Matching** → Cosine similarity finds best matches from 500K+ recipes
5. **Response** → Filtered, ranked recipes returned to user
6. **Visualization** → Interactive charts and meal plans displayed

---

## 📦 Installation

### Prerequisites

- **Python 3.10+**
- **Docker & Docker Compose** (for containerized setup)
- **Git**

### Docker Setup (Recommended)

The easiest way to run the application:

```bash
# Clone the repository
git clone https://github.com/Saiteja1718/diet-recommendation-system.git
cd diet-recommendation-system

# Start with Docker Compose
docker-compose up -d --build

# Access the application
# Frontend: http://localhost:8501
# API Docs: http://localhost:8080/docs
```

### Local Setup

For development or if you prefer running without Docker:

#### 1. Clone the Repository

```bash
git clone https://github.com/Saiteja1718/diet-recommendation-system.git
cd diet-recommendation-system
```

#### 2. Set Up Backend

```bash
cd FastAPI_Backend

# Install dependencies
pip install -r requirements.txt

# Start the API server
python -m uvicorn main:app --host 0.0.0.0 --port 8080
```

#### 3. Set Up Frontend (New Terminal)

```bash
cd Streamlit_Frontend

# Install dependencies
pip install -r requirements.txt

# Start the Streamlit app
python -m streamlit run Hello.py --server.port 8501
```

#### 4. Access the Application

- **Frontend:** http://localhost:8501
- **API Documentation:** http://localhost:8080/docs
- **API Health Check:** http://localhost:8080/

---

## 🚀 Usage

### 1. Diet Recommendation (Personalized Plans)

Perfect for getting a complete daily meal plan based on your profile:

1. Navigate to **💪 Diet Recommendation**
2. Enter your details:
   - Age, height, weight
   - Gender and activity level
   - Weight goal (maintain, lose, gain)
   - Daily budget
3. Click **Generate**
4. Review your personalized meal plan with:
   - BMI calculation
   - Calorie recommendations
   - Recipe suggestions for each meal
   - Shopping list

### 2. Custom Food Recommendation (Recipe Search)

For finding specific recipes matching your nutritional needs:

1. Navigate to **🔍 Custom Food Recommendation**
2. Adjust nutritional sliders:
   - Calories, protein, carbs, fats, etc.
3. (Optional) Specify ingredients
4. Set budget per recipe
5. Click **Generate**
6. Browse recipes with:
   - Nutritional breakdown
   - Cost estimates
   - Cooking instructions

### 3. Meal Planner (Weekly Planning)

For comprehensive weekly meal planning:

1. Navigate to **🍽️ Meal Planner**
2. Answer guided questions:
   - Health goals
   - Daily calories
   - Meals per day
   - Dietary restrictions
   - Preferred cuisines
   - Budget
   - Planning duration
3. Get your complete meal plan with:
   - Daily meal breakdowns
   - Shopping list
   - Budget tracking
   - Recipe details

### 4. Chat Assistant

Get instant answers to nutrition questions:

- **Quick Response Mode** (Default): Instant FAQ answers
- **AI Chat Mode** (Toggle): Personalized AI responses
- Ask about:
  - Ingredient substitutions
  - Cooking tips
  - Nutrition advice
  - Meal prep strategies
  - Budget tips

---

## 📁 Project Structure

```
diet-recommendation-system/
├── 📂 FastAPI_Backend/          # API server
│   ├── main.py                  # FastAPI application
│   ├── model.py                 # ML recommendation engine
│   ├── requirements.txt         # Backend dependencies
│   └── Dockerfile              # Backend container config
│
├── 📂 Streamlit_Frontend/       # Web interface
│   ├── Hello.py                # Welcome page
│   ├── style.css               # Custom styling
│   ├── llm_chat_optimized.py   # Chat system
│   ├── Generate_Recommendations.py  # API client
│   ├── shopping_list_generator.py   # Shopping list logic
│   ├── 📂 pages/               # Application pages
│   │   ├── 1_💪_Diet_Recommendation.py
│   │   ├── 2_🔍_Custom_Food_Recommendation.py
│   │   └── 3_🍽️_Meal_Planner.py
│   ├── 📂 .streamlit/          # Streamlit config
│   │   └── config.toml         # Theme settings
│   ├── requirements.txt        # Frontend dependencies
│   └── Dockerfile             # Frontend container config
│
├── 📂 Data/                    # Dataset files
│   └── dataset.csv.gz         # Compressed recipe database
│
├── 📂 Assets/                  # Images and icons
├── 📂 Docs/                    # Documentation
├── docker-compose.yml          # Multi-container setup
├── requirements.txt            # Root dependencies
└── README.md                   # This file
```

---

## 🧠 How It Works

### Content-Based Filtering

The system uses **content-based filtering** to match recipes to user preferences:

1. **Feature Extraction**: Each recipe is represented by nutritional values
2. **User Profile**: User preferences create a target nutrition vector
3. **Similarity Calculation**: Cosine similarity measures recipe-user match
4. **Ranking**: Recipes ranked by similarity score
5. **Filtering**: Budget, dietary restrictions, and preferences applied

### Cosine Similarity Formula

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

Where:
- **A** = User's target nutrition vector
- **B** = Recipe's nutrition vector
- **θ** = Angle between vectors (smaller = more similar)

### Nearest Neighbors Algorithm

Uses scikit-learn's `NearestNeighbors` with:
- **Algorithm**: Brute force (optimal for small-medium datasets)
- **Metric**: Cosine similarity
- **n_neighbors**: Configurable (default: 5-300 based on filters)

---

## 📊 Dataset

### Source
[Food.com Recipes and Reviews](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews) from Kaggle

### Statistics
- **500,000+** recipes
- **1,400,000+** user reviews
- **Nutritional Information**: Calories, protein, carbs, fats, vitamins, minerals
- **Recipe Details**: Ingredients, instructions, cook time, prep time
- **Metadata**: Cuisine type, difficulty, servings

### Features Used
- Calories
- Fat Content
- Saturated Fat
- Cholesterol
- Sodium
- Carbohydrates
- Fiber
- Sugar
- Protein
- Ingredients
- Instructions
- Cooking Time

---

## 📚 API Documentation

### Endpoints

#### `GET /`
Health check endpoint

**Response:**
```json
{
  "health_check": "OK"
}
```

#### `POST /predict/`
Get recipe recommendations

**Request Body:**
```json
{
  "nutrition_input": [2000, 50, 10, 100, 400, 250, 25, 30, 80],
  "ingredients": ["chicken", "rice"],
  "params": {
    "n_neighbors": 10,
    "return_distance": false
  }
}
```

**Response:**
```json
{
  "output": [
    {
      "Name": "Chicken Fried Rice",
      "Calories": 450.5,
      "ProteinContent": 28.3,
      "RecipeIngredientParts": ["chicken", "rice", "soy sauce"],
      "RecipeInstructions": ["Step 1...", "Step 2..."],
      "CookTime": "20",
      "PrepTime": "10",
      "TotalTime": "30"
    }
  ]
}
```

### Interactive Documentation

Visit `http://localhost:8080/docs` for Swagger UI with:
- Interactive API testing
- Request/response schemas
- Authentication details
- Example requests

---

## ⚡ Performance Optimizations

### Recent Improvements

1. **Instant Chat Responses**
   - Quick Response mode: < 100ms (vs 10-30s with AI)
   - Smart FAQ system with keyword matching
   - Optional AI mode for complex queries

2. **Caching**
   - Recipe recommendations cached
   - Reduced redundant API calls
   - Faster page loads

3. **UI Enhancements**
   - Modern gradient theme
   - Custom CSS with animations
   - Responsive design
   - Smooth transitions

### Performance Metrics

| Feature | Before | After | Improvement |
|---------|--------|-------|-------------|
| Chat Response | 10-30s | <100ms | **100x faster** |
| Page Load | 3-5s | 1-2s | **2.5x faster** |
| Recipe Search | 2-3s | 1-2s | **1.5x faster** |

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** - Open an issue with details
- 💡 **Suggest features** - Share your ideas
- 📝 **Improve documentation** - Fix typos, add examples
- 🔧 **Submit pull requests** - Fix bugs or add features
- ⭐ **Star the repo** - Show your support!

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Test your changes

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Food.com** - For the comprehensive recipe dataset
- **Kaggle** - For hosting the dataset
- **Streamlit** - For the amazing web framework
- **FastAPI** - For the high-performance API framework
- **Scikit-learn** - For ML algorithms
- **Contributors** - Everyone who has contributed to this project

---

## 📞 Contact & Support

- **Repository**: [github.com/Saiteja1718/diet-recommendation-system](https://github.com/Saiteja1718/diet-recommendation-system)
- **Issues**: [Report Issues](https://github.com/Saiteja1718/diet-recommendation-system/issues)
- **Author**: Sai Teja Dusari

---

<div align="center">

**Made with ❤️ for healthy eating**

⭐ Star this repo if you find it helpful!

[Back to Top](#-diet-recommendation-system)

</div>
