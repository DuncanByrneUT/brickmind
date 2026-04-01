

# BrickMind 🧱

https://github.com/user-attachments/assets/0de0ee76-480e-4631-ae02-d09bb0a9747f



An AI-powered Lego companion app that generates custom building challenges and recommends official Lego sets based on your interests.

## Features

- **Build Challenge Generator** — select a theme, piece count, and age range and get a unique AI-generated building challenge with step by step tips
- **Set Recommender** — describe what you're into and get personalized official Lego set recommendations with prices and difficulty levels
- Built with a fun, colorful Lego-inspired UI

## Tech Stack

- **Python** / **Flask** — backend web server and routing
- **Anthropic Claude API** — AI challenge generation and set recommendations
- **HTML / CSS / JavaScript** — colorful Lego-themed frontend
- **Prompt Engineering** — custom Claude personalities for on-brand AI responses

## Getting Started

1. Clone the repo
```
   git clone https://github.com/DuncanByrneUT/brickmind.git
   cd brickmind
```

2. Create and activate a virtual environment
```
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies
```
   pip3 install flask anthropic python-dotenv
```

4. Create a `.env` file in the root directory and add your Anthropic API key
```
   ANTHROPIC_API_KEY=your-api-key-here
```

5. Run the app
```
   python3 app.py
```

6. Open your browser and go to `http://127.0.0.1:5000`

## Usage

- **Build Challenge** — pick a theme like Space, WWE Wrestling, or Video Games, select your piece count and age range, and hit Generate Challenge
- **Set Recommender** — type in your interests and hobbies and get 3 official Lego set recommendations tailored to you
