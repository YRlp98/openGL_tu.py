import glfw
from OpenGL.GL import *
import numpy as np

# Iinitializing glfw library
if not glfw.init():
    raise Exception("glfx can not be initialized!")

# Create the window
window = glfw.create_window(1280, 780, "My OpenGL window", None, None)

# Check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created")

# Set window's position
glfw.set_window_pos(window, 400, 200)

# Make the context current
glfw.make_context_current(window)

#! My Codes

vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY) 
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)

glClearColor(0, 0.1, 0.1, 1)

# Loop until the user closes the window
while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

    #! My events
    glClear(GL_COLOR_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, 3)

# Termiante glfw
glfw.terminate()