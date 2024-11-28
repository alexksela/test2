import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="ServiceBusQueueTrigger1")
@app.service_bus_queue_trigger(arg_name="message", 
                                queue_name="genai_ingest_1 ", 
                                connection="Endpoint=sb://dev-scop.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=enT5ugiWnZtqkufezzJ9cDIVWWkUM0Bp0+ASbCKhLbU=")
def test_function(message: func.ServiceBusMessage):
    try:
        message_body = message.get_body().decode("utf-8")
        logging.info("Python ServiceBus queue trigger processed message.")
        logging.info(f"Message Body: {message_body}")
        logging.info(f"Message ID: {message.message_id}")
    except Exception as e:
        logging.error(f"Error processing message: {e}")
