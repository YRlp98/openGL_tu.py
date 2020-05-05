import glfw

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

# Loop until the user closes the window
while not glfw.window_should_close(window):
    # Render here, e.g. using pyOpenGL

    # Swap front and back buffers
    glfw.swap_buffers(window)

    # Poll for and process events
    glfw.poll_events()

# Termiante glfw
glfw.terminate()
