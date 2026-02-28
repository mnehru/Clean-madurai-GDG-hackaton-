# 🌿 Clean Madurai | Project Pulse

**A unified digital ecosystem for a cleaner, smarter, and more sustainable Madurai.**

The **Clean Madurai** project is a comprehensive suite of civic tools designed to empower citizens through actionable data. By integrating real-time tracking, community verification, and advanced mapping, we aim to bridge the gap between urban infrastructure and citizen needs.

---

## 🚀 Ecosystem Modules

### 📍 Madurai Pulse: Garbage Hotspots Finder
A high-energy monitoring dashboard that leverages civic data and smart analytics to identify urban waste bottlenecks.
*   **Identify**: Locate chronic garbage dumping areas in real-time.
*   **Analyze**: Visualize the "pulse" of city cleanliness to prioritize cleaning efforts.
*   **Collaborate**: Connect data insights with city management for faster resolution.

### 🚻 Advanced Toilet Finder
A community-driven map application designed to eliminate public urination by making quality restrooms easily discoverable.
*   **Search Radius**: Optimized 20km discovery range around your location.
*   **Community Verified**: Users can add new locations and rate existing facilities.
*   **Real-time Navigation**: One-tap directions to the nearest verified facility.
*   **Robust Coverage**: Merges OpenStreetMap (OSM) data with real-time community contributions via Firebase.

---

## ✨ Key Features

*   **Premium User Experience**: Modern, dark-themed portal with a focus on ease of use and visual clarity.
*   **Ecosystem Integration**: A central landing page serves as the gateway to all Clean Madurai initiatives.
*   **Crowdsourced Accuracy**: Citizen-led data entry ensures the information remains current and reliable.
*   **Smart Fallbacks**: Advanced API handling ensures the map works even in low-connectivity or rate-limited scenarios.

---

## 🛠️ Deployment & Setup

To deploy this ecosystem on your own server:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo/clean-madurai.git
    ```
2.  **Configuration**:
    *   Rename `.env.example` to `config.json` (for production) or `.env` (for local).
    *   Add your Firebase API keys and project credentials.
3.  **Permissions**:
    *   Ensure the site is served over **HTTPS** to enable GPS location features.
4.  **Launch**:
    *   Point your web server to `index.html` in the root directory.

---

## 🤝 Contributing to a Cleaner City

We believe in the power of community. You can contribute by:
*   Adding newly identified restrooms to the **Toilet Finder**.
*   Rating existing facilities to maintain high quality standards.
*   Reporting garbage hotspots through the **Madurai Pulse** module.

**Together, we can make Madurai a model for urban cleanliness.**

---



