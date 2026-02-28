import firebase_admin
from firebase_admin import credentials, firestore
import xml.etree.ElementTree as ET
import sys

# ── HACKATHON CONFIG ──────────────────────────────────────────
# 1. Go to Firebase Console -> Project Settings -> Service Accounts
# 2. Click "Generate New Private Key"
# 3. Save as 'serviceAccountKey.json' in this folder
SERVICE_ACCOUNT_PATH = 'serviceAccountKey.json'
OSM_FILE_PATH = 'map.osm'

def seed_toilets():
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        print("Please ensure 'serviceAccountKey.json' exists.")
        return

    db = firestore.client()
    collection_ref = db.collection('community_toilets')

    print(f"Parsing {OSM_FILE_PATH}...")
    try:
        tree = ET.parse(OSM_FILE_PATH)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing OSM file: {e}")
        return

    count = 0
    # Parse nodes with amenity=toilets
    for node in root.findall('node'):
        tags = {tag.get('k'): tag.get('v') for tag in node.findall('tag')}
        
        if tags.get('amenity') == 'toilets':
            doc_data = {
                'id': f"osm_{node.get('id')}",
                'lat': float(node.get('lat')),
                'lng': float(node.get('lon')),
                'name': tags.get('name', 'Public Toilet'),
                'fee': tags.get('fee', 'no'),
                'is_osm_source': True,
                'rating_avg': 0,
                'review_count': 0
            }
            
            # Use node ID as document ID to prevent duplicates
            collection_ref.document(doc_data['id']).set(doc_data)
            count += 1
            if count % 10 == 0:
                print(f"Uploaded {count} toilets...")

    print(f"Success! Seeded {count} toilets from OSM to Firebase Firestore.")

if __name__ == "__main__":
    seed_toilets()
