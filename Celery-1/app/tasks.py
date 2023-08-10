from __future__ import absolute_import , unicode_literals

import time
from core.celery import app

from .emails import send_review_email as send_email

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def send_review_email(message , recipient_list):

    logger.info('email successfull')
    # time.sleep(300)
    return send_email(message , recipient_list)

