from groq import Groq
from pipeline.image_to_data import analyze_image
import time

def image_result_to_response(image):
    """Get summarized insights from image analysis."""
    try:
        yield("-----------Give me a quick second to analyzing the image-----------")
        image_description = analyze_image(image) 
        yield("-----------It Will be quick, another second to create the summarization-----------")

        client = Groq(api_key="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")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": f"Below is extracted data from an image. "
                                    f"Generate a short and structured presentation with bullet points summarizing the insights:\n\n{image_description}"
                        },
                    ],
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.1,
        )
        
        response = chat_completion.choices[0].message.content
        
        displayed_text = ""
        for char in response:
            displayed_text += char
            time.sleep(0.01)  
            yield displayed_text
    
    except Exception as e:
        yield f"Error occurred: {str(e)}"
