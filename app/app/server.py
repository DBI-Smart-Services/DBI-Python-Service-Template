"""
This file should be used to be the main entry point for your app.
In here shouldn't be any logic, besides the logic to start your app.
"""
from dbi_pyton_service_template.DashView import create_dash_app
from dbi_pyton_service_template.Helper import get_system_default_config

if __name__ == "__main__":
    config = get_system_default_config()

    app = create_dash_app()
    app.run(host='0.0.0.0', port=config.port, debug=False)
