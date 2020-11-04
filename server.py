import flask
import jinja2
import os

server = flask.Flask(__name__)
pdfnames = os.listdir("static/pdf")
pdfnames = ["".join(a.split('.')[:-1]) for a in pdfnames]
currentedition = open("config/current_edition_filename.txt").read()


@server.route("/")
def index():
    return flask.redirect("/index")


def formatted_page(template, **kwargs):
    """Returns the given template with the header and footer appended onto it"""
    return "\n".join([
        flask.render_template("header.html"),
        flask.render_template(template, **kwargs),
        flask.render_template("footer.html")])


@server.route("/<string:subpath>")
def template(subpath: str):
    try:
        return formatted_page("%s.html" % subpath, pdfs=pdfnames, pdfnow=currentedition)
    except jinja2.exceptions.TemplateNotFound:
        flask.abort(404)


if __name__ == '__main__':
    server.run()
