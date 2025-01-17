# Reddit AI Bot

This project is a Reddit bot that automates posting and commenting on Reddit using AI-generated content. The bot leverages the Reddit API and an AI content generation service to create engaging posts and comments.

## Features

- **Automated Posting**: Schedule daily posts to specific subreddits with AI-generated content.
- **Automated Commenting**: Generate and post comments on recent posts in a subreddit.
- **AI Content Generation**: Uses an AI model to generate post titles, bodies, and comments based on given topics.
- **Streamlit App**: A user-friendly interface to interact with the bot for generating posts, posting to Reddit, commenting, and scheduling tasks.
- **Error Logging**: Logs errors and activities for debugging and monitoring.

## Project Structure

├── bot.py # Main Reddit bot logic

├── scheduler.py # Scheduler for automating posts and comments

├── content_generator.py # AI-based content generation logic

├── config.py # Reddit API authentication setup

├── app.py # Streamlit app for interacting with the bot

├── .env # Environment variables for API keys and credentials

├── bot.log # Log file for bot activities

└── README.md # Project documentation

## Prerequisites

1. **Python 3.10**: Ensure you have Python installed.
2. **PRAW**: Python Reddit API Wrapper for interacting with Reddit.
3. **dotenv**: For managing environment variables.
4. **schedule**: For scheduling tasks.
5. **Streamlit**: For creating the web app interface.
6. **AI API Access**: Requires access to the Groq AI API for content generation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/reddit-ai-bot.git
   cd reddit-ai-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your API keys and credentials:
   ```bash
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USERNAME=your_username
   REDDIT_PASSWORD=your_password
   GROQ_API_KEY=your_groq_api_key
   ```
4. Test the Reddit API connection:
   ```bash
   python config.py
   ```

# Usage

1. **Running the Bot**

   To manually post or comment, run the bot.py file:

```bash
   python bot.py
```

2. **Scheduling Posts and Comments**

   To schedule daily posts and comments, run the bot_scheduler.py file:

```bash
   python bot_scheduler.py
```

3. **Generating Content**

   To test the AI content generation, run the content_generator.py file:

   ```bash
   python content_generator.py
   ```

4. **Running the Streamlit App**

   The project includes a Streamlit app (`app.py`) that provides a user-friendly interface for interacting with the bot. The app allows you to:

   - Generate AI content for Reddit posts.
   - Post AI-generated or custom content to Reddit.
   - Comment on posts in a subreddit.
   - Schedule posts and comments.
   - To run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

**Streamlit App Features**

- Generate Post: Enter a topic and generate a Reddit post with a title and body.
- Post to Reddit: Post the generated content to a specific subreddit.
- Comment on Posts: Automatically comment on recent posts in a subreddit.
- Schedule Posts and Comments: Schedule daily posts and comments to be posted at specific times.

**Streamlit App Interface**

- The app has a sidebar for navigation, allowing you to select features like "Generate Post", "Post to Reddit", "Comment on Posts" and "Schedule Posts".
- Each feature has input fields and buttons to perform the desired actions.

## Logging

    bot.log: Logs activities and errors related to the bot's operations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [PRAW](https://praw.readthedocs.io/) for Reddit API integration.
- [Groq AI](https://groq.com/) for content generation.
- [Schedule](https://schedule.readthedocs.io/) for task scheduling.
- [Streamlit](https://streamlit.io/) for creating the web app interface.
# RedditAIBot
