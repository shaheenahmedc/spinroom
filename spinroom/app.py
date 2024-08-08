import gradio as gr
from spinroom.models.model_loader import load_model
from spinroom.topologies.loop_communication import loop_communication
from spinroom.topologies.broadcast_communication import broadcast_communication

# Define available models and topologies
MODEL_NAMES = ["gpt4-o", "gpt3.5", "gpt3.5"]

TOPOLOGIES = {
    "Loop Communication": loop_communication,
    "Broadcast Communication": broadcast_communication
}

def debate(num_models, topology_name, initial_message, n_loops):
    models = []
    tokenizers = []
    for i in range(num_models):
        model_name = MODEL_NAMES[i % len(MODEL_NAMES)]
        model, tokenizer = load_model(model_name)
        if model is None and tokenizer is None:  # Indicates an API-based model
            models.append(model_name)
            tokenizers.append(None)
        else:
            models.append(model)
            tokenizers.append(tokenizer)
    topology = TOPOLOGIES[topology_name]
    responses = topology(models, tokenizers, initial_message, n_loops)
    return responses

def get_response_text(responses, index):
    if index < len(responses):
        return responses[index]
    return ""

def create_response_containers(num_models):
    return [gr.Textbox(label=f"Model {i+1} Response", interactive=False) for i in range(num_models)]

with gr.Blocks() as demo:
    gr.Markdown("# LLM Debate App")

    with gr.Row():
        num_models = gr.Slider(2, 6, step=1, label="Number of Models", value=2)
        n_loops = gr.Slider(2, 10, step=1, label="Number of Loops")
        topology = gr.Dropdown(list(TOPOLOGIES.keys()), label="Communication Topology")
        initial_message = gr.Textbox(label="Initial Message")

    debate_button = gr.Button("Start Debate")

    # Initial creation of response containers
    response_containers = create_response_containers(num_models.value)
    response_column = gr.Column(*response_containers)

    def update_responses(num_models, topology, initial_message, n_loops):
        num_models = int(num_models)  # Ensure num_models is an integer
        responses = debate(num_models, topology, initial_message, n_loops)
        return [gr.update(value=get_response_text(responses, i)) for i in range(num_models)]

    def refresh_response_containers(num_models):
        num_models = int(num_models)  # Ensure num_models is an integer
        new_containers = create_response_containers(num_models)
        response_column.children = new_containers
        return new_containers

    num_models.change(fn=refresh_response_containers, inputs=[num_models], outputs=response_column.children)

    debate_button.click(update_responses, inputs=[num_models, topology, initial_message, n_loops], outputs=response_column.children)

demo.launch()


test = """
This is the log of a debate you're having with some more LLMs.
The question is: in 10 words, should Leyton Orient have gotten the Olympic stadium?
Figure out which model you are by reading who last spoke in the log, then finding your previous responses.
If there is no log, then assume you are the first to speak.
Begin your answer with which LLM you are.
Only give one response, don't continue the conversation.
As you gain more information, try to constructively debate each other, and reach a consensus where possible.
Directly reference the other LLM and their responses.
Start from more extreme ends of the debate spectrum, and begin answers with yes or no.
Assume lively characters, that are suited to the question posed.
[BEGIN_DEBATE]
"""
