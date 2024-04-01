from vertexai.preview.language_models import ChatModel, InputOutputTextPair

chat_model = ChatModel.from_pretrained("chat-bison@001")
context1 = "Please respond with a translation of the input text to english." # TODO: Insert context
context2 = "Please classify what language the input text is written in."


def get_translation(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #

    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    } 

     # ---------------- YOUR CODE HERE ---------------- #
    chat = chat_model.start_chat(context=context1)
    response = chat.send_message(post, **parameters)
    if response.is_blocked:
        return ""
    return response.text
    
def get_language(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #
    
    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

     # ---------------- YOUR CODE HERE ---------------- #
    chat = chat_model.start_chat(context=context2)
    response = chat.send_message(post, **parameters)
    return response.text

def translate_content(content: str) -> tuple[bool, str]:
    if content == '':
        return True, content
    if "english" in get_language(content).lower():
        return True, content
    
    return (False, get_translation(content))
