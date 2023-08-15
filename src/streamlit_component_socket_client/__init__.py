from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_component_socket_client,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_component_socket_client", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_component_socket_client(
    key: Optional[str] = None,
    url: str = "http://localhost:5000",
    message: str = "Hello World!",
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key, url=url, message=message
    )
    return component_value


def main():
    st.write("## Example")
    value = streamlit_component_socket_client(
        url="http://139.177.201.45:5000", message="phone in water"
    )
    st.write(value)


if __name__ == "__main__":
    main()
