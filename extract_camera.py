# CODE TO GENERATE THE IMAGES AND CAMERA PARAMETERS FOR THE NERF DATASET
# This code is CREATED FOR EE526 COURSE PROJECT

import numpy as np
import os

# Create folders if they don't exist
os.makedirs('/home/pc-14-2/Desktop/EE526/test/image', exist_ok=True)
os.makedirs('/home/pc-14-2/Desktop/EE526/intrinsics', exist_ok=True)
os.makedirs('/home/pc-14-2/Desktop/EE526/pose', exist_ok=True)

# Get the active view
view = GetActiveView()

# Get the active source (assumed to be the object you want to rotate)
source = GetActiveSource()

# Get the active camera
camera = view.GetActiveCamera()

# Set the desired image size
image_size = (512, 512)
# Set the view size directly
view.ViewSize = image_size
# Get the number of views
num_views = 10
# Lists to store camera parameters
intrinsics_list = []
pose_list = []

# Iterate through different views
for view_index in range(num_views):
    # Rotate the camera to create a different view
    rotation_angle = 360.0 * view_index / num_views
    camera.Azimuth(rotation_angle)
    Render()

    # Save RGB image with the desired size
    SaveScreenshot(f'/home/pc-14-2/Desktop/EE526/test/image/image_{view_index}.png', view=view, TransparentBackground=1)

    # Get the camera position, focal point, and view up direction
    camera_position = np.array(camera.GetPosition())
    focal_point = np.array(camera.GetFocalPoint())
    view_up = np.array(camera.GetViewUp())

    # Calculate the camera direction (forward)
    camera_direction = focal_point - camera_position
    camera_direction /= np.linalg.norm(camera_direction)

    # Calculate the right and up directions
    camera_right = np.cross(view_up, camera_direction)
    camera_right /= np.linalg.norm(camera_right)