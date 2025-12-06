# Confam 🇳🇬 ✅
> "Don't just believe it. Dial it. Confam it."

**Confam** is an AI-powered USSD fact-checking tool designed to democratize access to the truth for offline users in Nigeria. By combining the accessibility of USSD with the intelligence of Google Gemini, we empower anyone with a basic feature phone to verify news, rumors, and health claims instantly—no internet required.

---

## 🚀 Live Demo (How to Test)

Since this is a USSD application, you cannot "visit" the website. You must simulate a phone call using the **Arkesel Simulator**.

The best experience is on the native mobile simulator.

1.  **Download the App:** Install the [Arkesel USSD Simulator](https://play.google.com/store/apps/details?id=com.arkesel.mobile.simulator) from the Google Play Store.
2.  **Configure:**
    * Open the app.
    * Tap the **+ (Plus)** button to add a new connection.
    * **Phone Number:** Enter any random number (e.g., `233541234567`), if this takes time, use a Ghanian Number.
    * **Callback URL:** Paste this link exactly:
        `https://confam-five.vercel.app/ussd`
    * Tap **Save**.
3.  **Test:**
    * Tap on the connection you just created.
    * Dial any code (e.g., `*920#` or `*384*1#`).
    * Press **Send**.
    * *Voila! You are now chatting with Confam.*

---

## ⚡ Key Features

* **Offline Accessibility:** Works on any GSM phone; no internet or smartphone required.
* **AI-Powered Verification:** Uses **Google Gemini 2.0 Flash** to analyze claims against a live knowledge base.
* **Context Aware:** specifically tuned for **Nigerian context** (e.g., understands "Tinubu", "Naira", "Lagos Traffic").
* **Rate Limit Handling:** Intelligent error handling that prevents crashes during high traffic.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **AI Engine:** Google Gemini 2.5 Flash (via `google-genai` SDK)
* **Search Grounding:** Google Search Tool (built-in RAG)
* **USSD Gateway:** Arkesel
* **Hosting:** Vercel

---

## 🏃 Local Development Setup

If you want to run this locally:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/yourusername/confam.git](https://github.com/yourusername/confam.git)
    cd confam
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    Create a `.env` file and add your Google Gemini API Key:
    ```bash
    GENAI_KEY="your_api_key_here"
    ```

4.  **Run the Server:**
    ```bash
    python app.py
    ```

5.  **Expose to Internet:**
    Use ngrok to make your localhost visible to the simulator:
    ```bash
    ngrok http 5000
    ```

---

**Built with ❤️ by Raheem for the Primetech Hackathon**
