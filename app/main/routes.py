from app.main import bp

@bp.route("/")
def index():
    return "<span style='color:red;'>This is the main blueprint</span>"
