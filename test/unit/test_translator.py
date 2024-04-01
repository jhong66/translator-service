from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert "this is a chinese message" in translated_content.lower()

def test_spanish():
    is_english, translated_content = translate_content("Este es un mensaje Español")
    assert is_english == False
    assert "this is a spanish message" in translated_content.lower()

def test_english():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert "This is an English message" == translated_content

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("adsfiagsdafjeoigh")
    assert is_english == True
    assert "adsfiagsdafjeoigh" in translated_content.lower()