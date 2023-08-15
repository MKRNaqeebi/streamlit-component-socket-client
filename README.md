# streamlit-component-socket-client

socket client which allow you to use and render session tate with out to wait for socket.

## Installation instructions 

```sh
pip install streamlit-component-socket-client
```

## Usage instructions

```python
import streamlit as st

from streamlit_component_socket_client import streamlit_component_socket_client

value = streamlit_component_socket_client()

st.write(value)
