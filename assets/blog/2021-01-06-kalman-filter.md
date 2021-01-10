# KALMAN FILTER

https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/

Few software engineers and scientists seem to know about it
For systems which are continuously changing
Tool for combining information in the presence of uncertainty
When you have uncertain information about some dynamic system, and you can make an educated guess about what the system is going to do next.
Its ability to extract accurate information seems almost magical

![kalman filter](assets/blog/assets/kalman_filter.jpg)

* IMU - inertial measurement units
[Kalman filter-based IMU](https://www.bzarg.com/p/improving-imu-attitude-estimates-with-velocity-data/)
https://github.com/pms67/EKF-Quaternion-Attitude-Estimation
https://github.com/pms67/Attitude-Estimation


## More

http://www.allaboutcircuits.com/technical-articles/how-sensor-fusion-works/

The Kalman Filter
At its heart, the algorithm has a set of “belief” factors for each sensor. 
Each loop, data coming from the sensors is used to statistically improve the location guess, 
but the quality of the sensors is judged as well.

Robotic systems also include constraints that encode the real-world knowledge that 
physical objects move smoothly and continuously through space (often on wheels), rather 
than teleporting around like GPS coordinate samples might imply.

That means if one sensor which has always given excellent, consistent values starts 
telling you unlikely and frankly impossible things (such as GPS/radio systems when 
you go into a tunnel), that sensors' believability rating gets downgraded within a 
few millisecond iterations until it starts talking sense again.

This is better than just averaging or voting because the Kalman filter can cope 
with the majority of its sensors going temporarily crazy, so long as one keeps 
making good sense. It becomes the lifeline that gets the robot through the dark times.

The Kalman filter is an application of the more general concepts of Markov Chains 
and Bayesian Inference, which are mathematical systems that iteratively refine their 
guesses using evidence. These are tools designed to help science itself test ideas 
(and are the basis of what we call “statistical significance”).

![kalman_filter](img\Algorithms\kalman_filter.jpg)