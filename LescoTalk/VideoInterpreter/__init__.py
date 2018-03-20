import numpy as np
import cv2

#Iniciar captura con la camara
cap = cv2.VideoCapture(0)
print_ctr = 1
while(True):
    # captura de cada frame del video
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # Voltear imagen para eliminar vista en espejo
    
    #Extraccion de un cuadro de la imagen para analizar
    cv2.rectangle(frame,(600,300),(400,100),(0,255,0),0)
    crop_img = frame[100:300, 400:600]
    
    # Covertir imagen extraida a escala de grises ademas de eliminar ruido
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray.copy(),(5,5),0)
    
    cv2.imshow("gray", gray) #Muestra imagen en escala de grises
    ret, thresh_img = cv2.threshold(gray,91,255,cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)#filtrado para extraer los bordes
    cv2.imshow("Thresh", thresh_img) #muestra el fltrado
    
    _,contours,_ =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#encuentra todos los contornos del recuadro
    
    # extrae el contorno mas representativo del recuadro
    if len(contours) != 0:
        for c in contours:
            area = cv2.contourArea(c)
            if area > 1000 and area < 20000:
                hull =  cv2.convexHull(c,returnPoints = False)
                defects = cv2.convexityDefects(c,hull)
                for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    start = tuple(c[s][0])
                    end = tuple(c[e][0])
                    far = tuple(c[f][0])
                    cv2.line(crop_img,start,end,[0,255,0],2)
                    cv2.circle(crop_img,far,5,[0,0,255],-1)
                cv2.drawContours(crop_img, [c], -1, (0, 255, 0), 2, cv2.LINE_AA)
    
    #Muestra la imagen con el procesado
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cuando se presiona q se cierra el app
cap.release()
cv2.destroyAllWindows()