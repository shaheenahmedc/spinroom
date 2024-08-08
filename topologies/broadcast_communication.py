def broadcast_communication(models, tokenizers, initial_message):
    responses = []
    for model, tokenizer in zip(models, tokenizers):
        inputs = tokenizer(initial_message, return_tensors="pt")
        outputs = model.generate(inputs.input_ids, max_length=100)
        message = tokenizer.decode(outputs[0], skip_special_tokens=True)
        responses.append(message)
    return responses
