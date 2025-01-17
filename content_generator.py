import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
    def generate_post_content(self, topic):
        """Generate a Reddit post about a given topic."""
        # Refined prompt to limit the output to only title and body
        prompt = f"""Generate an engaging Reddit post about "{topic}" in layman's terms.
        The post should include:
        1. A catchy title (on a single line).
        2. A well-written body (up to 300 words) that is informative, easy to understand, and conversation-starting.
        Do not include anything else in the response.""" 
        
        response = self.groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="mixtral-8x7b-32768",
            temperature=0.7,
        )
        generated_text = response.choices[0].message.content
        try:
            title, body = generated_text.split('\n', 1)
            return {
                "title": title.strip(), 
                "body": body.strip()
                }
        
        except ValueError:
            # If splitting fails, return a fallback response
            return {
                'title': "AI Generated Post",
                'body': generated_text.strip()
            }
    def generate_comment(self, post_title, post_content):
        """Generate a relevant comment based on the post title and content."""
        prompt = f"""Write a short, engaging comment for a Reddit post.
        The post is titled: "{post_title}" and its content is: "{post_content}".
        The comment should be relevant, insightful, and encourage further discussion."""

        response = self.groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="mixtral-8x7b-32768",
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()    
        
        
# Test the content generation
if __name__ == "__main__":
    generator = ContentGenerator()
    post_content = generator.generate_post_content("machine learning")
    print("Generated Title:", post_content['title'])
    print("\nGenerated Body:", post_content['body'])

    comment = generator.generate_comment(post_content['title'], post_content['body'])
    print("\nGenerated Comment:", comment)