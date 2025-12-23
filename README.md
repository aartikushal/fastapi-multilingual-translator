# 🌍 Language Translation API using FastAPI & Gemini AI

A lightweight and scalable **Language Translation API** built using **FastAPI** and **Google Gemini AI**, designed to translate text between different languages via a simple REST interface.

---

## 📌 Project Overview

This project exposes a RESTful API endpoint that accepts input text along with source and target languages, and returns an AI-generated translation using **Gemini 2.0 Flash**.

The API is fast, easy to integrate, and suitable for applications such as:
- Multilingual platforms
- Chatbots
- Content localization tools
- Enterprise translation services

---

## 🚀 Key Features

- ⚡ High-performance REST API using FastAPI  
- 🤖 AI-powered translations with Google Gemini  
- 🌐 Supports multiple language pairs  
- 📦 Clean request & response schema using Pydantic  
- 🔐 API key-based authentication for Gemini  
- 🧪 Easy to test using Postman or Swagger UI  

---

## 🏗 Architecture Flow

1. Client sends a POST request with text and language details  
2. API constructs a translation prompt  
3. Request is sent to Gemini Generative Language API  
4. Gemini processes and returns translated content  
5. API extracts and returns the translated text as JSON  

---

## 📥 API Endpoint

### **POST** `/translate`

#### Request Body
- `text` – Text to be translated  
- `source_lang` – Source language (e.g., English)  
- `target_lang` – Target language (e.g., French)  

#### Response
- `translated_text` – AI-generated translated output  

---

## 🛠 Technologies Used

- **Python**
- **FastAPI**
- **Pydantic**
- **Google Gemini AI**
- **Requests**
- **Uvicorn**

---

## 🔐 Security Note

The Gemini API key is required for translation requests.  
For production usage, it is recommended to store the API key securely using **environment variables** instead of hardcoding.

---

## 📂 Project Structure



---

## 🧪 Testing & Documentation

- Interactive API documentation available via **Swagger UI**
- Easily testable using **Postman**, **curl**, or browser-based tools
- FastAPI automatically generates OpenAPI documentation

---

## 📈 Use Cases

- Real-time language translation services  
- Multilingual chat applications  
- AI-powered customer support  
- Content localization pipelines  
- Educational language tools  

---

## 🔮 Future Enhancements

- Batch translation support  
- Language auto-detection  
- Authentication & rate limiting  
- Logging & monitoring  
- Support for additional Gemini models  

---

## ✅ Conclusion

This project demonstrates how **FastAPI** and **Generative AI** can be combined to build a fast, scalable, and production-ready translation service.  
It serves as a strong foundation for enterprise-grade multilingual applications.

---

⭐ If you find this project useful, consider starring the repository!
