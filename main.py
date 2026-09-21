# Python Scraping & Automation Tool
# Created for automated data processing and task tracking

import json

def process_tasks():
    tasks = [
        {"id": 1, "task": "Learn Python Basics", "status": "Completed"},
        {"id": 2, "task": "Build GitHub Portfolio", "status": "In Progress"},
        {"id": 3, "task": "Freelancing on Mostaql", "status": "Pending"}
    ]
    
    print("=== Automated Data Processing ===")
    for item in tasks:
        print(f"[{item['status']}] Task {item['id']}: {item['task']}")
    
    return json.dumps(tasks, indent=4)

if __name__ == "__main__":
    formatted_data = process_tasks()
    print("\nGenerated JSON Report:")
    print(formatted_data)
