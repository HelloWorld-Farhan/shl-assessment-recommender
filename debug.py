import traceback
from models import ChatRequest, Message
from agent import generate_response

req = ChatRequest(messages=[Message(role="user", content="Test")])
try:
    generate_response(req)
except Exception as e:
    traceback.print_exc()
