import requests
import json
import os

def get_ed_discussion_brief():
    """
    Scrapes the Ed Discussion API for the latest announcements and posts 
    for specific EPFL courses (Algorithms, ML, Neuro, Systems).
    """
    course_ids = [3013, 2241, 3006, 2987]
    
    # Retrieve token securely from environment variable (DO NOT hardcode keys)
    token = os.environ.get("ED_DISCUSSION_TOKEN")
    if not token:
        print("Error: ED_DISCUSSION_TOKEN environment variable not set.")
        return

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "X-Token": token,
        "Origin": "https://edstem.org"
    }
    
    print("=== 🎓 MORNING BRIEFING : EPFL COURSES ===\n")
    for cid in course_ids:
        try:
            url = f"https://eu.edstem.org/api/courses/{cid}/threads?limit=5&sort=new"
            resp = requests.get(url, headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                threads = data.get("threads", [])
                
                print(f"--- Course ID: {cid} ---")
                for t in threads:
                    status = "📌 [PINNED]" if t.get("is_pinned") else "💬 [NEW]"
                    title = t.get("title", "")
                    print(f"{status} {title}")
                print("\n")
        except Exception as e:
            print(f"Failed to fetch course {cid}: {e}")

if __name__ == "__main__":
    get_ed_discussion_brief()
