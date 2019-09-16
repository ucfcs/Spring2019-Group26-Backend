from asltutor.main import app

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        pass
