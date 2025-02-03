from groq import Groq
from utils.encode_image import encode_image_to_base64

def analyze_image(image):
    """Analyze image using Groq's vision model and return response."""
    try:
        base64_image = encode_image_to_base64(image) 
        print("Encoded Image:", base64_image[:100])
        
        client = Groq(api_key="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")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": "Extract all data from the image in table format (columns and rows)."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="llama-3.2-90b-vision-preview",
            temperature=0.1,
        )
        
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error occurred: {str(e)}"
