import asyncio
import json
from browser_use import Agent, Browser, BrowserConfig, Controller
from langchain_openai import ChatOpenAI

from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    post_text: str
    url: str

class Posts(BaseModel):
    posts: List[Post]

async def main():
    # Create the language model interface
    llm = ChatOpenAI(model="gpt-4o-mini")
    
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    initial_actions = [
        {'open_tab': {'url': 'https://www.x.com/apify'}},
    ]
    
    browser = Browser(
        config=BrowserConfig(
            browser_binary_path=chrome_path
        )
    )
    
    controller = Controller(output_model=Posts)

    # Define the browser agent with the LLM
    agent = Agent(
        task = "Retrieve the text and post URL of the 3 most recent posts.",
        llm = llm,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions
    )

    # Ask the agent to perform a task
    result = await agent.run()
    await browser.close()
    
    posts_list = []
    try:
        final_result = result.final_result()
        # Notice: final_result() is a method call, not an attribute access
        if final_result:
            parsed: Posts = Posts.model_validate_json(final_result)
        print(f"Retrieved {len(parsed.posts)} posts")
        
        for post in parsed.posts:
            posts_list.append({
                "post_text": post.post_text,
                "url": post.url
            })
        
        file_name = "posts.json"
        with open(file_name, 'w') as f:
            json.dump(posts_list, f, indent=4)
            
        print(f"Saved results to {file_name}")
    
    except Exception as e:
        print(f"Error processing results: {e}")

# Run the async main function
if __name__ == '__main__':
    asyncio.run(main())