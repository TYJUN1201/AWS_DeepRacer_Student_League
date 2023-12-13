# AWS_DeepRacer_Student_League
AWS DeepRacer Student League is a place for high school and college-enrolled learners around the globe to develop machine learning (ML) skills. It provides access to educational material, the optional AWS AI &amp; ML Scholarship program, and the opportunity to train and test reinforcement learning (RL) models for the AWS DeepRacer Student League.

# General starting algorithm
An algorithm that marks 10 marker outwards from the centre line of the track, with fewer rewards the further away an agent is from the centre line.

# Radius_Target_Algorithm (Advanced Algorithm)
1. Create a circle with radius X centred on the agent and find the intersection point between the centre line of the track and the circle.
2. Calculates the angle formed between the front wheel of agents and this intersection point.
3. Provide feedback that the angle is inversely proportional to the reward (the smaller the angle, the larger the reward)

*Due to the limited number of track waypoints from the environmental feedback, the **up_sample(track_waypoints, Y_times)** function can expand the list of track waypoints by Y times to be used in calculating the **intersection point** in **step 2**.

# Radius_Target_Algorithm_2.0 (Advanced Algorithm BASED ON Radius_Target_Algorithm)
1. Create **3** circleS with radius R1, R2, R3 centred on the agent and find the intersection points between the centre line of the track and the circles.
2. Calculates the angle formed between the agent's front wheel and these intersection points.
3. Defines the maximum angle of the agent's front wheels, accepts the angle that are less than or equal to the threshold angle.
4. Provide feedback that the angle is inversely proportional to the reward (the smaller the angle, the larger the reward)

*Due to the limited number of track waypoints from the environmental feedback, the **up_sample(track_waypoints, Y_times)** function can expand the list of track waypoints by Y times to be used in calculating the **intersection point** in **step 2**.

