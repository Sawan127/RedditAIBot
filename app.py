import streamlit as st
from content_generator import ContentGenerator
from bot import RedditBot
from scheduler import BotScheduler
from datetime import datetime

# Initialize the ContentGenerator
generator = ContentGenerator()
reddit_bot = RedditBot()
scheduler = BotScheduler()

# Start the scheduler in the background
if "scheduler_started" not in st.session_state:
    scheduler.start()
    st.session_state["scheduler_started"] = True
    
# Step 1: Basic Streamlit App with Larger Font Sizes
st.markdown(
    """
    <h1 style='text-align: center; font-size: 50px;'>Reddit AI Bot</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style='text-align: center; font-size: 20px;'>
    Welcome to the Reddit AI Bot Streamlit App!<br>
    This app allows you to generate posts, post to Reddit, comment on posts, and schedule tasks.
    </p>
    """,
    unsafe_allow_html=True,
)



# Sidebar for navigation
st.sidebar.header("Reddit AI Bot Features")
feature = st.sidebar.selectbox("Choose a feature:", ["Generate Post", "Post to Reddit", "Comment on Posts", "Schedule Posts"])

# Feature: Generate Post
if feature == "Generate Post":
    st.header("Generate a Reddit Post")
    topic = st.text_input("Enter a topic:", value="machine learning")

    if st.button("Generate Post"):
        with st.spinner("Generating post..."):
            try:
                # Generate the post content
                post_content = generator.generate_post_content(topic)
                st.success("Post generated successfully!")
                st.write("### Generated Title")
                st.write(post_content['title'])
                st.write("### Generated Body")
                st.write(post_content['body'])
            except Exception as e:
                st.error(f"Error generating post: {e}")

# Feature: Post to Reddit
elif feature == "Post to Reddit":
    st.header("Post to Reddit")
    subreddit = st.text_input("Enter the subreddit name:", value="test")
    topic = st.text_input("Enter a topic for the post:", value="machine learning")

    if st.button("Post to Reddit"):
        with st.spinner("Posting to Reddit..."):
            try:
                # Post to Reddit
                post_url = reddit_bot.post_to_reddit(subreddit, topic)
                if post_url:
                    st.success(f"Post created successfully! [View Post]({post_url})")
                else:
                    st.error("Failed to create the post.")
            except Exception as e:
                st.error(f"Error posting to Reddit: {e}")

# Feature: Comment on Posts
elif feature == "Comment on Posts":
    st.header("Comment on Posts")
    subreddit = st.text_input("Enter the subreddit name:", value="test")
    number_of_posts = st.slider("Number of posts to comment on:", min_value=1, max_value=10, value=5)

    if st.button("Comment on Posts"):
        with st.spinner("Commenting on posts..."):
            try:
                # Comment on posts in the subreddit
                reddit_bot.comment_on_post(subreddit, number_of_posts)
                st.success(f"Successfully commented on {number_of_posts} posts in r/{subreddit}.")
            except Exception as e:
                st.error(f"Error commenting on posts: {e}")
                
# Feature: Schedule Posts and Comments
elif feature == "Schedule Posts":
    st.header("Schedule Posts and Comments")
    st.write("Use this feature to schedule daily posts and comments.")

    # Input fields for scheduling posts
    subreddit = st.text_input("Enter the subreddit name:", value="test")
    topic = st.text_input("Enter a topic for the post:", value="machine learning")
    post_time_str_12hr = st.text_input("Enter the time to post (HH:MM AM/PM):", value="08:00 AM")

    # Input fields for scheduling comments
    comment_time_str_12hr = st.text_input("Enter the time to comment (HH:MM AM/PM):", value="08:02 AM")

    if st.button("Schedule Post and Comment"):
        with st.spinner("Scheduling tasks..."):
            try:
                # Convert 12-hour format to 24-hour format
                
                post_time_24hr = datetime.strptime(post_time_str_12hr, "%I:%M %p").strftime("%H:%M")
                comment_time_24hr = datetime.strptime(comment_time_str_12hr, "%I:%M %p").strftime("%H:%M")

                # Schedule the post and comment
                scheduler.schedule_post(subreddit, topic, post_time_24hr)
                scheduler.schedule_comment(subreddit, comment_time_24hr)

                st.success(f"Post scheduled successfully for {post_time_str_12hr} in r/{subreddit}.")
                st.success(f"Comment scheduled successfully for {comment_time_str_12hr} in r/{subreddit}.")
            except ValueError:
                st.error("Invalid time format. Please use HH:MM AM/PM (e.g., 08:00 AM).")
            except Exception as e:
                st.error(f"Error scheduling tasks: {e}")

    st.write("The scheduler will run in the background to execute the scheduled tasks.")