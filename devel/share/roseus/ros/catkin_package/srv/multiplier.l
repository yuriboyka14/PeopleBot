;; Auto-generated. Do not edit!


(when (boundp 'catkin_package::multiplier)
  (if (not (find-package "CATKIN_PACKAGE"))
    (make-package "CATKIN_PACKAGE"))
  (shadow 'multiplier (find-package "CATKIN_PACKAGE")))
(unless (find-package "CATKIN_PACKAGE::MULTIPLIER")
  (make-package "CATKIN_PACKAGE::MULTIPLIER"))
(unless (find-package "CATKIN_PACKAGE::MULTIPLIERREQUEST")
  (make-package "CATKIN_PACKAGE::MULTIPLIERREQUEST"))
(unless (find-package "CATKIN_PACKAGE::MULTIPLIERRESPONSE")
  (make-package "CATKIN_PACKAGE::MULTIPLIERRESPONSE"))

(in-package "ROS")





(defclass catkin_package::multiplierRequest
  :super ros::object
  :slots (_a _b ))

(defmethod catkin_package::multiplierRequest
  (:init
   (&key
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; int32 _a
    4
    ;; int32 _b
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _a
       (write-long _a s)
     ;; int32 _b
       (write-long _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _a
     (setq _a (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _b
     (setq _b (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass catkin_package::multiplierResponse
  :super ros::object
  :slots (_result ))

(defmethod catkin_package::multiplierResponse
  (:init
   (&key
    ((:result __result) 0)
    )
   (send-super :init)
   (setq _result (round __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; int32 _result
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _result
       (write-long _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _result
     (setq _result (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass catkin_package::multiplier
  :super ros::object
  :slots ())

(setf (get catkin_package::multiplier :md5sum-) "a7d7d7065d45755acef7d4dcf908162a")
(setf (get catkin_package::multiplier :datatype-) "catkin_package/multiplier")
(setf (get catkin_package::multiplier :request) catkin_package::multiplierRequest)
(setf (get catkin_package::multiplier :response) catkin_package::multiplierResponse)

(defmethod catkin_package::multiplierRequest
  (:response () (instance catkin_package::multiplierResponse :init)))

(setf (get catkin_package::multiplierRequest :md5sum-) "a7d7d7065d45755acef7d4dcf908162a")
(setf (get catkin_package::multiplierRequest :datatype-) "catkin_package/multiplierRequest")
(setf (get catkin_package::multiplierRequest :definition-)
      "int32 a
int32 b
---
int32 result
")

(setf (get catkin_package::multiplierResponse :md5sum-) "a7d7d7065d45755acef7d4dcf908162a")
(setf (get catkin_package::multiplierResponse :datatype-) "catkin_package/multiplierResponse")
(setf (get catkin_package::multiplierResponse :definition-)
      "int32 a
int32 b
---
int32 result
")



(provide :catkin_package/multiplier "a7d7d7065d45755acef7d4dcf908162a")


