# app.py (Modified to fix routing)
import dash
import dash_bootstrap_components as dbc
import os # <-- 1. Import os module

# 2. Get the base path from the environment. 
# It defaults to '/' for local use or when the deployment root is '/'.
# Render uses the full URL as the base, which is why this is important.
APP_PATH_PREFIX = os.environ.get('DASH_REQUESTS_PATHNAME_PREFIX', '/')

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # **3. CRITICAL LINE: Tell Dash its base path.**
    requests_pathname_prefix=APP_PATH_PREFIX,
    url_base_pathname=APP_PATH_PREFIX
) 

app.config.suppress_callback_exceptions = True
app.title = "Optick Analytics"
server = app.server
