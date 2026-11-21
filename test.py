from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
results = tavily_search("Best hotels in India") 
print(results)
res=search_flights("i want to go to Tunisia from France")
print(res)