from typing import Any
import streamlit as st
import numpy as np

def animation_demo() -> None:
    # Interactive Streamlit elements with unique keys
    iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1, key="iterations")
    separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885, key="separation")

    # Progress bar with unique key
    progress_bar = st.sidebar.progress(0)
    frame_text = st.sidebar.empty()
    image = st.empty()

    # Julia Set parameters
    m, n, s = 960, 640, 400
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

    # Animation loop
    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
        # Update progress bar and frame counter
        progress_bar.progress(frame_num + 1)
        frame_text.text(f"Frame {frame_num + 1}/100")

        # Fractal calculation
        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M: Any = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        # Update image
        image.image(1.0 - (N / N.max()), use_column_width=True)

    # Clear widgets after animation
    progress_bar.empty()
    frame_text.empty()

    # Button with unique key
    st.button("Re-run", key="rerun_button")


# Page setup
st.set_page_config(page_title="Animation Demo", page_icon="📹")
st.markdown("# Animation Demo")
st.sidebar.header("Animation Demo")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the Julia Set. Use the slider
to tune different parameters."""
)

# Call the animation function
animation_demo()
