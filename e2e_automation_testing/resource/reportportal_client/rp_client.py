import os
import subprocess
import traceback
from mimetypes import guess_type
from time import time

# Report Portal versions below 5.0.0:
from reportportal_client import ReportPortalServiceAsync

# Report Portal versions >= 5.0.0:
from reportportal_client import ReportPortalService


def timestamp():
    return str(int(time() * 1000))


endpoint = "http://10.6.40.6:8080"
project = "default"
# You can get UUID from user profile page in the Report Portal.
token = "1adf271d-505f-44a8-ad71-0afbdf8c83bd"
launch_name = "Test launch"
launch_doc = "Testing logging with attachment."


def my_error_handler(exc_info):
    """
    This callback function will be called by async service client when error occurs.
    Return True if error is not critical and you want to continue work.
    :param exc_info: result of sys.exc_info() -> (type, value, traceback)
    :return:
    """
    print("Error occurred: {}".format(exc_info[1]))
    traceback.print_exception(*exc_info)


# Report Portal versions below 5.0.0:
service = ReportPortalServiceAsync(endpoint=endpoint, project=project,
                                   token=token, error_handler=my_error_handler)

# Report Portal versions >= 5.0.0:
service = ReportPortalService(endpoint=endpoint, project=project,
                                   token=token)

# Start launch.
launch = service.start_launch(name=launch_name,
                              start_time=timestamp(),
                              description=launch_doc)

# Start test item Report Portal versions below 5.0.0:
test = service.start_test_item(name="Test Case",
                               description="First Test Case",
                               tags=["Image", "Smoke"],
                               start_time=timestamp(),
                               item_type="STEP",
                               parameters={"key1": "val1",
                                           "key2": "val2"})

# Start test item Report Portal versions >= 5.0.0:
item_id = service.start_test_item(name="Test Case",
                                  description="First Test Case",
                                  start_time=timestamp(),
                                  item_type="STEP",
                                  parameters={"key1": "val1",
                                              "key2": "val2"})


# Create text log message with INFO level.
service.log(time=timestamp(),
            message="Hello World!",
            level="INFO")

# Create log message with attached text output and WARN level.
service.log(time=timestamp(),
            message="Too high memory usage!",
            level="WARN",
            attachment={
                "name": "free_memory.txt",
                "data": subprocess.check_output("free -h".split()),
                "mime": "text/plain"
            })

# Create log message with binary file, INFO level and custom mimetype.
image = "/tmp/image.png"
with open(image, "rb") as fh:
    attachment = {
        "name": os.path.basename(image),
        "data": fh.read(),
        "mime": guess_type(image)[0] or "application/octet-stream"
    }
    service.log(timestamp(), "Screen shot of issue.", "INFO", attachment)

# Create log message supplying only contents
service.log(
    timestamp(),
    "running processes",
    "INFO",
    attachment=subprocess.check_output("ps aux".split()))

# Finish test item Report Portal versions below 5.0.0.
service.finish_test_item(end_time=timestamp(), status="PASSED")

# Finish test item Report Portal versions >= 5.0.0.
service.finish_test_item(item_id=item_id, end_time=timestamp(), status="PASSED")

# Finish launch.
service.finish_launch(end_time=timestamp())

# Due to async nature of the service we need to call terminate() method which
# ensures all pending requests to server are processed.
# Failure to call terminate() may result in lost data.
service.terminate()