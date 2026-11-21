import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from backend import run_travel_agent
user_input=input("Enter your travel query: ")
resultat=run_travel_agent(
    user_input=user_input, thread_id="test_thread")
print("\n FINAL RESPONSE \n ")
print(resultat["answer"])