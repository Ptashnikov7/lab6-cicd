# Лабораторна робота №6: CI/CD pipeline

**Тема:** Налаштування автоматизованого CI/CD pipeline для Flask API за допомогою GitHub Actions.  
**Виконав:** Пташников Василь, група АІ-235.  
**Модель:** Метод Ньютона (5 семестр).

---

## Опис налаштованого CI/CD процесу

У цьому репозиторії реалізовано автоматичний автоматизований пайплайн через GitHub Actions (конфігурація у файлі `.github/workflows/ci.yml`). 
Він тригериться при кожному коміті у гілку `main`.

### Етапи виконання автоматизації:
1. **Checkout code:** завантаження коду репозиторію на віртуальну машину GitHub.
2. **Set up Python:** конфігурація середовища Python 3.11.
3. **Install dependencies:** автоматичне встановлення Flask із файлу `requirements.txt`.
4. **Lint & Syntax Check:** автоматична перевірка коду програми `main.py` на наявність синтаксичних помилок.
5. **Build Docker Image:** тестова автоматична збірка Docker-образу згідно з інструкціями у `Dockerfile`.

```
                                                                                         

   build-and-test (Success in 42s)                                                                                                                                           
   Set up job                                                                    2s   
   Run actions/checkout@v4                                                       3s   
   Set up Python                                                                 5s   
  Install dependencies                                                         12s   

     run: python -m pip install --upgrade pip                                          
     pip install -r requirements.txt                                              

     Successfully installed flask-3.0.3 Werkzeug-3.0.1 ...                                                                                                                    

  Lint and syntax check                                                         1s   
      run: python -m py_compile main.py                                                                                                                            
    Build Docker Image                                                            15s  
      run: docker build -t lab2-model:latest .                                          
      Sending build context to Docker daemon  24.57kB                                  
      Step 1/7 : FROM python:3.11-slim                                                  
      Successfully named docker.io/library/lab2-model:latest                            
                                                                                         
Post Run actions/checkout@v4                                                  1s   
    Complete job                                                                  0s 
    ```
