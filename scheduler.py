import schedule
import time
import logging
from bot import RedditBot
from threading import Thread

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot_schedule.log'
)

class BotScheduler:
    def __init__(self):
        self.bot = RedditBot()
        self.running = False  # Flag to control the scheduler thread

    def schedule_post(self, subreddit, topic, time_str):
        """Schedule a daily post."""
        schedule.every().day.at(time_str).do(
            self.bot.post_to_reddit, subreddit, topic
        )
        logging.info(f"Scheduled post for r/{subreddit} at {time_str} with topic '{topic}'.")

    def schedule_comment(self, subreddit, time_str):
        """Schedule a daily comment."""
        schedule.every().day.at(time_str).do(
            self.bot.comment_on_post, subreddit
        )
        logging.info(f"Scheduled comment for r/{subreddit} at {time_str}.")

    def run_scheduler(self):
        """Run the scheduler in a loop."""
        self.running = True
        while self.running:
            try:
                schedule.run_pending()
                time.sleep(1)  # Check for scheduled tasks every second
            except Exception as e:
                logging.error(f"Scheduler error: {str(e)}")
                time.sleep(5)  # Wait 5 seconds if there's an error

    def start(self):
        """Start the scheduler in a background thread."""
        thread = Thread(target=self.run_scheduler, daemon=True)
        thread.start()
        logging.info("Scheduler started in the background.")

    def stop(self):
        """Stop the scheduler."""
        self.running = False
        logging.info("Scheduler stopped.")

# Test the scheduler
if __name__ == "__main__":
    scheduler = BotScheduler()
    # Schedule a post and a comment
    scheduler.schedule_post("test", "machine learning questions ", "12:56")
    scheduler.schedule_comment("test", "12:57")
    print("Scheduler started. Press Ctrl+C to exit.")
    scheduler.run_scheduler()