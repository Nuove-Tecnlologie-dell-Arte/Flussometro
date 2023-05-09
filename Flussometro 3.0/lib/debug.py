import cv2

def rileva_volto_webcam():
    # Carica il classificatore addestrato per il rilevamento dei volti
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Inizializza la webcam
    webcam = cv2.VideoCapture(0)

    while True:
        # Leggi il frame dalla webcam
        _, frame = webcam.read()

        # Converti il frame in scala di grigi
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Rileva i volti nel frame
        volti = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(30, 30))

        # Disegna i rettangoli intorno ai volti rilevati
        for (x, y, w, h) in volti:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        # Mostra il frame con i volti rilevati
        cv2.imshow('Rilevamento volti', frame)

        # Interrompi il ciclo se viene premuto il tasto 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Rilascia le risorse
    webcam.release()
    cv2.destroyAllWindows()

rileva_volto_webcam()