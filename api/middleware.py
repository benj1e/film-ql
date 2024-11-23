from fastapi import Request
from .logger import get_logger
import time


async def logging_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time
    middleware_log = get_logger("Runtime", "runtime.log")
    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "process-time": process_time,
    }

    middleware_log.info(log_dict, extra=log_dict)

    return response
