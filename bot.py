import logging
from config import get_reddit_instance
from content_generator import ContentGenerator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='bot.log'
)

class RedditBot:
    def __init__(self):
        self.reddit = get_reddit_instance()
        self.content_generator = ContentGenerator()

    def post_to_reddit(self, subreddit_name, topic):
        """Generates content and posts it to the specified subreddit."""
        try:
            content = self.content_generator.generate_post_content(topic)
            subreddit = self.reddit.subreddit(subreddit_name)
            
            post = subreddit.submit(
                title=content['title'], 
                selftext=content['body']
                )
            
            logging.info(f"Successfully posted to r/{subreddit_name}: {post.url}")
            return post.url
        
        except Exception as e:
            logging.error(f"Error posting to Reddit: {e}")
            return None
    
    def comment_on_post(self, subreddit_name, number_of_posts=5):
        """Comment on recent posts in a subreddit."""
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            for post in subreddit.hot(limit=number_of_posts):
                if not post.stickied:
                    # Generate a comment based on the post's title and content
                    comment_text = self.content_generator.generate_comment(post.title, post.selftext)
                    post.reply(comment_text)
                    logging.info(f"Commented on post '{post.title}': {post.url}")
                    break
        except Exception as e:
            logging.error(f"Error commenting on posts in r/{subreddit_name}: {e}")
    
    
# Test the bot
if __name__ == "__main__":
    bot = RedditBot()
    # Test posting
    post_url = bot.post_to_reddit("test", "machine learning")
    if post_url:
        print(f"Post created successfully: {post_url}")

    # Test commenting
    subreddit_name = "test"
    bot.comment_on_post(subreddit_name)