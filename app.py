import gradio as gr
from models.model_loader import load_model
from topologies.loop_communication import loop_communication
from topologies.broadcast_communication import broadcast_communication

# Define available models and topologies
MODEL_NAMES = ["gpt2", "EleutherAI/gpt-neo-2.7B"]
TOPOLOGIES = {
    "Loop Communication": loop_communication,
    "Broadcast Communication": broadcast_communication
}

def debate(num_models, topology_name, initial_message):
    models = []
    tokenizers = []
    for i in range(num_models):
        model, tokenizer = load_model(MODEL_NAMES[i % len(MODEL_NAMES)])
        models.append(model)
        tokenizers.append(tokenizer)

    topology = TOPOLOGIES[topology_name]
    responses = topology(models, tokenizers, initial_message)
    return responses

with gr.Blocks() as demo:
    gr.Markdown("# LLM Debate App")
    num_models = gr.Slider(2, 4, step=1, label="Number of Models")
    topology = gr.Dropdown(list(TOPOLOGIES.keys()), label="Communication Topology")
    initial_message = gr.Textbox(label="Initial Message")
    debate_button = gr.Button("Start Debate")
    output = gr.Textbox(label="Debate Responses")

    debate_button.click(debate, inputs=[num_models, topology, initial_message], outputs=output)

demo.launch()
