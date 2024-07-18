import requests

def call_azure_translation_api(text, target_language):
    api_key = 'Copy_and_paste_your_key_from_azure_translator'
    endpoint = 'https://api.cognitive.microsofttranslator.com/translate'
    
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Content-type': 'application/json',
        'Ocp-Apim-Subscription-Region': 'YOUR_REGION'
    }
    
    body = [{
        'text': text
    }]
    
    params = {
        'api-version': '3.0',
        'to': target_language
    }
    
    response = requests.post(endpoint, headers=headers, params=params, json=body)
    response_json = response.json()
    
    return response_json[0]['translations'][0]['text']
