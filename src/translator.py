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

    language = get_language(content)
    translation = get_translation(content)

    # Check for error response
    error_message = "I'm not able to help with that"
    if (not language
        or not translation
        or language.startswith(error_message)
        or translation.startswith(error_message)
        or language.startswith("Error")
        or translation.startswith("Error")):
        return (False, "")
    
    if "english" in language.lower():
        return True, content
    
    return (False, translation)
