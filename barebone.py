from livereload import Server, shell
import sass
import os


def compile_sass():
    cwd = os.getcwd()
    scss_dir = os.path.join(cwd + "/style/sass/")
    css_dir = os.path.join(cwd + "/style/css/")
    scss = os.path.join(scss_dir + 'style.scss')
    css = os.path.join(css_dir + 'style.css')

    if not os.path.exists(scss):
        with open(scss, 'a'): pass
    if not os.path.exists(css):
        with open(css, 'a'): pass

    try:
        sass.compile(dirname=(scss_dir, css_dir))
        print('yoyoyo')
    except sass.CompileError:
        print('compile error')
        pass


def server():
    server = Server()
    server.watch('./style/sass/style.scss', compile_sass)
    server.serve(port=8080, host='localhost')


server()

