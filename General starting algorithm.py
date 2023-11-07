def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.13 * track_width
    marker_3 = 0.17 * track_width
    marker_4 = 0.2 * track_width
    marker_5 = 0.25* track_width
    marker_6 = 0.3 * track_width
    marker_7 = 0.35 * track_width
    marker_8 = 0.4 * track_width
    marker_9 = 0.45 * track_width
    marker_10 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.95
    elif distance_from_center <= marker_3:
        reward = 0.9
    elif distance_from_center <= marker_4:
        reward = 0.85
    elif distance_from_center <= marker_5:
        reward = 0.8
    elif distance_from_center <= marker_6:
        reward = 0.6
    elif distance_from_center <= marker_7:
        reward = 0.3
    elif distance_from_center <= marker_8:
        reward = 0.1
    elif distance_from_center <= marker_9:
        reward = 0.01
    elif distance_from_center <= marker_10:
        reward = 0.001

    return float(reward)
