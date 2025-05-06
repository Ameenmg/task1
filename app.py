from flask import Flask, render_template, redirect, url_for, request
import os
import uuid

# ✨ OpenTelemetry Imports
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace

# ✨ إعداد التتبع
trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(
    endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://10.99.74.220:4318"),
    insecure=True
)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)  # ✨ ربط Flask مع التتبع

@app.route('/')
def home():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    my_name = os.getenv("MY_NAME")
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n ' + 'Name: '+ my_name

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
