from spinroom.models.model_loader import get_gpt35_response, get_gpt4o_response

def loop_communication(models, tokenizers, initial_message, n_loops):
    responses = []
    responses.append(initial_message)
    for i in range(n_loops):
        for index, model_name in enumerate(models):

            if model_name == "gpt4-o":
                response = get_gpt4o_response("Model " + str(index) + ": " + str(responses))
            elif model_name == "gpt3.5":
                response = get_gpt35_response("Model " + str(index) + ": " + str(responses))

            else:
                input_ids = tokenizers[0].encode(initial_message, return_tensors='pt')
                response_ids = models[0].generate(input_ids)
                response = tokenizers[0].decode(response_ids[0], skip_special_tokens=True)
            responses.append(response)
        print (i, responses)
    return responses
