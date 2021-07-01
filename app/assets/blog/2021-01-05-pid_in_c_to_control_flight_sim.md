## PID - PROPORTIONAL–INTEGRAL–DERIVATIVE CONTROLLER

Feedback based control loop mechanism used to control systems requiring continuously modulated control
Used when requiring accurate and optimized automatic control
The PID controller 
- continuously calculates an error value e(t) = desired setpoint (SP) - measured process variable (PV)
- applies a correction based on proportional, integral, and derivative terms (denoted P, I, D)
- Ex: cruise control on a car
- hill ascending = lower speed if only constant engine power were applied
- PID algorithm will increase engine speed to target the measured speed to the desired speed with minimal delay.
- Historic: 1920, automatic steering systems for ships

download.code(https://raw.githubusercontent.com/pms67/PID/master/PID.h)
download.code(https://raw.githubusercontent.com/pms67/PID/master/PID.c)

- https://github.com/pms67/PID
- https://github.com/pms67/ControlSystemDesign-Tutorial/tree/master/BalancedAeropendulum

[PID Controller in C](https://www.youtube.com/watch?v=zOByx3Izf5U)

## More
- https://en.wikipedia.org/wiki/PID_controller

[Kalman filter-based IMU-inertial measurement units](https://www.bzarg.com/p/improving-imu-attitude-estimates-with-velocity-data/)
Automatic differentiation makes a linearized extended Kalman filter (EKF) particularly easy and robust to implement.