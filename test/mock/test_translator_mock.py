from mock import patch
from src.translator import translate_content

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_error_result(mocker):
  mocker.return_value.text = "Error: I can't understand your request."

  assert translate_content("Aquí está su primer ejemplo.") == (False, "")


@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_other_error_result(mocker):
  mocker.return_value.text = "Error: I can't access the data you requested."

  assert translate_content("Aquí está su primer ejemplo.") == (False, "")


@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_malformed_input(mocker):
  mocker.return_value.text = ""
  assert translate_content("Some input that causes failure") == (False, "")


@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_other_uninteligible_input(mocker):
  mocker.return_value.text = "I don't understand your request"

  assert translate_content("$$%%^^&&*skdjhfs*(){}[]:;''\67890 0987654321") == (False, "")