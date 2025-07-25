Распознавание марок автомобилей

Этот проект позволяет распознавать марки автомобилей (Ferrari, Mercedes, Renault) с помощью готовой нейронной сети с точностью не менее 85%. Вы можете использовать модель model_avto.h5 для предсказаний без обучения. В проекте есть скрипт для предсказания, тестовые изображения и архив для демо-панели.

Что включено:
- model_avto.h5: Готовая модель (скачивается с Google Drive). https://drive.google.com/file/d/1O6Z4TFgsm0VWnBMHb7lP32HPf00g61UC/view?usp=drive_link
- script.py: Скрипт для предсказания марки по изображению.
- label.txt: Метки классов (Ferrari, Mercedes, Renault).
- 1.png–9.png: Тестовые изображения (по 3 на марку).
- archive.zip: Архив с моделью, скриптом, метками и изображениями.
- Распознавание_марок_автомобилей.ipynb: Код для демонстрации работы.

Требования:
- Google Colab с GPU (включить: Runtime → Change runtime type → GPU).
- Установи библиотеки:
  !pip install tensorflow gdown

Как использовать в Google Colab:

1. Склонируй репозиторий:
   !git clone <URL_репозитория>
   Или загрузи файлы (script.py, label.txt, 1.png–9.png, archive.zip) вручную.

2. Скачай модель:
   Модель model_avto.h5 хранится на Google Drive:
   !gdown https://drive.google.com/uc?id=<1O6Z4TFgsm0VWnBMHb7lP32HPf00g61UC>

3. Распакуй тестовые изображения:
   Если нет файлов 1.png–9.png, распакуй архив:
   !unzip archive.zip

4. Сделай предсказание:
   Запусти скрипт:
   from script import predict
   predict(img_path='1.png', model_path='model_avto.h5')
   Используй 1.png (Ferrari), 4.png (Mercedes), 7.png (Renault) или своё изображение.

5. Свои изображения:
   Загрузи изображение:
   from google.colab import files
   uploaded = files.upload()
   Предскажи:
   predict(img_path='your_image.png', model_path='model_avto.h5')

6. Демо-панель:
   Скачай archive.zip и распакуй:
   !unzip archive.zip
   Архив готов для демо-панели.

Важно:
- Изображения должны быть PNG/JPG, желательно 128x64 пикселя (RGB).
- Если ссылка на модель не работает, проверь репозиторий или напиши в Issues.
- Архив archive.zip включает всё для демо: модель, скрипт, метки, изображения.

О проекте:
- Датасет: Изображения Ferrari, Mercedes, Renault (middle_fmr.zip).
- Модель: Сверточная нейронная сеть (CNN).
- Точность: ≥85% на тесте (341 изображение).

Если что-то не работает, создай Issue на GitHub!
