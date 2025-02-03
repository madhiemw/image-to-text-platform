import gradio as gr
from pipeline.image_result_to_summary import image_result_to_response

with gr.Blocks() as demo:
    gr.Markdown("Muhammad Adhiem Wicaksana's Image to Description project")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="numpy", label="Upload Image", sources=["upload"]) 
            analyze_button = gr.Button("Analyze Image")
        
        with gr.Column():
            output_text = gr.Textbox(label="Analysis Result", lines=50, max_lines=50)
    
    analyze_button.click(
        fn=image_result_to_response,
        inputs=[image_input],
        outputs=output_text,
        api_name="analyze"
    )

if __name__ == "__main__":
    demo.launch()
