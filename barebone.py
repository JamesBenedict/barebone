from livereload import Server, shell
import sass
import os


def compile_sass():
    scss =  "style/style.scss"
    css = "style/style.css"

    if not os.path.exists(scss):
        with open(scss, 'a'): pass

    if not os.path.exists(css):
        with open(css, 'a'): pass

    try:
        sass.compile(dirname=("style", "style"))
        print('yoyoyo')
    except sass.CompileError:
        pass


def server():
    server = Server()
    server.watch('style/style.scss', compile_sass)
    server.serve(port=8080, host='localhost')


server()

