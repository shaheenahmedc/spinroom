def loop_communication(models, tokenizers, initial_message):
    responses = []
    message = initial_message
    for model, tokenizer in zip(models, tokenizers):
        inputs = tokenizer(message, return_tensors="pt")
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=100,  # Specify the number of tokens to generate
            pad_token_id=tokenizer.eos_token_id  # Set pad_token_id to eos_token_id
        )
        message = tokenizer.decode(outputs[0], skip_special_tokens=True)
        responses.append(message)
    return responses
