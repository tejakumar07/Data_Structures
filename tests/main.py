import requests

my_api_key = "sk-kxK668651aa40065911259"

def find_plants(sun, water, inside):
    link = "https://perenual.com/api/species-list"
    my_data = {
        "key": my_api_key,
        "sunlight": sun,
        "watering": water,
        "indoor": inside
    }

    reply = requests.get(link, params=my_data)
    if reply.status_code != 200:
        print("❌ Oops! Error:", reply.status_code, reply.text)
        return

    all_data = reply.json()
    plant_list = all_data.get("data", [])

    if not plant_list:
        print("❗ Sorry, no plants found with these choices.")
        return

    print(f"\n🌿 Plants for sunlight = '{sun}', watering = '{water}', indoor = {inside}:\n")
    for p in plant_list:
        print(f"🌱 Name: {p.get('common_name', 'N/A')}")
        print(f"   Science Name: {p.get('scientific_name', 'N/A')}")
        print(f"   Water: {p.get('watering', 'N/A')}")

        sun_info = p.get('sunlight')
        if isinstance(sun_info, list):
            sun_text = ', '.join(sun_info)
        else:
            sun_text = str(sun_info) if sun_info else 'N/A'
        print(f"   Sunlight: {sun_text}")

        img_info = p.get('default_image')
        if isinstance(img_info, dict):
            img_url = img_info.get('thumbnail', 'No image')
        else:
            img_url = 'No image'

        print(f"   Picture: {img_url}")
        print("-" * 50)


# ----------------------
# 🌱 Ask the User
# ----------------------

print("👋 Hello! Let's find a plant for you!")

user_sun = input("☀️  Sunlight (full_sun / partial_sun / shade): ").strip()
user_water = input("💧 Watering (frequent / average / minimum): ").strip()
user_indoor = input("🏠 Is it indoor? (true / false): ").strip().lower()

# Fix indoor if wrong
if user_indoor not in ["true", "false"]:
    print("⚠️  Hmm, not sure what you meant. I'll just use 'true' for now.")
    user_indoor = "true"

# Call the plant finder
find_plants(sun=user_sun, water=user_water, inside=user_indoor)
