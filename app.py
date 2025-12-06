from flask import Flask, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Load environment variables
GENAI_KEY = os.getenv("GENAI_KEY")

client = genai.Client(api_key=GENAI_KEY)

google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

class USSDResponse:
    def __init__(self, session_id=None, user_id=None, msisdn=None, message=None, continue_session=False):
        self.sessionID = session_id
        self.userID = user_id
        self.msisdn = msisdn
        self.message = message
        self.continueSession = continue_session

def get_gemini_verdict(user_query):

    prompt = f"""
    Fact check this claim in the Nigerian context: "{user_query}"
    Output strictly in this format: VERDICT (True/False/Unverified): Short explanation (Source).
    Keep it under 140 chars for SMS.
    """
    
    try:
        #Use 'client.models.generate_content'
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[google_search_tool], # Pass the tool here
                response_modalities=["TEXT"] # Ensure we get text back
            )
        )
        return response.text.strip()
        
    except Exception as e:
        error_msg = str(e)
        print(f"API ERROR: {error_msg}")
        
        if "429" in error_msg:
            return "System busy (Rate Limit). Please try again in 10s."
        else:
            return "Service temporarily unavailable. Try again."

@app.route('/')
def index():
    return "USSD Fact-Checking Service is running."

@app.route('/ussd', methods=['POST'])
def ussd_handler():
    #GET JSON DATA (Safe handling)
    ussd_request = request.get_json(silent=True) or request.values
    
    ussd_response = USSDResponse(
        session_id=ussd_request.get('sessionID'),
        user_id=ussd_request.get('userID'),
        msisdn=ussd_request.get('msisdn')
    )

    user_data = str(ussd_request.get('userData', '')).strip()
    
    # Logic to detect new session (Arkesel specific)
    is_new_session = ussd_request.get('newSession') 
    if is_new_session is None:
        is_new_session = (user_data == "" or user_data == "*928*9#")

    if is_new_session:
        ussd_response.message = "CONFAM\n \n1. Check a Fact\n2. Report Fake News"
        ussd_response.continueSession = True
        
    elif user_data == '1':
        ussd_response.message = "Enter a keyword (e.g. Vaccine, Tax):"
        ussd_response.continueSession = True
        
    elif user_data == '2':
        ussd_response.message = "Type the fake news to report:"
        ussd_response.continueSession = True
        
    else:
        # AI SEARCH
        result = get_gemini_verdict(user_data)
        ussd_response.message = result
        ussd_response.continueSession = False

    return jsonify(vars(ussd_response))

if __name__ == '__main__':
    app.run(port=5000, debug=True)