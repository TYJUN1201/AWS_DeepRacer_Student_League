# AWS_DeepRacer_Student_League
AWS DeepRacer Student League is a place for high school and college-enrolled learners around the globe to develop machine learning (ML) skills. It provides access to educational material, the optional AWS AI &amp; ML Scholarship program, and the opportunity to train and test reinforcement learning (RL) models for the AWS DeepRacer Student League.

# General starting algorithm
An algorithm that marks 10 marker outwards from the centre line of the track, with fewer rewards the further away an agent is from the centre line.

# Radius_Target_Algorithm
1. Create a circle with radius X centred on the agent and find the intersection point between the centre line of the track and the circle.
2. Calculates the angle formed between the front wheel of agents and this intersection point.
*Due to the limited number of track waypoints from the environmental feedback, the **up_sample(track_waypoints, Y_times)** function can expand the list of track waypoints by Y times to be used in calculating the **intersection point** in **step 2**.
3. Provide feedback that the angle is inversely proportional to the reward (the smaller the angle, the larger the reward)


