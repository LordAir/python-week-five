from datetime import datetime
import re

class Tweet:
    """Base class representing a standard tweet"""
    
    def __init__(self, author, content, timestamp=None):
        self.author = author
        self._content = self._validate_content(content)  # Encapsulated attribute
        self.timestamp = timestamp or datetime.now()
        self.likes = 0
        self.retweets = 0
        self._is_pinned = False  # Protected attribute
    
    def _validate_content(self, content):
        """Private method for content validation"""
        if len(content) > 280:
            raise ValueError("Tweet cannot exceed 280 characters")
        return content
    
    def display(self):
        """Public method to display tweet"""
        print(f"{self.author} (@{self.author.lower().replace(' ', '_')})")
        print(f"{self._content}")
        print(f"🕒 {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"❤️ {self.likes} | 🔄 {self.retweets}")
        if self._is_pinned:
            print("📌 Pinned Tweet")
    
    def like(self):
        """Method to increment likes"""
        self.likes += 1
        print(f"Liked by someone! Total likes: {self.likes}")
    
    def retweet(self):
        """Method to increment retweets"""
        self.retweets += 1
        print(f"Retweeted by someone! Total retweets: {self.retweets}")
    
    def pin(self):
        """Method to pin tweet"""
        self._is_pinned = True
        print("Tweet pinned to profile!")
    
    def edit_content(self, new_content):
        """Method demonstrating encapsulation"""
        self._content = self._validate_content(new_content)
        print("Tweet content updated!")


class PollTweet(Tweet):
    """Subclass representing a tweet with a poll"""
    
    def __init__(self, author, content, options, duration_hours=24):
        super().__init__(author, content)
        self.poll_options = options
        self.votes = {option: 0 for option in options}
        self.poll_end = datetime.now() + timedelta(hours=duration_hours)
    
    def display(self):
        """Override display method to show poll"""
        super().display()
        print("\nPoll Options:")
        for i, option in enumerate(self.poll_options, 1):
            print(f"{i}. {option} - {self.votes[option]} votes")
        print(f"⏰ Poll ends: {self.poll_end.strftime('%Y-%m-%d %H:%M')}")
    
    def vote(self, option_index):
        """New method specific to PollTweet"""
        if datetime.now() > self.poll_end:
            print("This poll has ended!")
            return
        
        if 1 <= option_index <= len(self.poll_options):
            option = self.poll_options[option_index - 1]
            self.votes[option] += 1
            print(f"Voted for '{option}'!")
        else:
            print("Invalid option selected!")


class MediaTweet(Tweet):
    """Subclass representing a tweet with media"""
    
    def __init__(self, author, content, media_url, media_type="image"):
        super().__init__(author, content)
        self.media_url = media_url
        self.media_type = media_type
        self.views = 0
    
    def display(self):
        """Override display method to show media"""
        super().display()
        print(f"\nMedia: [{self.media_type.upper()}] {self.media_url}")
        print(f"👀 Views: {self.views}")
    
    def view(self):
        """New method specific to MediaTweet"""
        self.views += 1
        print(f"Media viewed! Total views: {self.views}")


# Example usage
if __name__ == "__main__":
    print("=== Twitter Simulation ===")
    
    # Create instances
    standard_tweet = Tweet(
        "Jane Doe",
        "Just setting up my Twitter account! #NewHere"
    )
    
    poll_tweet = PollTweet(
        "Tech News",
        "Which smartphone do you prefer?",
        ["iPhone", "Android", "Other"]
    )
    
    media_tweet = MediaTweet(
        "Nature Photography",
        "Beautiful sunset at the beach today 🌅",
        "https://example.com/sunset.jpg",
        "image"
    )
    
    # Demonstrate functionality
    print("\n=== Standard Tweet ===")
    standard_tweet.display()
    standard_tweet.like()
    standard_tweet.retweet()
    standard_tweet.pin()
    
    print("\n=== Poll Tweet ===")
    poll_tweet.display()
    poll_tweet.vote(1)
    poll_tweet.vote(2)
    poll_tweet.display()
    
    print("\n=== Media Tweet ===")
    media_tweet.display()
    media_tweet.view()
    media_tweet.view()
    media_tweet.display()
