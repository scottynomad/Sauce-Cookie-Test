from cookieapp.base import application

def run():
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, application,
               use_debugger=True, use_reloader=True)

