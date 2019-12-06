import cv2
import numpy as np
from Robot import Robot

class WebCam():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        print("aaaaaaaaaa")
        print(self.cap.get(3))
        print(self.cap.get(3))
        self.robot = Robot('Dolzay')
        #self.cap.set(3, 800) #width
        #self.cap.set(4, 800) #height
    def is_red_circle_detected(self,frame):
        red_area = cv2.inRange(frame, (0,0,0), (100,100,100))
        red_area = cv2.erode(red_area, kernel, iterations=5 )
        red_area = cv2.dilate(red_area, kernel, iterations=9 )
        _,contours, _ = cv2.findContours(red_area.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 1 :
            return True
        return False

    def follow_the_black_line(self,frame) :
        Blackline = cv2.inRange(frame, (0,0,0), (100,100,100))
        kernel = np.ones((3,3), np.uint8)
        Blackline = cv2.erode(Blackline, kernel, iterations=5)
        Blackline = cv2.dilate(Blackline, kernel, iterations=9)
        _,contours, _ = cv2.findContours(Blackline.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours_len = len(contours)
        blackbox = None
        x_last = 320
        y_last = 320
        if contours_len > 0 :
            if contours_len == 1 :
                blackbox = cv2.minAreaRect(contours[0])
            else :
                candidates = []
                off_bottom = 0

                # gather black box candidates
                for cnt in range(contours_len):
                    blackbox = cv2.minAreaRect(contours[cnt])
                    (x_min, y_min), (w_min, h_min), ang = blackbox
                    box = cv2.boxPoints(blackbox)
                    (x_box,y_box) = box[0]
                    if y_box > 648 : # count the number of blackboxs starting from the bottom
                        off_bottom += 1
                    candidates.append((y_box,cnt,x_min,y_min))

                candidates = sorted(candidates)

                # handle the off_bottom blackboxs
                if off_bottom > 1  :
                    candidates_off_bottom = []
                    for cnt in range((contours_len-off_bottom),contours_len) :
                        (y_highest,con_highest,x_min, y_min) = candidates[con_num]
                        total_distance = (abs(x_min - x_last)**2 + abs(y_min - y_last)**2)**0.5
                        canditates_off_bottom.append((total_distance,con_highest))
                    canditates_off_bottom = sorted(candidates_off_bottom)
                    (total_distance,con_highest) = candidates_off_bottom[0]
                    blackbox = cv2.minAreaRect(contours[con_highest])
                else :
                    (y_highest,con_highest,x_min, y_min) = candidates[contours_len-1]
                    blackbox = cv2.minAreaRect(contours[con_highest])
        if blackbox is not None :

            (x_min, y_min), (w_min, h_min), ang = blackbox
            x_last = x_min
            y_last = y_min
            if ang < -45 :
                ang = 90 + ang
            if w_min < h_min and ang > 0:
                ang = (90-ang)*-1
            if w_min > h_min and ang < 0:
                ang = 90 + ang
            setpoint = 320
            error = int(x_min - setpoint)
            ang = int(ang)
            if ang > -5 :
                self.robot.right()
            elif ang < 5 :
                self.robot.left()
            elif ang in range(-5,5) :
                self.robot.forward
            box = cv2.boxPoints(blackbox)
            box = np.int0(box)
            cv2.drawContours(frame,[box],0,(0,0,255),3)
            cv2.putText(frame,str(ang),(10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame,str(error),(10, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.line(frame, (int(x_min),200 ), (int(x_min),250 ), (255,0,0),3)
            cv2.line(frame, (320,0 ), (320,639 ), (0,255,0),3)
        # else  :
        #     robot.rotate_360()
        return frame,Blackline

    def run_cam(self):
        print(self.cap.isOpened())
        while(self.cap.isOpened()) :

            _,frame = self.cap.read()
            if self.ultrason_forward.distance() <= 10 :
                # face detecton
                self.robot.stop()
                is_face == True
                if is_face == True :
                    self.robot.rigth()
                else :
                    self.robot.left()
                time.sleep(2)

            if self.ultrason_right.distance() <= 10 :
                self.robot.sleep()
                time.sleep(2)
            if self.is_red_circle_detected(frame):
                
            frame,Blackline  = self.follow_the_black_line(frame)
            cv2.imshow('Blackline',Blackline)
            cv2.imshow('Frame',frame)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
            # _,frame = cv2.imencode('.jpg', frame)
            # return  frame.tobytes()


    def reload_webcam(self):
        self.cap = cv2.VideoCapture(0)
            # _,frame = cv2.imencode('.jpg', frame)
            # return  frame.tobytes()
