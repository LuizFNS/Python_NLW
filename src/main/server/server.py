from flask import Flask
from src.main.server.routes.event import event_route_bp
from src.main.server.routes.subscribers import subs_route_bp
from src.main.server.routes.events_link import events_link_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(subs_route_bp)
app.register_blueprint(events_link_route_bp)
